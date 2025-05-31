import os
import subprocess
import sys
from datetime import datetime

# Ensure a target domain is provided
if len(sys.argv) < 2:
    print("Usage: python3 auto_recon.py <target_domain>")
    sys.exit(1)

# Target domain
target = sys.argv[1]

# Create output directory
output_dir = f"recon_{target}"
os.makedirs(output_dir, exist_ok=True)

# Run Google Dorks (manual list)
print("[+] Running Google Dorks (manual review required)...")
google_dorks = f"site:{target} inurl:admin"
google_dorks += f"\nsite:{target} intitle:index.of"
google_dorks += f"\nsite:{target} ext:php | ext:asp | ext:aspx | ext:jsp"
google_dorks += f"\nsite:{target} intext:password"
with open(os.path.join(output_dir, "google_dorks.txt"), "w") as f:
    f.write(google_dorks)

# WHOIS Lookup
print("[+] Running WHOIS lookup...")
with open(os.path.join(output_dir, "whois.txt"), "w") as f:
    subprocess.run(["whois", target], stdout=f, stderr=subprocess.DEVNULL)

# DNS Records (nslookup)
print("[+] Running DNS lookup...")
with open(os.path.join(output_dir, "dns_records.txt"), "w") as f:
    subprocess.run(["nslookup", target], stdout=f, stderr=subprocess.DEVNULL)

# Traceroute
print("[+] Running traceroute...")
with open(os.path.join(output_dir, "traceroute.txt"), "w") as f:
    subprocess.run(["traceroute", target], stdout=f, stderr=subprocess.DEVNULL)

# theHarvester (requires installation)
print("[+] Running theHarvester...")
with open(os.path.join(output_dir, "theharvester.txt"), "w") as f:
    subprocess.run(["theHarvester", "-d", target, "-b", "all"], stdout=f, stderr=subprocess.DEVNULL)

# Sherlock (if available)
print("[+] (Optional) Running Sherlock... (manual installation required)")
with open(os.path.join(output_dir, "sherlock.txt"), "w") as f:
    f.write("Run: python3 sherlock.py <name> to gather social info (manual)")

# DNSdumpster (manual)
print("[+] Adding note for DNSdumpster...")
with open(os.path.join(output_dir, "dnsdumpster_note.txt"), "w") as f:
    f.write("Visit https://dnsdumpster.com and perform manual recon for: " + target)

print(f"[✔] Recon complete. Results saved in: {output_dir}")
