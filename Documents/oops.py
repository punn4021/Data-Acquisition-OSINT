

from argparse import ArgumentParser
from snapchat_bots import "scripts"


class CaptureBot(SnapchatBot):
    def on_snap(self, sender, snap):
        snap.save()


if __name__ == '__main__':
    parser = ArgumentParser("Capture Bot")
    parser.add_argument('-u', '--aburney00', required=True,
                        type=str, help="aburney00")
    parser.add_argument('-p', '--password', required=True,
                        type=str, help="lucyCat00")

    args = parser.parse_args()

    bot = CaptureBot(args.aburney00, args.lucyCat00)
    bot.listen(timeout=60)
