import os
import subprocess
import sys


def _run(name):
    executable = os.path.join(os.path.dirname(__file__), "data", "bin", name)
    return subprocess.call([executable] + sys.argv[1:])


def python3():
  raise SystemExit(_run("python3"))


if __name__ == "__main__":
  python3()
