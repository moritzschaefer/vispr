# coding: utf-8
from __future__ import absolute_import, division, print_function

import argparse
import logging
import sys
import string
import random
import os

import yaml

from vispr import TargetResults, Results, VisprError
from vispr.server import app


def init_server(*configs):
    app.results = Results()
    for path in configs:
        with open(path) as f:
            config = yaml.load(f)
            try:
                app.results.add(config)
            except KeyError as e:
                raise VisprError("Syntax error in config file {}. Missing key {}.".format(path, e))
    app.secret_key = ''.join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(30)
    )
    app.run()


def main():
    # create arg parser
    parser = argparse.ArgumentParser(
        "An HTML5-based interactive visualization of CRISPR/Cas9 screen data."
    )
    parser.add_argument("--debug", action="store_true", help="Print debug info.")
    subparsers = parser.add_subparsers(dest="subcommand")

    server = subparsers.add_parser("server")
    server.add_argument(
        "config",
        nargs="+",
        help="YAML config files. Each file points to the results of one "
             "MAGeCK test run."
    )

    test = subparsers.add_parser("test")

    args = parser.parse_args()

    logging.basicConfig(
        format="%(message)s",
        level=logging.DEBUG if args.debug else logging.INFO,
        stream=sys.stderr,
    )

    try:
        if args.subcommand == "server":
            init_server(*args.config)
        elif args.subcommand == "test":
            os.chdir(os.path.join(os.path.dirname(__file__), "tests"))
            init_server("config.yaml")
        else:
            parser.print_help()
            exit(1)
    except VisprError as e:
        logging.error(e)
        exit(1)
    except ImportError as e:
        print(
            "{}. Please ensure that all dependencies from "
            "requirements.txt are installed.".format(e),
            file=sys.stderr
        )
        exit(1)
    exit(0)
