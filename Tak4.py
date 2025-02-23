import openai
from transformers import pipeline
import gradio as gr

# OpenAI API-based text generation
def generate_text_openai(prompt, model="gpt-3.5-turbo", max_tokens=100):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens
    )
    return response["choices"][0]["message"]["content"]

# Hugging Face GPT-2-based text generation
def generate_text_gpt2(prompt, max_length=100):
    generator = pipeline("text-generation", model="gpt2")
    result = generator(prompt, max_length=max_length, num_return_sequences=1)
    return result[0]['generated_text']

# Interactive UI using Gradio
def generate_text(prompt, model_type):
    if model_type == "OpenAI GPT-3.5":
        return generate_text_openai(prompt)
    elif model_type == "GPT-2":
        return generate_text_gpt2(prompt)
    else:
        return "Invalid model selection"

iface = gr.Interface(
    fn=generate_text,
    inputs=["text", gr.Radio(["OpenAI GPT-3.5", "GPT-2"])],
    outputs="text",
    title="AI Text Generation",
    description="Enter a prompt and select a model to generate text."
)

# Example usage
if __name__ == "__main__":
    user_prompt = "Once upon a time in a distant galaxy,"
    
    print("\n=== OpenAI GPT-3.5 Output ===")
    print(generate_text_openai(user_prompt))
    
    print("\n=== GPT-2 Output ===")
    print(generate_text_gpt2(user_prompt))
    
    iface.launch()
