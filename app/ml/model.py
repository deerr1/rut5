from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
from fastapi import Depends
from typing import List


def get_model():
    model = T5ForConditionalGeneration.from_pretrained('ml/rut5')
    model.train()
    return model

def get_tokenizer():
    tokenizer = T5Tokenizer.from_pretrained('ml/rut5')
    return tokenizer

# def generate(text:str, quantity:int = 1, model: T5ForConditionalGeneration = Depends(get_model), tokenizer: T5Tokenizer = Depends(get_tokenizer),  **kwargs) -> List[str]:
def generate(text:str, quantity:int = 1, **kwargs) -> List[str]:
    
    inputs = tokenizer(text, return_tensors='pt')
    with torch.no_grad():
        hypotheses = model.generate(**inputs, num_beams=20, num_return_sequences=quantity, **kwargs)
    return tokenizer.batch_decode(hypotheses, skip_special_tokens=True)


model, tokenizer = get_model(), get_tokenizer()
