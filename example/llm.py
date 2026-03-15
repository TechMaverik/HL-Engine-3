from HL_Engine_LLM import LargeLanguageModelEngine as llm
from configurations import *
question=input("Enter the question to ask llm...\n")
ans=llm().ask(question,AI_PROMPTS,"mattbot",OLLAMA_URL)
print(ans)