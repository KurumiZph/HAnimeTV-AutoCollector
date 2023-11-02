#THIS FILE RUNS THE OTHER FILES ONE BY ONE AND WAITS FOR THEM TO FINISH
import subprocess

def run_script(script_name):
    subprocess.run(["python", script_name])
#THIS IS TO CONFIGURE WICH SCRIPTS SHOULD BE RAN
if __name__ == "__main__":
    scripts = ["getcoins.py", "append.py", "webhook.py"]
#-CONFIG END-

    for script in scripts:
        run_script(script)
