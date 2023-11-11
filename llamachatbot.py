from llama_cpp import Llama
from IPython.display import display, HTML
import json
import time
import pathlib


LLM = Llama(model_path="./WizardLM-7B-uncensored.ggmlv3.q2_K.bin", n_ctx=2048)


prompt = "Q: when was your dataset updated A:"


output = LLM(prompt, max_tokens=0)


print(output["choices"][0]["text"])
