# Lane-Assisted Visual Odometry

> GPU-accelerated visual odometry with lane assistance, developed in a Docker-based ML environment.

---

## Project Overview

_TODO: Describe your project here — what it does, the approach, datasets used, etc._

---

## Repository Structure

```
Lane-Assisted-VO/
├── docker/                     # Docker environment setup
│   ├── Dockerfile              # Container definition (CUDA + Python + ML stack)
│   ├── docker-compose.yml      # GPU passthrough, volumes, ports
│   └── .devcontainer/
│       └── devcontainer.json   # VS Code Dev Containers config
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

### Quick Start

```bash
git clone git@github.com:nazrulnazeer/Lane-Assisted-VO.git
cd Lane-Assisted-VO/docker
docker compose up --build
```

Then in VS Code: `Ctrl+Shift+P` → `Dev Containers: Open Folder in Container`

---

## Usage

_TODO: Add usage instructions, example commands, how to run notebooks, etc._

---

## Results

_TODO: Add results, metrics, visualizations._

---

## License

_TODO: Add license._
