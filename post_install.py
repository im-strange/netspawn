import requests
import json
import os

def path(x):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), x)

def get_commit_info():
    url = f'https://api.github.com/repos/im-strange/netspawn/branches/main'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data

    return None

def save_commit_info(file_path, data):
	with open(file_path, 'w') as f:		
	    json.dump(data, f, indent=4)

if __name__ == "__main__":
    info = get_commit_info()
    if sha:
    	filename = "netspawn/data/netspawn-commit-info.json"
    	file_path = path(filename)
        save_commit_info(file_path, info)
        print(f"[netspawn] commit info saved to {file_path}")
    else:
        print("[netspawn] commit info failed to save")