#!/bin/bash
# ============================================================
# Memwyre Compose-Up Wrapper
# Prunes dead containers/networks then starts services.
# Usage: bash scripts/compose-up.sh [extra docker compose args]
# ============================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$ROOT_DIR"

echo "=== Pruning stopped containers ==="
docker container prune -f

echo "=== Pruning unused networks ==="
docker network prune -f

echo "=== Pruning unused images ==="
docker image prune -f

echo "=== Starting services ==="
docker compose up -d --remove-orphans "$@"

echo "=== Done! Services are up. ==="
docker compose ps
