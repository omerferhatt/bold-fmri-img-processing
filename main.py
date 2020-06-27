from cli_file import *

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    dirs = folder_manipulation(args)
