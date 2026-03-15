import requests


class LargeLanguageModelEngine():   
    
    def ask(self,question:str,system_prompt:str,model_name:str,url:str):
        messages = [
        {"role": "system", "content": system_prompt}
        ]

        messages.append({"role": "user", "content": question})

        payload = {
            "model": model_name,
            "messages": messages,
            "stream": False
        }

        r = requests.post(url, json=payload)
        reply = r.json()["message"]["content"]

        messages.append({"role": "assistant", "content": reply})
        return reply


    