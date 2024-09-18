import random
import sys
import json

with open("proxies.json") as file:
	proxy_list = json.load(file)["data"]

args = sys.argv[1:]
length = int(args[0])

proxy_list = [random.choice(proxy_list) for _ in range(length)]

for dict_ in proxy_list:
	proxy = ""
	proxy += str(dict_["protocols"][0]) + " "
	proxy += str(dict_["ip"]) + " "
	proxy += str(dict_["port"])
	print(proxy)
