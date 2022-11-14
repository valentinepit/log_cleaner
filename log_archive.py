import datetime
import os
import subprocess
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

work_dir = "/var/log"
try:
    sudo_pas = os.environ["MY_SUDO_PASS"]
except KeyError:
    sudo_pas = ""


def files_generator():
    for file in os.listdir(work_dir):
        if file.endswith(".log"):
            proc = subprocess.Popen(
                f"sudo -S chmod 666 {work_dir}/{file}".split(),
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            proc.communicate(sudo_pas.encode())
            yield file


def compress_file(_file, now):
    file_name = f"{work_dir}/{_file}"
    subprocess.call(["sudo", "gzip", f"--suffix={now}.gz", file_name])


def main():
    now = datetime.datetime.now().date()
    for f in files_generator():
        compress_file(f, now)


if __name__ == "__main__":
    main()
