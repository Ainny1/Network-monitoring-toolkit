# AWS private monitoring lab — deployment preparation

**Status: Infrastructure template only. Not deployed.** Creating this CloudFormation stack incurs AWS charges (EC2, EBS, network transfer, and possibly public IPv4/NAT). Do not deploy until the account owner reviews costs, selects a region/VPC/subnet, enables MFA, and configures an AWS Budget. This is not covered by GitHub Actions free compute.

## Security design

- No inbound security-group rules: Grafana (3000), Prometheus (9090), and SSH (22) are **not internet-accessible**.
- The instance receives the `AmazonSSMManagedInstanceCore` role to support Session Manager when SSM connectivity is available.
- The template requires a subnet with outbound connectivity for updates; in a public subnet, an automatically assigned public IPv4 address may incur a charge even though no inbound traffic is allowed. A private subnet may require NAT or SSM VPC endpoints, also billable.
- The EBS volume is encrypted. No application passwords are stored in CloudFormation parameters, user data, or GitHub.
- The template does **not** install software or start services automatically. This avoids silently running a public or default-password dashboard.

## When you have AWS access and explicitly approve charges

1. Verify AWS region and account, create a monthly AWS Budget, and enable MFA.
2. In CloudFormation, upload `aws/private-monitoring.yaml`, select a VPC and an internet-capable subnet, and acknowledge IAM resource creation.
3. Review the **Change set and estimated charges** before creating the stack.
4. In AWS Systems Manager, confirm the EC2 instance appears as a managed node and start a Session Manager shell. If it doesn't appear, troubleshoot IAM, SSM Agent, and outbound connectivity; **do not open SSH publicly as a workaround**.
5. In the SSM shell, install Docker Engine and the Docker Compose plugin following the vendor's current Ubuntu instructions, then clone the repository. Do not run curl-piped scripts.
6. In the repository directory, create `.env` with `GRAFANA_ADMIN_PASSWORD=<strong unique password>`; restrict file permissions with `chmod 600 .env`.
7. Run `docker compose config`, then `docker compose up -d`, and check `docker compose ps` and logs.
8. For remote viewing, use **SSM port forwarding** to the instance for ports 3000 and 9090. This requires AWS CLI and Session Manager plugin on the viewer's device. Do not change Docker bindings from `127.0.0.1` or add public ingress.
9. Query `up{job="prometheus"}` and confirm it equals 1. Open Grafana, confirm real samples, and only then capture a redacted screenshot.

## Stop costs

Stop the instance when not needed (EBS charges continue), or delete the CloudFormation stack to terminate the instance and stack-managed volume. Review remaining snapshots, public IPv4 charges, and other resources separately.

## Limits

The provided dashboard monitors Prometheus itself. It is **not** yet network-wide monitoring. Zabbix and Nagios are not deployed. A generated dashboard illustration is not proof of a working deployment.
