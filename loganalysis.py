import re
from collections import defaultdict

def analyze_logs(logfile):
    ip_counts = defaultdict(int)
    with open(logfile, 'r') as file:
        for line in file:
            match = re.search(r'Failed password for (\S+) from (\S+)', line)
            if match:
                user, ip = match.groups()
                ip_counts[ip] += 1
    for ip, count in ip_counts.items():
        if count > 5:  # arbitrary threshold
            print(f'Suspicious activity detected from IP {ip}: {count} failed login attempts')

analyze_logs('auth.log')
