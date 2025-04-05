import requests

def download_link(url, output_path):
    try:
        r = requests.get(url, timeout=30)
        if r.ok:
            with open(output_path, 'wb') as f:
                f.write(r.content)
            return True
    except:
        pass
    return False