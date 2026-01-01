# CKAN on Azure VM – Infrastructure Runbook (Dev / QA / Prod)

This repository documents how CKAN was deployed on a single Azure VM using Docker Compose, with three isolated environments: **dev**, **qa**, and **prod**.

This is an **infrastructure runbook** so that I (or a teammate) can come back later and immediately understand:
- what VM is used
- how to connect
- how CKAN is running
- how to start/stop/rebuild each environment

---

## Azure VM Information

- **Resource Group:** IRIU1  
- **VM Name:** PDCA  
- **Location:** Canada Central  
- **OS:** Ubuntu 24.04 LTS  
- **VM Size:** Standard E4ads v6 (4 vCPU, 32 GB RAM)  
- **Public IP:** `4.239.251.68`  

---

## How to Connect to the VM (SSH)

Using Azure Cloud Shell or a local terminal:

```bash
ssh -i ~/.ssh/fara-pdca-ssh.pem fara@4.239.251.68
```

Notes:
- SSH key permissions must be `600`
- VM must be **Started** (not deallocated)

---

## Installed Technologies

- Git
- Docker
- Docker Compose
- CKAN (via `ckan/ckan-docker`)
- PostgreSQL
- Solr
- Redis
- Nginx (HTTPS reverse proxy)

All services run inside Docker containers.

---

## Environment Structure

Each environment is isolated and stored in its own folder:

```text
/opt/ckan/dev
/opt/ckan/qa
/opt/ckan/prod
```

Important rule:

> **Folder = Environment**

All `docker-compose` commands must be run from the correct folder.

---

## Public Access URLs

| Environment | URL |
|------------|-----|
| Dev | https://4.239.251.68:8443 |
| QA | https://4.239.251.68:9443 |
| Prod | https://4.239.251.68:10443 |

Notes:
- HTTPS uses a self-signed certificate
- Browser warning is expected

---

## Daily Commands (Most Used)

### Check environment status
```bash
cd /opt/ckan/dev
docker-compose ps
```

### Start an environment
```bash
cd /opt/ckan/dev
docker-compose up -d
```

### Stop an environment (safe)
```bash
docker-compose down
```

### Rebuild containers (only if configs or images changed)
```bash
docker-compose up -d --build
```

⚠️ **Never run** `docker-compose down -v` in QA or PROD  
(this deletes all data).

---

## Ports & Networking

- Each environment uses a **unique HTTPS port**
- Azure Network Security Group (NSG) allows:
  - SSH: 22
  - HTTPS ports for Dev / QA / Prod

If you see a `port is already allocated` error, two environments are trying to use the same host port.

---

## CKAN Admin Access

Each environment has its own CKAN sysadmin user.

Admin credentials are defined via environment variables in `.env` files.

**Do NOT commit real passwords to GitHub.**  
Store credentials in a password manager.

---

## Persistence & Data

- Docker volumes are used for:
  - PostgreSQL data
  - CKAN file storage
  - Solr indexes
- Data survives container restarts

---

## Logs & Troubleshooting

### View logs
```bash
docker-compose logs -f --tail=200 nginx
docker-compose logs -f --tail=200 ckan
```

### Check listening ports
```bash
sudo ss -ltnp | egrep ':(8443|9443|10443)\b' || true
```

---

## Key Reminders

- Dev, QA, and Prod are fully isolated
- Changes in Dev do **not** affect QA or Prod
- Production should be changed last and carefully
- Most team members only need CKAN UI access, not SSH

---
