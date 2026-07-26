#!/bin/bash
# ============================================================
# Memwyre EC2 Bootstrap Script
# Run once on a fresh Ubuntu 22.04 EC2 instance:
#   chmod +x ec2-setup.sh && sudo ./ec2-setup.sh
# ============================================================
set -e

echo "=== Installing Docker ==="
apt-get update
apt-get install -y ca-certificates curl gnupg
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
chmod a+r /etc/apt/keyrings/docker.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

apt-get update
apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Add ubuntu user to docker group
usermod -aG docker ubuntu

echo "=== Creating app directory ==="
mkdir -p /opt/memwyre
chown ubuntu:ubuntu /opt/memwyre

echo "=== Installing AWS CLI ==="
apt-get install -y awscli

echo "=== Setting up Let's Encrypt options ==="
mkdir -p /opt/memwyre/certbot/conf
curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/_internal/tls_configs/options-ssl-nginx.conf > /opt/memwyre/certbot/conf/options-ssl-nginx.conf
curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot/certbot/ssl-dhparams.pem > /opt/memwyre/certbot/conf/ssl-dhparams.pem

echo "=== Done! ==="
echo ""
echo "Next steps:"
echo "1. Log out and back in (for docker group)"
echo "2. Configure AWS CLI:  aws configure"
echo "3. Copy .env.prod to /opt/memwyre/.env.prod"
echo "4. Copy docker-compose.prod.yml to /opt/memwyre/"
echo "5. Login to ECR:  aws ecr get-login-password | docker login --username AWS --password-stdin <ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com"
echo "6. Initialize certificates: cd /opt/memwyre && chmod +x deploy/init-letsencrypt.sh && ./deploy/init-letsencrypt.sh"
echo "7. Deploy:  cd /opt/memwyre && bash scripts/compose-up.sh -f docker-compose.prod.yml"
