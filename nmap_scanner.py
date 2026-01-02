import nmap
import json
from datetime import datetime
from utils.config import get_targets

def run_nmap_scan(targets):
    nm = nmap.PortScanner()
    results = {
        "scan_time": str(datetime.now()),
        "targets": []
    }

    for target in targets:
        print(f"[*] Scanning {target}")
        nm.scan(target, arguments='-sS -sV -O')

        for host in nm.all_hosts():
            host_data = {
                "ip": host,
                "state": nm[host].state(),
                "services": []
            }

            for proto in nm[host].all_protocols():
                for port in nm[host][proto]:
                    service = nm[host][proto][port]
                    host_data["services"].append({
                        "port": port,
                        "protocol": proto,
                        "name": service.get("name"),
                        "product": service.get("product"),
                        "version": service.get("version")
                    })

            results["targets"].append(host_data)

    return results


if __name__ == "__main__":
    targets = get_targets()
    scan_results = run_nmap_scan(targets)

    with open("nmap_results.json", "w") as f:
        json.dump(scan_results, f, indent=4)

    print("[+] Nmap scanning completed")
