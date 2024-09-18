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
    import argparse
    import requests
    import random
    import json
    import time
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

def display_proxy(proxies):
    print(f"{'Protocols':<15}{'Address':<20}{'Port'}")
    for proxy in proxies:
        print(f"{' '*3}{proxy['protocols'][0]:<12}{proxy['ip']:<20}{proxy['port']}")

def path(x):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), x)

def refresh_proxy():
    pass

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
				f"\ncommands:",
				f"{' '*4}{'--count':<15} number of data to spawn",
				f"{' '*4}{'--help':<15} show this help message",
				f"{' '*4}{'--refresh':<15} refresh list",
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
	parser.add_argument("type", type=str)
	parser.add_argument("--version", action="store_true")
	parser.add_argument("--count", type=int, default=10)

	args = parser.parse_args()

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
		for index, email in enumerate(emails, start=1):
			print(f"{' '*4}{index:<5}{email}")


if __name__ == "__main__":
    main()
