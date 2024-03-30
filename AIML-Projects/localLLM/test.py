# my hugging face token
# "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"
import os 
import transformers 
from transformers import AutoModel, AutoTokenizer 

model_name = os.getenv("MODEL_NAME") 
model_config_path = os.getenv("MODEL_CONFIG")

# load the model
model = AutoModel.from_pretrained(model_name, config=model_config_path) 
tokenizer = AutoTokenizer.from_pretrained(model_name) 

# Example usage:
input_text = "Hello, world!" 
tokens = tokenizer(input_text) 
outputs = model(tokens)

# Print the outputs
print(outputs) 