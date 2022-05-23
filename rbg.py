import os
import random
import requests as r

def main():
	print("Example: /sdcard/DCIM/camera")
	
	key = random.choice(['C11K4kWoRkPotbh6fk5y8SHj','pTNM2McuSRZBphpZ7NMUKfM1','Gc5HuejRCbZnU9yRDLTN1w83','WZX8woiVWfRuyw96jk2r5EVi','aCetdbap1aAKVNSufAQ8bbXQ','i1pvm6bCv88HiyFJYNdAcHw6','mPwnGTAJTEE4HwwJTzUSGUj2','9UhrsicgYrfh9NswadvgmYc3','WEFrnkQc3CMHxyhmnjRMRzuY','HJFTmChoh5RFXVT85onTY1MJ','6Mi1bsr8eHH13sizGeZvpWKK','W6EWZMXTzvRXHhNa14chkbmg','v6DyB7bsKwg2GGNjiMPTzwqJ','m291Cg6yQsPmADofC6KxF6x7','N5aJtZgF9fBf2szSwfKgc1X5'])
	path = input("Path to folder: ")
	color = input("Background color: ")
	respath = f"{path}/hasil"
	
	for file in os.listdir(path):
		nameonly = os.path.splitext(file)[0]
		filepath = f"{path}/{file}"
		if os.path.isfile(filepath):
			raw = r.post('https://api.remove.bg/v1.0/removebg',files={'image_file': open(filepath, 'rb')},data={'size': 'auto','bg_color': color},headers={'X-Api-Key': key})
			if raw.status_code == r.codes.ok:
				if not os.path.isdir(respath): os.system(f"mkdir {respath}")
				with open(f"{respath}/{nameonly}.png", 'wb') as save:
					save.write(raw.content)
					print(f"[ok] {file}")
			else:
				print(f"[error] {raw.status_code} {raw.text}")

if __name__=="__main__":
	main()