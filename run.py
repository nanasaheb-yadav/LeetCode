import subprocess

out = subprocess.run("env.sh", stdout=subprocess.PIPE, shell=True)
print(out.returncode)