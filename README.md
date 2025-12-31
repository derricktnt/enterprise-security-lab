# enterprise-security-lab
### Runtime Configuration
This framework prompts for:
- Multiple target IPs or CIDRs
- Multiple web application URLs
- API keys (entered securely at runtime)

No sensitive data is hardcoded or stored in the repository.

## CI/CD Security Scanning

This repository includes a GitHub Actions pipeline that performs automated security checks on every push and pull request.

### CI/CD Coverage
- Static code analysis (Bandit)
- Dependency vulnerability scanning (Safety)
- Passive web application scanning (OWASP ZAP Baseline)

### Design Considerations
Active exploitation and intrusive scans are intentionally excluded from CI/CD pipelines and are performed manually in controlled environments.

Scan results are published as build artifacts for review.
