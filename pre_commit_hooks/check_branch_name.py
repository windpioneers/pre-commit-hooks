import argparse
import re
from typing import Optional
from typing import Sequence
import subprocess


def main(argv: Optional[Sequence[str]] = None) -> int:
    """ Returns 0 if the current git branch name matches at least one of the regexes provided as an argument
    If no matches are found, returns 1.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'regexes',
        nargs='*',
        help='Valid regexes for a branch name',
    )

    current_branch_name = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode('ascii').strip()

    args = parser.parse_args(argv)
    for regexp in args.regexes:
        if re.match(regexp, current_branch_name):
            return 0

    # Return 0 if there are no regexes given
    return 1 if len(args.regexes) > 0 else 0


if __name__ == '__main__':
    exit(main())
