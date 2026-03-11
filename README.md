# Lane-Assisted Visual Odometry

> GPU-accelerated visual odometry with lane assistance, developed in a Docker-based ML environment.

---

## Project Overview

_TODO: Describe your project here — what it does, the approach, datasets used, etc._

---

## Repository Structure

```
Lane-Assisted-VO/
├── .devcontainer/              # VS Code Dev Containers config (must be at repo root)
│   └── devcontainer.json
│
├── docker/                     # Docker environment setup
│   ├── Dockerfile              # Container definition (CUDA + Python + ML stack)
│   ├── docker-compose.yml      # GPU passthrough, volumes, ports
│   └── README.md               # Full environment setup instructions
│
├── scripts/
│   └── verify_setup.py         # Verify GPU, matplotlib, OpenCV inside container
│
├── src/                        # Source code
├── notebooks/                  # Jupyter notebooks
├── data/                       # Datasets (gitignored)
├── .gitattributes
├── .gitignore
└── README.md
```

---

## Environment Setup

The development environment runs inside a Docker container with:
- CUDA 12.1 + cuDNN 8 (NVIDIA GPU acceleration)
- PyTorch pre-installed
- Matplotlib + OpenCV with GUI support via WSLg (Windows 11)
- JupyterLab on port 8888
- VS Code Dev Containers integration

### Prerequisites
- Windows 11
- NVIDIA GPU with up-to-date drivers
- Docker Desktop (WSL2 backend)
- VS Code + Dev Containers extension
- NVIDIA Container Toolkit installed in WSL

> Full step-by-step setup instructions: [docker/README.md](docker/README.md)

### First Time Setup

```bash
git clone git@github.com:nazrulnazeer/Lane-Assisted-VO.git
cd Lane-Assisted-VO/docker
docker compose up --build
```

First build takes ~15 minutes (downloads CUDA base image). Subsequent starts take seconds.

Once built, open the repo root folder in VS Code → `Ctrl+Shift+P` → **"Dev Containers: Reopen in Container"**.

### Verify Everything Works

Inside the VS Code terminal (now inside the container):
```bash
python scripts/verify_setup.py
```

---

## Daily Workflow

### Starting work
```bash
# 1. Start the container
cd A:\projects\Lane-Assisted-VO\docker
docker compose up -d

# 2. Open VS Code — click "Reopen in Container" popup (bottom right)
#    or: Ctrl+Shift+P → "Dev Containers: Reopen in Container"
```

### Stopping work
```bash
cd A:\projects\Lane-Assisted-VO\docker
docker compose down
```

Your code lives on your Windows filesystem and is only mounted into the container — stopping or deleting the container never affects your files.

---

## Usage

_TODO: Add usage instructions, example commands, how to run notebooks, etc._

---

## Results

_TODO: Add results, metrics, visualizations._

---

## License

_TODO: Add license._
