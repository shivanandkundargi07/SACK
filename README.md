# SACK: Sequentially Acquiring Concepts to Guide Continual Learning

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**SACK** is a plugin-compatible continual learning method that leverages concept relevance to guide training across experiences. It integrates concept-based reasoning into the continual learning pipeline, enabling improved generalization, interpretability, and stability-plasticity balance.

---

## 🚀 Features

- **Plugin-Compatible**: SACK is applicable to **all continual learning methods implemented in the [Mammoth](https://github.com/aimagelab/mammoth) framework**, including ER, DER++, GDumb, CoPE, AR1, and more
- **Concept-Aware Sampling**: Uses zero-shot concept extractors (e.g., CLIP, GPT-4o) to assign semantic importance to training samples
- **Flexible CL Support**: Works across class-incremental, task-incremental, and long-tail scenarios
- **Stability-Plasticity Tradeoff**: Reduces catastrophic forgetting while promoting meaningful knowledge integration
- **Lightweight & Modular**: Implemented as a drop-in sampling module using PyTorch's `WeightedRandomSampler`, with minimal changes to existing training loops

---




## 📦 Installation

```bash
git clone https://github.com/<your-username>/sack-cl.git
cd sack-cl
pip install -r requirements.txt

> 📁 **Important**: Before running any experiments, please update `paths.py` with your local directory paths for datasets, logs, and saved models.

Edit the following fields in `paths.py`:

```python
# paths.py

# Path to your dataset root directory
DATA_ROOT = "/your/local/path/to/datasets"

# Path to store training logs
LOG_DIR = "/your/local/path/to/logs"

# Path to save model checkpoints
MODEL_DIR = "/your/local/path/to/models"
