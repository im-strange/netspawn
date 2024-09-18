#!/usr/bin/env python3

# colors
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'

toolname = "netspawn"

try:
	import subprocess
	import argparse
	import requests
	import random
	import json
	import time
	import sys
	import os

except ModuleNotFoundError as e:
    print(f"[{toolname}] {e}")
    exit()

def get_file(filename):
	file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
	with open(filename) as file:
		return [i.strip() for i in file.readlines()]

def get_proxy(proxy_file, count):
    with open(proxy_file) as file:
        proxy_list = [i for i in json.load(file)["data"]]
        proxies = [random.choice(proxy_list) for _ in range(count)]

    return proxies

def refresh_proxy(file_path):
	url = "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc"
	output_file = file_path

	print(f"[{toolname}] Requesting new proxies")
	response = requests.get(url)
	data = json.loads(response.text)

	print(f"[{toolname}] Writing file")
	with open(output_file, "w") as file:
		json.dump(data, file, indent=4)

	print(f"[{toolname}] File saved to {output_file}")

def display_proxy(proxies):
    print(f"{'Protocols':<15}{'Address':<20}{'Port'}")
    for proxy in proxies:
        print(f"{' '*3}{proxy['protocols'][0]:<12}{proxy['ip']:<20}{proxy['port']}")

def path(x):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), x)

def update_package():
	command = "pip uninstall netspawn && pip install git+https://github.com/im-strange/netspawn.git"
	print(f"[{toolname}] getting latest update from https://github.com/im-strange/netspawn.git")
	print(f"[{toolname}] press enter to continue..")
	try:
		result = subprocess.run(command, shell=True, text=True, capture_output=True, check=True)
		print(f"[{toolname}] package updated successfully!")
	except Exception as e:
		print(f"[{toolname}] {e}")

# main function
def main():
	# cli info
	cli_version = "netspawn 1.0.0"

	proxy_file = path("data/proxies.json")
	email_file = path("data/emails.txt")

	# custom parser
	class CustomArgumentParser(argparse.ArgumentParser):
		def print_help(self):
			lines = [
				f"usage: spawn <type> [OPTIONS]",
				f"\ntype:",
				f"{' '*4}{'proxy':<15} spawn proxy",
				f"{' '*4}{'email':<15} spawn email",
				f"{' '*4}{'password':<15} spawn password",
				f"\narguments:",
				f"{' '*4}{'-t, --type':<15} set type of data to spawn",
				f"{' '*4}{'-c, --count':<15} number of data to spawn [default=10]",
				f"\ncommands:",
				f"{' '*4}{'-h, --help':<15} show this help message",
				f"{' '*4}{'-r, --refresh':<15} refresh list",
				f"{' '*4}{'--update':<15} update the package",
				f"\nexamples:",
				f"{' '*4}spawn --type proxy --count 10",
				f"{' '*4}spawn --refresh",
				]
			for line in lines:
				print(line)
				time.sleep(0.01)

		def error(self, message):
			print(f"[{toolname}] {message}")
			print()
			self.print_help()
			exit(2)

	parser = CustomArgumentParser()
	parser.add_argument("-t", "--type", type=str)
	parser.add_argument("-v", "--version", action="store_true")
	parser.add_argument("-r", "--refresh", action="store_true")
	parser.add_argument("-c", "--count", type=int, default=10)
	parser.add_argument("--update", action="store_true")

	args = parser.parse_args()

	if len(sys.argv) == 1:
		print(f"[{toolname}] there is no any argument given")
		print(f"[{toolname}] try 'spawn --help'")
		exit()

	if args.version:
		print(f"{cli_version}")
		exit()

	if args.type == "proxy":
		count = args.count
		proxies = get_proxy(proxy_file, count)
		display_proxy(proxies)

	if args.type == "email":
		count = args.count
		emails = random.choices(get_file(email_file), k=count)
		print(f"Emails:")
		for email in emails:
			print(f"{' '*4}{email}")

	if args.refresh:
		refresh_proxy(proxy_file)
		exit()

	if args.update:
		update_package()
		exit()

if __name__ == "__main__":
    main()
