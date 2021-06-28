from transformers import T5Tokenizer
from transformers import TFAutoModelForCausalLM


class Rinna():

    def __init__(self, top_p=0.95, top_k=50):
        self.top_p = top_p
        self.top_k = top_k

    def load(self):
        self.model = TFAutoModelForCausalLM.from_pretrained("rinna/japanese-gpt2-medium")
        self.tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-medium")

    def generate(self, input_tensor, output_size):
        output_tensors = self.model.generate(
            input_ids=input_tensor,
            max_length=int(output_size),
            top_p=self.top_p,
            top_k=self.top_k,
            do_sample=True,
            early_stopping=True,
            bos_token_id=self.tokenizer.bos_token_id,
            eos_token_id=self.tokenizer.eos_token_id,
            pad_token_id=self.tokenizer.pad_token_id,
            num_return_sequences=1
            )
        return output_tensors

    def tokenize(self, data):
        input_tensor = self.tokenizer(data, return_tensors="tf")["input_ids"]
        return input_tensor

    def decode(self, output_tensors):
        text = self.tokenizer.decode(output_tensors.numpy()[0])
        return text
