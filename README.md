# Automated Footprinting and Reconnaissance Toolkit

This project automates the ethical hacking reconnaissance phase for a target domain. It uses tools like Google Dorks, WHOIS, nslookup, traceroute, and theHarvester to gather intelligence.

## 🛠 Tools Used

- Google Dorking
- WHOIS Lookup
- DNS Records (nslookup)
- Traceroute
- theHarvester
- Sherlock (optional)
- Manual note for DNSdumpster

## 🔧 How to Run

```bash
python3 auto_recon.py
```

Results will be saved in a folder named `recon_<target_domain>`.

**Note**: Run this in a Kali Linux / Parrot OS terminal for best compatibility.

## 📁 Output Files

- `google_dorks.txt`
- `whois.txt`
- `dns_records.txt`
- `traceroute.txt`
- `theharvester.txt`
- `sherlock.txt` *(optional)*
- `dnsdumpster_note.txt`