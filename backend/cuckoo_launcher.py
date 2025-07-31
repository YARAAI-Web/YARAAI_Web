import subprocess

subprocess.Popen(
    ["ssh", "babo@192.168.88.130", "nohup cuckoo > /dev/null 2>&1 &"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
)
