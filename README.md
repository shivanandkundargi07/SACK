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

```

## 🔧 Example Scripts

We provide example bash scripts for running SACK with different continual learning methods.

### Example: Run SACK with iCaRL

```bash
bash scripts/icarl.sh

```


## 🙏 Acknowledgements

This repository builds upon the excellent [Mammoth](https://github.com/aimagelab/mammoth) continual learning framework by AIMAGELAB. We thank the authors for providing a well-structured and extensible codebase that facilitated rapid integration and benchmarking of our method.

If you find this repository useful, please consider also citing the original Mammoth paper:

```bibtex
@inproceedings{maracani2023mammoth,
  title={Mammoth: A Flexible and Modular Framework for Continual Learning},
  author={Maracani, Andrea and Buzzega, Pietro and Boschini, Matteo and Calderara, Simone},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
  year={2023}
}

```
