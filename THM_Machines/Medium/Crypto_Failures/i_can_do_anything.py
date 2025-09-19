import os
import requests
import urllib
import subprocess

"""
i can't explain it enough, its just working ;_;
"""

URL = "http://10.201.50.77/index.php"
charset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-{}`~!@#$%^&*()+=[]\\|:;\'<>,.?/';
def getNewCookie(userAgent):
	while True:
		header = {"User-Agent":userAgent}
		res = requests.get(URL,allow_redirects=False,headers=header)
		decoded_res = urllib.parse.unquote(res.headers["Set-Cookie"])
		secure_cookie = decoded_res.split("=")[1].split(";")[0]
		salt = secure_cookie[:2]
		chunks = secure_cookie.split(salt)[1:]
		chunks2 = list(filter(lambda x:len(x)==11,chunks))
		if len(chunks) == len(chunks2):
			break
	final_chunks = list(map(lambda x: salt + x, chunks))
	print(final_chunks)
	return final_chunks

def blockOracle():
	flag = ''
	Block_Size = 7 # cause of colon appended
	Block_len = 6 # gonna increase it
	userAgent = "AA"
	previous_chars = ""
	counter = 0
	current_block = 1
	found = ""
	while True:
		found = ""
		for i in range(Block_Size):
			suffix = "A" * ((Block_len + counter) - i)
			secure_cookie = getNewCookie(userAgent+suffix)
			chunk = secure_cookie[current_block]
			if current_block == 1:
				previous_chars = suffix + ":"
			for char in charset:
				if current_block == 1:
					cmd_text = f"php experiment.php {previous_chars + found + char} {chunk[:2]}"
				else:
					cmd_text = f"php experiment.php '{previous_chars[i:] + found + char}' '{chunk[:2]}'"
				output = subprocess.run(cmd_text, capture_output=True, check=True, text=True, shell=True)
				output = output.stdout
				print(f"trying with char {char} and ouput is {output} and chunk is {chunk}")
				if output == chunk:
					flag += char
					found += char
					print(f"Found the char {char}")
					print(f"Found the flag {flag}")
					break
		previous_chars = found	
		current_block += 1
		counter += 1

blockOracle()