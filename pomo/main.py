'''
    pomo cli
        commands:
            start: Start the clock.
                -d | --duration: duration in minutes or seconds.
                -s | --short: short break (5 minutes).
                -l | --long: long break (15 minutes).
            status: Show how much time is left in the current pomo tracker. 
                -f | --format: show the time in a specific format.
            stop: Stop the clock & reset.
            pause: Pause the clock & no reset.
            config: Config the pomo clock.

The pomo cli tool should do the following:
1. Keep track of the current countdown timer. This can be accomplished by having a temp file with the
original start time as reference.
2. When the timer has expired, the pomo cli tool should notify the user the time with flashing the terminal
and playing a 'beep' sound.
* Instead of having a timestamp file for start/paused, have the script determine when the
expected time for the alarm to go off, when the time expires, sound the alarm.
* Can do something like eval in basic bash to run a subprocess:
    $ eval "sleep 4 && echo $test"&
    [1] 41569

Pomo directory:
- $HOME/.config/pomo/ : The configuration directory
- /tmp/pomo/ : Where the throw away files will be located

Possible:
- Show the remanining time in tmux status bar, ex: (12:43)

'''

import argparse
import sys
from typing import Optional
from typing import Sequence

import pomo.constants as C

from pomo.commands.start import start
from pomo.commands.pause import pause
from pomo.commands.status import status
from pomo.commands.stop import stop
from pomo.commands.config import config


def main(argv: Optional[Sequence[str]] = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]

    parser = argparse.ArgumentParser(
        prog='pomo',
        description='A Pomodor timer command line interface tool.',
    )

    parser.add_argument(
        '-V',
        '--version',
        action='version',
        version=f'%(prog)s {C.VERSION}',
    )

    subparser = parser.add_subparsers(dest='command')

    # add the start command
    start = subparser.add_parser('start', help='Start the pomo timer.')
    start.add_argument("-d", "--duration", default=25 ,help="The duration of the pomo timer. Default 25 minutes.")
    start.add_argument("-s", "--short-break", default=5, help="Take a short break. Default 5 minutes.")
    start.add_argument("-l", "--long-break", default=10, help="Take a long break. Default 10 minutes.")

    # add the stop command
    stop = subparser.add_parser('stop', help='Stop and reset the pomo timer.')

    # add the pause command
    pause = subparser.add_parser('pause', help='Pause the pomo timer.')

    # add the status command
    status = subparser.add_parser('status', help='Show the current status of the pomo timer.')

    # add the config command
    config = subparser.add_parser('config', help='Configure the pomo timer.')

    # add help command
    help = subparser.add_parser('help', help='Show help for a specific command.')
    help.add_argument('help_cmd', nargs='?', help='Command to show help for.')

    if len(argv) == 0:
        parser.parse_args(['--help'])
        return 0

    args = parser.parse_args(argv)

    if args.command == 'help' and args.help_cmd:
        parser.parse_args([args.help_cmd, '--help'])
        return 0
    elif args.command == 'help':
        parser.parse_args(['--help'])
        return 0

    args = parser.parse_args(argv)

if __name__ == '__main__':
    SystemExit(main())
