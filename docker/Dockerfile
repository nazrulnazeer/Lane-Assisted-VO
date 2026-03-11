# ─────────────────────────────────────────────────────────────────────────────
# Base: CUDA 12.1 + cuDNN 8 + Ubuntu 22.04
# ─────────────────────────────────────────────────────────────────────────────
FROM nvidia/cuda:12.1.1-cudnn8-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC
ENV DISPLAY=:0
ENV LIBGL_ALWAYS_INDIRECT=0

# ── System packages ───────────────────────────────────────────────────────────
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.11 python3.11-dev python3-pip python3.11-venv \
    build-essential cmake git curl wget unzip \
    libglib2.0-0 libsm6 libxext6 libxrender-dev libgl1-mesa-glx libglib2.0-dev \
    libgtk-3-dev python3-tk \
    vim htop \
    && rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1 \
 && update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1 \
 && update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

RUN pip install --upgrade pip setuptools wheel

# ── PyTorch with CUDA 12.1 (separate command — needs its own --index-url) ─────
RUN pip install --no-cache-dir \
    torch torchvision torchaudio \
    --index-url https://download.pytorch.org/whl/cu121

# ── Uncomment below to use TensorFlow instead of PyTorch ─────────────────────
# RUN pip install --no-cache-dir tensorflow[and-cuda]

# ── Uncomment below to use JAX instead of PyTorch ────────────────────────────
# RUN pip install --no-cache-dir jax[cuda12_pip] \
#     -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html

# ── All other Python packages ─────────────────────────────────────────────────
RUN pip install --no-cache-dir \
    numpy pandas scikit-learn scipy \
    matplotlib seaborn plotly \
    opencv-python Pillow \
    jupyterlab ipywidgets \
    tqdm pyyaml python-dotenv

# ── Working directory points to repo root (mounted via compose) ───────────────
WORKDIR /workspace

CMD ["/bin/bash"]
