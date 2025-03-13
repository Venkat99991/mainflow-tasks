import re
from collections import Counter

def parse_log(file_path):
    ip_counter = Counter()
    url_counter = Counter()
    response_code_counter = Counter()

    with open(file_path, 'r') as log_file:
        for line in log_file:
            try:
                # Example log line format: "IP - - [timestamp] 'METHOD URL PROTOCOL' RESPONSE_CODE SIZE"
                match = re.match(r'(\d+\.\d+\.\d+\.\d+).*"(\w+)\s(\S+)\s.*"\s(\d+)', line)
                if match:
                    ip, method, url, response_code = match.groups()
                    ip_counter[ip] += 1
                    url_counter[url] += 1
                    response_code_counter[response_code] += 1
            except Exception as e:
                print(f"Error parsing line: {line.strip()} - {e}")

    return ip_counter, url_counter, response_code_counter

def display_results(ip_counter, url_counter, response_code_counter):
    print("\nMost Frequent IP Addresses:")
    for ip, count in ip_counter.most_common(5):
        print(f"{ip}: {count} times")

    print("\nMost Accessed URLs:")
    for url, count in url_counter.most_common(5):
        print(f"{url}: {count} times")

    print("\nResponse Code Counts:")
    for code, count in response_code_counter.most_common():
        print(f"{code}: {count} times")

# Example usage
log_file_path = "access.log"  # Replace with the actual path of your log file
ip_counter, url_counter, response_code_counter = parse_log(log_file_path)
display_results(ip_counter, url_counter, response_code_counter)
