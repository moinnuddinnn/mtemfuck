#!/usr/bin/env python3

#custem shell
#a friendly, extendable shell, supports history, external commands etc

import os
import shlex
import subprocess
import readline   # handy line editing & history
import sys

HISTORY_FILE = os.path.expanduser("~/.my_py_shell_history")
try:
    readline.read_history_file(HISTORY_FILE)
except FileNotFoundError:
    pass

def save_history():
    try:
        readline.write_history_file(HISTORY_FILE)
    except Exception:
        pass

def run_cmd(cmdline):
    parts = shlex.split(cmdline)
    if not parts:
        return
    cmd = parts[0]
    if cmd in ('exit','quit'):
        save_history()
        sys.exit(0)
    if cmd == 'cd':
        try:
            os.chdir(parts[1] if len(parts)>1 else os.path.expanduser("~"))
        except Exception as e:
            print("cd:", e)
        return
    if cmd == 'help':
        print("Builtins: cd, exit, help")
        return
    # run external command
    try:
        subprocess.run(parts)
    except FileNotFoundError:
        print(f"{cmd}: command not found")
    except Exception as e:
        print("Error:", e)

def main():
    try:
        while True:
            cwd = os.getcwd()
            prompt = f"\033[1;32mmysh\033[0m:\033[1;34m{cwd}\033[0m$ "
            line = input(prompt)
            run_cmd(line)
    except (EOFError, KeyboardInterrupt):
        print()
        save_history()

if __name__ == "__main__":
    main()