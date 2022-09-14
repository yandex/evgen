#!/usr/bin/env python3

import sys
from unittest import TestCase, TestSuite, TextTestRunner

from evgen.events_checker import EventsChecker
from evgen.scripts import run_evgen


class TestConsistency(TestCase):
    def __init__(self, events_path, evgen_config_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.events_checker = EventsChecker(
            events_path=events_path, evgen_config_path=evgen_config_path
        )

    def test_generation(self):
        self.events_checker.check_generation()

    def test_consistency(self):
        self.events_checker.check_consistency()


def main():
    parser = run_evgen.get_arg_parser()
    parser_args = parser.parse_args()
    suite = TestSuite()
    suite.addTest(
        TestConsistency(
            parser_args.events_path, parser_args.evgen_config_path, "test_generation"
        )
    )
    suite.addTest(
        TestConsistency(
            parser_args.events_path, parser_args.evgen_config_path, "test_consistency"
        )
    )
    runner = TextTestRunner(verbosity=2)
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)


if __name__ == "__main__":
    main()
