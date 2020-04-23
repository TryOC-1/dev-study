import argparse
import logging

import pandas as pd
from create_chart import draw_chart, save_chart_png, set_matplotlib


def check_level(args):
    message = "checking level"

    if args.level == "debug":
        logging.debug(message)
    elif args.level == "info":
        logging.info(message)
    elif args.level == "warning":
        logging.warning(message)
    elif args.level == "error":
        logging.error(message)


def _set_log_level(level: str) -> None:
    logger = logging.getLogger()
    if level == "debug":
        logger.setLevel(logging.DEBUG)
    elif level == "info":
        logger.setLevel(logging.INFO)
    elif level == "warning":
        logger.setLevel(logging.warning)
    elif level == "error":
        logger.setLevel(logging.error)


def create_chart(args):
    # set log level to INFO
    _set_log_level(args.setlevel or "info")

    # initialize matplotlib
    set_matplotlib()

    df = pd.read_csv(args.file, encoding="euc-kr")
    df["분양가격(㎡)"] = pd.to_numeric(df["분양가격(㎡)"], errors="coerce")
    df["분양가격(㎡)"].fillna(df["분양가격(㎡)"].mean())

    if args.stations:
        df = df[df["지역명"].isin(args.stations)]

    filename = draw_chart(args.type, df)
    save_chart_png(filename)


def get_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="sub-command help")

<<<<<<< HEAD
    ht = "check log level"
    parser_check_level = subparsers.add_parser("check-level", help=ht)
    parser_check_level.add_argument(
        "level",
        type=str,
        choices=["debug", "info", "warning", "error"],
        help="The level of log message",
    )
    parser_check_level.set_defaults(func=check_level)

    ht = "create chart"
    parser_create_chart = subparsers.add_parser("create-chart", help=ht)
    parser_create_chart.add_argument("file", type=str, help="input csv file")
    parser_create_chart.add_argument(
        "-t", "--type", type=str, choices=["line", "bar", "pie"], default="bar"
    )
    parser_create_chart.add_argument(
        "-s", "--stations", type=str, help="stations name with `,`"
    )
    parser_create_chart.add_argument(
        "-l", "--setlevel", type=str, choices=["debug", "info", "warning", "error"]
    )
    parser_create_chart.set_defaults(func=create_chart)
=======
    # TODO: Add `check-level subparser
    parser_check = subparsers.add_parser("check-level", help="check log level")
    parser_check.add_argument(
        "{debug,info,warning,error}", help="the level of log message"
    )

    # TODO: Add `create-chart` subparser
    parser_create = subparsers.add_parser("create-chart", help="create chart")
    parser_create.add_argument("file", type=str, help="input csv file")
    parser_create.add_argument(
        "-t", "--type", choices=["line", "bar", "pie"], default="bar"
    )
    parser_create.add_argument("-s", "--stations", help="stations name with `,`")
    parser_create.add_argument(
        "-l", "--setlevel", choices=["debug", "info", "warning", "error"]
    )
    parser_create.set_defaults(func=create_chart)
>>>>>>> Update all files to pass static check

    return parser
