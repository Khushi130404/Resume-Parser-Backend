# from llama_cpp import Llama
# import os

# llm = Llama(
#     model_path="./models/mistral-7b-instruct.Q4_K_M.gguf",
#     n_ctx=2048,
#     n_threads=8  
# )

# def ask_local_llm(prompt: str) -> str:
#     response = llm(
#         prompt=f"[INST] {prompt} [/INST]",
#         max_tokens=1024,
#         temperature=0.2,
#         stop=["</s>"],
#     )
#     return response['choices'][0]['text'].strip()
