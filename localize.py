import os

import nibabel as nib
import numpy as np
import pandas as pd
from scipy import signal as sig


def localize(args, path):
    os.chdir(path)
    print(f"Localizing {path}")
    mri_file = args.output_file
    event_file = args.event_file
    hrf_file = args.hrf_file
    mri = nib.load(mri_file)
    events = pd.read_csv(event_file, delimiter='\t')
    events = events.to_numpy()

    hrf = pd.read_csv(os.path.join('../..', hrf_file))
    hrf = hrf.to_numpy()
    hrf = np.squeeze(hrf)

    tr = mri.header.get_zooms()[3]

    ts = np.zeros(int(tr * mri.shape[3]))

    for i in range(events.shape[0]):
        if events[i, 3] == 'FAMOUS' or events[i, 3] == 'UNFAMILIAR' or events[i, 3] == 'SCRAMBLED':
            ts[int(events[i, 0])] = 1

    convolved = sig.convolve(ts, hrf, mode='full')
    convolved = convolved[0:ts.shape[0]]
    convolved = convolved[0::2]
    img = mri.get_data()

    meansub_img = img - np.expand_dims(np.mean(img, 3), 3)
    meansub_conv = convolved - np.mean(convolved)

    correlation = (np.sum(meansub_img * meansub_conv, 3) /
                   (np.sqrt(np.sum(meansub_img * meansub_img, 3)) *
                    np.sqrt(np.sum(meansub_conv * meansub_conv))))

    ni_img = nib.Nifti1Image(correlation, mri.affine)
    print(f'Saving corr.nii.gz on {path}')
    nib.save(ni_img, 'corr.nii.gz')
    if args.batch_process:
        print(f'Registrating corr.nii.gz and t1.nii.gz. Saved as corr_in_t1.nii.gz in {path}\n')
        cmd = 'flirt -in corr.nii.gz -ref t1.nii.gz -applyxfm -init epireg.mat -out corr_in_t1.nii.gz'
        os.system(cmd)
    else:
        print('\n')
    os.chdir('../../..')


def register_template(pre):
    s = np.zeros((193, 229, 193))
    count = 0
    aff = np.zeros((4, 4))
    for p in pre:
        count += 1
        os.chdir(p)
        print(f'Registering {p} to template\n')
        os.system('sh template.sh')
        corr = nib.load('corr_in_template.nii.gz')
        corr_data = corr.get_data()
        aff += corr.affine
        s += corr_data
        os.chdir('../../..')
    s /= count
    aff /= count
    avg_corr = nib.Nifti1Image(s, aff)
    nib.save(avg_corr, 'data/global_avg_corr_in_template.nii.gz')
