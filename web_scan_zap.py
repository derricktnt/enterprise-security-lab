from zapv2 import ZAPv2
import time
import json
from utils.config import get_targets, get_api_key

def run_zap_scan(targets, api_key):
    zap = ZAPv2(apikey=api_key)

    all_alerts = []

    for target in targets:
        print(f"[*] Scanning web target {target}")
        zap.urlopen(target)
        time.sleep(2)

        scan_id = zap.ascan.scan(target)
        while int(zap.ascan.status(scan_id)) < 100:
            time.sleep(5)

        alerts = zap.core.alerts(baseurl=target)
        all_alerts.extend(alerts)

    with open("zap_alerts.json", "w") as f:
        json.dump(all_alerts, f, indent=4)

    print("[+] ZAP scanning completed")


if __name__ == "__main__":
    targets = get_targets()
    api_key = get_api_key("OWASP ZAP")
    run_zap_scan(targets, api_key)
