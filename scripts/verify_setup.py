#!/usr/bin/env python3
"""
verify_setup.py — Run this inside the container to confirm everything works.
Usage:  python scripts/verify_setup.py
"""

import sys

print("=" * 55)
print("  ML Container Setup Verification")
print("=" * 55)

# ── Python version ────────────────────────────────────────
print(f"\n[1] Python:  {sys.version.split()[0]}")

# ── CUDA / GPU ────────────────────────────────────────────
print("\n[2] CUDA / GPU:")
try:
    import torch
    cuda_ok = torch.cuda.is_available()
    print(f"    PyTorch version : {torch.__version__}")
    print(f"    CUDA available  : {cuda_ok}")
    if cuda_ok:
        print(f"    GPU name        : {torch.cuda.get_device_name(0)}")
        print(f"    GPU count       : {torch.cuda.device_count()}")
        t = torch.tensor([1.0, 2.0]).cuda()
        print(f"    Tensor on GPU   : {t}  ✓")
    else:
        print("    ⚠️  CUDA not available — check nvidia-container-toolkit")
except ImportError:
    print("    PyTorch not installed (expected if using TF/JAX)")

# ── Matplotlib ────────────────────────────────────────────
print("\n[3] Matplotlib:")
try:
    import matplotlib
    matplotlib.use("Agg")           # non-interactive backend for this test
    import matplotlib.pyplot as plt
    import numpy as np
    fig, ax = plt.subplots()
    ax.plot(np.sin(np.linspace(0, 2 * 3.14, 100)))
    ax.set_title("Test plot")
    fig.savefig("/tmp/test_plot.png")
    print(f"    Version  : {matplotlib.__version__}")
    print(f"    Backend  : {matplotlib.get_backend()}")
    print(f"    Save test: /tmp/test_plot.png  ✓")
except Exception as e:
    print(f"    ✗ Error: {e}")

# ── OpenCV ────────────────────────────────────────────────
print("\n[4] OpenCV:")
try:
    import cv2
    import numpy as np
    img = np.zeros((100, 200, 3), dtype="uint8")
    cv2.putText(img, "OpenCV OK", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imwrite("/tmp/test_opencv.png", img)
    print(f"    Version  : {cv2.__version__}")
    print(f"    Save test: /tmp/test_opencv.png  ✓")
except Exception as e:
    print(f"    ✗ Error: {e}")

# ── NumPy / Pandas ────────────────────────────────────────
print("\n[5] Core libraries:")
try:
    import numpy as np
    import pandas as pd
    print(f"    NumPy  : {np.__version__}  ✓")
    print(f"    Pandas : {pd.__version__}  ✓")
except Exception as e:
    print(f"    ✗ {e}")

print("\n" + "=" * 55)
print("  Done. Review any ✗ items above.")
print("=" * 55 + "\n")
