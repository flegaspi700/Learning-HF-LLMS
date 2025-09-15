"""
This script demonstrates how to use the Hugging Face transformers library to generate text
with the meta-llama/Meta-Llama-3-8B-Instruct model.

It initializes a tokenizer and a text-generation pipeline, then feeds the model a prompt
to generate a joke about penguins. The resulting text is then printed to the console.
"""
import transformers
import torch
from transformers import AutoTokenizer

model = "meta-llama/Meta-Llama-3-8B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model)

pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

prompt = input("Enter your prompt: ")
sequences = pipeline(
    prompt,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    truncation=True,
    max_length=400,
    temperature=0.7
)

for seq in sequences:
    print(f"Result: {seq['generated_text']}")

# --- Suggestions for Enhancement ---
#
# 1. Make it Interactive:
#    Instead of a fixed prompt, you could accept user input.
#
#    prompt = input("Enter your prompt: ")
#    sequences = pipeline(prompt, ...)
#
# 2. Experiment with Parameters:
#    - `temperature`: Lower for more predictable answers (e.g., 0.2), higher for more creative ones (e.g., 1.0).
#    - `max_length`: Increase for longer text generation.
#    - `top_k` / `top_p`: Control the sampling strategy (e.g., `top_p=0.95` for nucleus sampling).
#
# 3. Encapsulate into a Function:
#    Wrap the logic in a function for reusability.
#
#    def generate_text(prompt: str, max_len: int = 400) -> str:
#        # ... (pipeline creation and call)
#        return sequences[0]['generated_text']
#
#    if __name__ == "__main__":
#        joke = generate_text("Tell me a joke about penguins.")
#        print(joke)
#
# 4. Add Command-Line Arguments:
#    Use Python's `argparse` library to pass the prompt and parameters from the command line.
#
# 5. Stream the Output:
#    For longer generations, print text token-by-token as it's generated for a real-time effect.
#    This requires a different approach using a `TextStreamer`.