from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch

def get_model():
    model = T5ForConditionalGeneration.from_pretrained('rut5')
    model.train()
    return model

def get_tokenizer():
    tokenizer = T5Tokenizer.from_pretrained('rut5')
    return tokenizer

def generate(text, **kwargs):
    inputs = tokenizer(text, return_tensors='pt')
    with torch.no_grad():
        hypotheses = model.generate(**inputs, num_beams=5, **kwargs)
    return tokenizer.decode(hypotheses[0], skip_special_tokens=True)


model, tokenizer = get_model(), get_tokenizer()