# Copilot Instructions for Learning-HF-LLMS

## Project Overview
This repository explores fine-tuning and using Large Language Models (LLMs) with Hugging Face tools. It includes scripts, notes, and troubleshooting guides for working with models like Meta-Llama-3-8B-Instruct.

## Key Components
- `test_llama.py`: Example script for text generation using Hugging Face transformers and Meta-Llama-3-8B-Instruct.
- `fine_tuning_notes.md`: Comparison and usage notes for popular LLM fine-tuning frameworks (SFTTrainer, Unsloth, Axolotl, TorchTune).
- `git_troubleshooting_summary.txt`: Practical Git troubleshooting steps, especially for handling large files and `.gitignore` usage.

## Developer Workflows
- **Text Generation**: Run `test_llama.py` to interactively generate text with a selected LLM. The script uses `transformers.pipeline` and prompts for user input.
- **Fine-Tuning**: Reference `fine_tuning_notes.md` for tool selection and configuration tips. Most workflows use Hugging Face's `transformers` and `datasets` libraries, with optional support for LoRA/QLoRA via `peft`.
- **Git Hygiene**: Always update `.gitignore` to exclude large model folders and virtual environments. See `git_troubleshooting_summary.txt` for recovery steps if large files are accidentally committed.

## Patterns & Conventions
- **Model Selection**: Models are referenced by their Hugging Face repo string (e.g., `meta-llama/Meta-Llama-3-8B-Instruct`).
- **Device Management**: Scripts use `device_map="auto"` and `torch_dtype=torch.float16` for efficient GPU usage.
- **Prompting**: Interactive scripts prompt for user input rather than using hardcoded prompts.
- **Parameter Tuning**: Example scripts expose parameters like `top_k`, `max_length`, and `temperature` for experimentation.
- **Notes & Documentation**: Markdown files provide practical, experience-based guidance rather than aspirational best practices.

## Integration Points
- **Hugging Face Transformers**: Core library for model loading and inference.
- **Datasets**: Used for loading and preparing data for training/fine-tuning.
- **PEFT**: For parameter-efficient fine-tuning (see `fine_tuning_notes.md`).

## Example: Text Generation Script
```python
from transformers import AutoTokenizer, pipeline
import torch
model = "meta-llama/Meta-Llama-3-8B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = pipeline("text-generation", model=model, torch_dtype=torch.float16, device_map="auto")
prompt = input("Enter your prompt: ")
sequences = pipeline(prompt, do_sample=True, top_k=10, num_return_sequences=1, eos_token_id=tokenizer.eos_token_id, truncation=True, max_length=400, temperature=0.7)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")
```

## Troubleshooting
- If you encounter issues with Git, refer to `git_troubleshooting_summary.txt` for step-by-step solutions.
- For model or library errors, check that your environment matches the requirements of the selected tool (see notes in markdown files).

---
**Feedback:** If any section is unclear or missing, please specify which workflows, conventions, or integration points need more detail.
