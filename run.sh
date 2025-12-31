#!/bin/bash

echo "[*] Enterprise Security Assessment"

python3 scanner/nmap_scanner.py
python3 scanner/web_scan_zap.py
python3 exploitation/metasploit_runner.py
python3 reports/report_generator.py

echo "[+] Assessment completed"
