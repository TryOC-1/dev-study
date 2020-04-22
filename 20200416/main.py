from cli import get_parser
from utils import set_logger

if __name__ == "__main__":
    set_logger()
    parser = get_parser()
    args = parser.parse_args()

    try:
        args.func(args)
    except AttributeError:
        parser.print_help()
