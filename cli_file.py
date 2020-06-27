import argparse
import glob
import os
import shutil
import sys


class ArgumentError(Exception):
    pass


def create_parser():
    # Parser is defined to control the project flow in the later parts of the project.
    parser = argparse.ArgumentParser(prog='BOLD fMRI Process',
                                     description='Localizing the brain area that processes faces with BOLD fMRI')

    parser.add_argument('-p', '--pre-process', action='store_true',
                        help='When the flag is activated, pre-processes the data before localization.')
    parser.add_argument('--use-pre', action='store_true',
                        help='When the flag is activated, uses pre-processed data to localize faces.')
    parser.add_argument('--pipeline', default='pipeline.sh', type=str,
                        help='Specifies the path to the bash code that will create the pipeline, '
                             'leave it as default to work normally.')
    parser.add_argument('--data-folder', default='data/raw', type=str,
                        help='Specifies the path to the folder containing the raw data.')
    parser.add_argument('--pre-data-folder', default='data/processed', type=str,
                        help='Specifies the path to the folder where the processed '
                             'data is located or to be saved after pre-processing.')
    parser.add_argument('--input-file', default='bold.nii.gz', type=str)
    parser.add_argument('--output-file', default='clean_bold.nii.gz', type=str)

    args = parser.parse_args()

    # To predict wrong situations before it happens
    try:
        if args.pre_process and args.use_pre:
            raise ArgumentError
        return parser

    except ArgumentError as err:
        print("Both pre-processing and pre-processed "
              "data cannot be used at the same time")
        sys.exit(0)


def folder_manipulation(args):
    raw_dirs = glob.glob(os.path.join(args.data_folder, '**'))
    print(f'Total Patient Count: {len(raw_dirs)}')
    if args.pre_process or args.use_pre:
        processed_dirs = [proc_dir.replace('raw', 'processed') for proc_dir in raw_dirs]
        if args.use_pre:
            for d in processed_dirs:
                if not os.path.isdir(d):
                    print('Raw directory and processed data directories are not matched.')
                    print(f'\t"{d}" is not directory or not exists.')
                    sys.exit(0)
            print("Using older pre-processed datas")
            print_dir(len(raw_dirs))
            return raw_dirs, processed_dirs

        elif args.pre_process:
            decision = input('\nBefore new pre-process, all old preprocessed files will be deleted. '
                             '\nDo you confirm:\n[Y][n] ')
            if decision == "Y" or decision == "y":
                count = 0
                for d in processed_dirs:
                    if os.path.isdir(d):
                        count += 1
                        shutil.rmtree(d)
                        print(f"{d} directory exists, removed.")
                print("Creating new pre-processed datas")
                print_dir(len(raw_dirs), count)
                return raw_dirs, processed_dirs
            else:
                sys.exit()
    print("Using only raw datas")
    print_dir(len(raw_dirs))
    return raw_dirs


def print_dir(raw_count, exist_dir=None):
    print(f"Total patient count in raw dir: {raw_count}")
    if exist_dir is not None:
        print(f"Already pre-processed and removed patient data: {exist_dir}")
