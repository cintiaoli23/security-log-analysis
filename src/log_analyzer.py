from collections import defaultdict

log_file = "../logs/auth.log"
failed_attempts = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split()
            ip_address = parts[-1]
            failed_attempts[ip_address] += 1

print("Suspicious IPs (3 or more failed attempts):")
for ip, count in failed_attempts.items():
    if count >= 3:
        print(f"{ip} - {count} failed attempts")