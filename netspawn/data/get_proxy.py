import requests
import json

def get_proxy():
	url = "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc"
	output_file = "proxies.json"

	print(f"[+] Sending requests")
	response = requests.get(url)
	data = json.loads(response.text)

	print(f"[+] Writing file")
	with open(output_file, "w") as file:
		json.dump(data, file, indent=4)

	print(f"[+] File saved to {output_file}")

if __name__ == "__main__":
	get_proxy()

