import os
import sys

import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np


def visualize(raw_path, pre_path):
    file = 'corr.nii.gz'

    raw_corr = os.path.join(raw_path, file)
    pre_corr = os.path.join(pre_path, file)

    if not (os.path.exists(raw_corr) or os.path.exists(pre_corr)):
        print(f'{file} not found')
        return
    print(f"Saving figures into {pre_corr}\n")

    raw_corr = nib.load(raw_corr).get_data()
    pre_corr = nib.load(pre_corr).get_data()

    start = 1
    stop = -2
    r = 5
    c = 6

    raw_corr = raw_corr[:, :, start:stop]
    pre_corr = pre_corr[:, :, start:stop]
    fig_raw, ax_raw = plt.subplots(r, c, figsize=(15, 15))
    fig_pre, ax_pre = plt.subplots(r, c, figsize=(15, 15))
    fig_over, ax_over = plt.subplots(r, c, figsize=(15, 15))

    for row in range(r):
        for col in range(c):
            ax_raw[row, col].imshow(np.rot90(raw_corr[:, :, (row * r) + col]), cmap='gray')
            ax_raw[row, col].axis('off')

            ax_pre[row, col].imshow(np.rot90(pre_corr[:, :, (row * r) + col]), cmap='magma')
            ax_pre[row, col].axis('off')

            ax_over[row, col].imshow(np.rot90(raw_corr[:, :, (row * r) + col]), cmap='gray')
            ax_over[row, col].imshow(np.rot90(pre_corr[:, :, (row * r) + col]), alpha=0.6, cmap='magma')
            ax_over[row, col].axis('off')

    fig_raw.savefig(os.path.join(pre_path, 'corr_raw.png'), dpi=600, bbox_inches='tight')
    fig_pre.savefig(os.path.join(pre_path, 'corr_pre.png'), dpi=600, bbox_inches='tight')
    fig_over.savefig(os.path.join(pre_path, 'corr_overlay.png'), dpi=600, bbox_inches='tight')

    sys.exit(0)


if __name__ == '__main__':
    visualize(['data/raw/patient01'], ['data/processed/patient01'])
