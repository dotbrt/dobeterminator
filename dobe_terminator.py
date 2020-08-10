#!/usr/bin/env python3
import subprocess, signal
import os, sys
p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
out, err = p.communicate()

for line in out.splitlines():
    adobes = [
        "Adobe Desktop Service",
        "Core Sync",
        "Core Sync Helper",
        "CCXProcess",
    ]
    if any(adobe in line.decode('utf-8') for adobe in adobes):
        pid = int(line.split(None, 1)[0])
        os.kill(pid, signal.SIGKILL)
print("\nKilled! 💩\n")
sys.exit()
