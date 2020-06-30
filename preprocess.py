import os
import shutil


def preprocess(args, raw, processed):
    if not os.path.exists(processed):
        os.mkdir(processed)
    copytree(raw, processed)
    shutil.copyfile(args.pipeline, os.path.join(processed, 'pipeline.sh'))
    print(os.getcwd())
    os.chdir(processed)
    print('---------------------------------------------------------------------')
    print(f"Data pre-processs {processed.split('/')[-1]}\n")
    print(os.getcwd())
    cmd = 'sh pipeline.sh'
    os.system(cmd)
    os.chdir('../../..')


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
