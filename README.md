# Learning Hugging Face LLMs

My hands-on journey learning Large Language Models with the Hugging Face ecosystem. This repository documents real experiments, working code, and practical lessons learned while exploring LLM fine-tuning and deployment.

## What's Here

### 🚀 **Working Examples**
- **`test_llama.py`** - Interactive text generation with Meta-Llama-3-8B-Instruct
- **`fine_tune_sst2.ipynb`** - Complete BERT fine-tuning pipeline for sentiment analysis (Trainer API approach)
- **`fine_tune_mrpc.ipynb`** - Manual training loop implementation for paraphrase detection (MRPC dataset)
- **End-to-end workflows** from data loading to model testing

### 📚 **Learning Materials**
- **`fine_tuning_notes.md`** - Comparison of popular fine-tuning frameworks (SFTTrainer, Unsloth, Axolotl, TorchTune)
- **Real examples** of parameter tuning and precision management
- **Troubleshooting guides** for common training issues

### 🛠 **Practical Solutions**
- **`git_troubleshooting_summary.txt`** - Git workflows for handling large model files
- **Device management patterns** using `device_map="auto"` and `torch_dtype` configurations
- **Interactive prompting** examples following project conventions

## Key Learning Areas

### **Model Usage & Inference**
- Loading models with Hugging Face model hub identifiers
- Text generation pipelines with customizable parameters (`top_k`, `temperature`, `max_length`)
- Device-aware model deployment for CPU/GPU environments

### **Fine-Tuning Workflows**
- **Dataset handling** with `datasets` library (SST-2, MRPC, GLUE tasks)
- **Training approaches** - Trainer API vs manual PyTorch training loops
- **Training configuration** with `TrainingArguments` and `Trainer` API
- **Manual training control** - Custom loops with DataLoader, optimizer, and device management
- **Precision management** - balancing performance and stability with BF16/FP16
- **Evaluation metrics** and model checkpoint management

### **Development Patterns**
- **Interactive scripts** that prompt for user input rather than hardcoded examples
- **Parameter experimentation** with exposed configuration options
- **Efficient workflows** using dynamic padding and batched processing

## Repository Structure

```
Learning-HF-LLMS/
├── test_llama.py              # Text generation example
├── fine_tune_sst2.ipynb       # BERT sentiment classification tutorial (Trainer API)
├── fine_tune_mrpc.ipynb       # BERT paraphrase detection (Manual training loop)
├── fine_tuning_notes.md       # Framework comparison and tips
├── git_troubleshooting_summary.txt  # Git workflow solutions
└── .github/
    └── copilot-instructions.md # Project conventions and patterns
```

## Getting Started

1. **Text Generation**: Run `test_llama.py` for interactive LLM experimentation
2. **Fine-Tuning (Trainer API)**: Follow `fine_tune_sst2.ipynb` for a complete training pipeline with built-in features
3. **Fine-Tuning (Manual Loop)**: Explore `fine_tune_mrpc.ipynb` to understand low-level PyTorch training mechanics
4. **Framework Selection**: Check `fine_tuning_notes.md` for tool recommendations

## Integration Stack

- **🤗 Transformers** - Core library for model loading and training
- **📊 Datasets** - Data loading and preprocessing
- **⚡ PEFT** - Parameter-efficient fine-tuning (LoRA/QLoRA)
- **🔧 PyTorch** - Backend training framework

## Lessons Learned

- **Two training approaches**: Trainer API for production convenience vs manual loops for learning PyTorch fundamentals
- **Dataset variety**: Single sentences (SST-2) vs sentence pairs (MRPC) require different tokenization approaches
- **Precision matters**: Mixed precision conflicts can break training - use consistent dtype configurations
- **Device management**: `device_map="auto"` handles multi-GPU setups automatically vs manual `.to(device)` control
- **Git hygiene**: Always exclude model folders in `.gitignore` before committing
- **Interactive development**: Scripts work better when they prompt for user input

---

*This is a practical learning repository focused on working code and real solutions rather than theoretical best practices.*