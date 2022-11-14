This is a script for archive log files in /var/log in a defined interval.

Script creates cron job for this task.
- Default period is 30 days
- Default comment for cron is a "log_gz"

First You have to type 
pip install -r requirements.txt

If You need a permission to change files in /var/log - insert Your password in .env

To create cron job You need to start cron_editor with arguments:
python cron_editor.py [path] [username] {-i interval} {-c comment}

- path: absolute path to log_archive.py
- username: username for crontab
- i: interval in days
- comment: comment for job in crontab


example:
python cron_editor.py admin /home/admin/scripts/log_cleaner/log_archive.py -i 20
