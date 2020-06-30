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
    parser.add_argument('-u', '--use-pre', action='store_true',
                        help='When the flag is activated, uses pre-processed data to localize faces.')
    parser.add_argument('-l', '--localize', action='store_true')
    parser.add_argument('--pipeline', default='pipeline.sh', type=str,
                        help='Specifies the path to the bash code that will create the pipeline, '
                             'leave it as default to work normally.')
    parser.add_argument('-S', '--select-data', default='', nargs='+',
                        help='Select data, otherwise all of them going to be used.')
    parser.add_argument('--data-folder', default='data/raw', type=str,
                        help='Specifies the path to the folder containing the raw data.')
    parser.add_argument('--pre-data-folder', default='data/processed', type=str,
                        help='Specifies the path to the folder where the processed '
                             'data is located or to be saved after pre-processing.')
    parser.add_argument('-i', '--input-file', default='bold.nii.gz', type=str)
    parser.add_argument('-o', '--output-file', default='clean_bold.nii.gz', type=str)
    parser.add_argument('-e', '--event-file', default='events.tsv', type=str)
    parser.add_argument('-H', '--hrf-file', default='hrf.csv', type=str)
    parser.add_argument('-t', '--template', default='template.nii.gz', type=str,
                        help='Specifies the path to template T1 space, '
                             'leave it as default to work normally.')
    parser.add_argument('-b', '--batch_process', action='store_true')
    parser.add_argument('-v', '--visualize-corr', action='store_true')
    args = parser.parse_args()

    # To predict wrong situations before it happens
    try:
        if args.pre_process and args.use_pre:
            raise ArgumentError
        return parser

    except ArgumentError:
        print("Both pre-processing and pre-processed "
              "data cannot be used at the same time")
        sys.exit(0)


def folder_manipulation(args):
    if args.select_data != '':
        raw_dirs = [os.path.join(args.data_folder, p) for p in args.select_data]
    else:
        raw_dirs = glob.glob(os.path.join(args.data_folder, '**'))

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
            decision = input('Before new pre-process, all old preprocessed files will be deleted. '
                             '\nDo you confirm:\n[Y][n] ')
            if decision == "Y" or decision == "y":
                count = 0
                for d in processed_dirs:
                    if os.path.isdir(d):
                        count += 1
                        shutil.rmtree(d)
                        print(f"{d} directory exists, removed.")
                print("Creating new pre-processed datas\n")
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

