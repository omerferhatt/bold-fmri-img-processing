import warnings

from cli_file import *
from localize import *
from preprocess import *
from vis import *

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    parser = create_parser()
    args = parser.parse_args()

    if not (args.use_pre or args.pre_process):
        raw_dir = folder_manipulation(args)
        raw_dir.sort()
        args.output_file = args.input_file
        if args.localize:
            for path in raw_dir:
                localize(args, path)
            print('Localizing completed!')

    else:
        raw_dir, pre_dir = folder_manipulation(args)
        raw_dir.sort()
        pre_dir.sort()
        if args.pre_process:
            for r_d, p_d in zip(raw_dir, pre_dir):
                preprocess(args, r_d, p_d)
            print('Pre-process completed!')

        if args.localize:
            for path in pre_dir:
                localize(args, path)
            print('Localizing completed!')

        if args.visualize_corr and (type(args.select_data) is list and len(args.select_data) == 1):
            for r, p in zip(raw_dir, pre_dir):
                visualize(r, p)
