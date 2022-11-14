import argparse

from crontab import CronTab

parser = argparse.ArgumentParser(description="Argument for log archives")
parser.add_argument("username", type=str, help="username for cron")
parser.add_argument("path", type=str, help="path of the log_archive file")
parser.add_argument("-i", type=int, default=30, help="launch interval in days(default: 30)")
parser.add_argument("-c", type=str, default="log_gz", help="comment for job in cron(default: log_gz)")

args = parser.parse_args()

my_cron = CronTab(user=args.username)

COMMENT = args.c
INTERVAL = args.i


def add_new_job(_path):
    _job = my_cron.new(command=f"python3 {_path}", comment=COMMENT)
    _job.minute.every(1)
    my_cron.write()
    return f"New job {COMMENT} added to corn"


def main():
    print(add_new_job(args.path))


if __name__ == "__main__":
    main()
