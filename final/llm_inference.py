from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def load_llm(model_id="Qwen/Qwen1.5-0.5B", device="cpu"):
    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True).to(device)
    return tokenizer, model

def generate_answer(tokenizer, model, prompt, device="cpu", max_tokens=150):
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            temperature=0.7,
            top_p=0.85,
            do_sample=True,
            repetition_penalty=1.1,
            eos_token_id=tokenizer.eos_token_id
        )
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    
    if "Answer:" in answer:
        answer = answer.split("Answer:")[-1].strip()
    return answer
