#!/usr/bin/env python3

import getpass

def get_targets():
    print("[*] Enter target IPs or CIDRs (comma-separated)")
    targets = input("Targets: ").strip()
    return [t.strip() for t in targets.split(",") if t.strip()]


def get_api_key(service_name):
    print(f"[*] Enter API key for {service_name}")
    return getpass.getpass("API Key (hidden): ")
