import os
from openai import OpenAI
from config import API_KEY

HISTORY_FILE = "history.txt"

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return file.read()
    return ""

def save_message(role, message):
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(f"{role.upper()}: {message}\n")

def main():
    client = OpenAI(api_key=API_KEY)

    messages = [
        {"role": "system", "content": "You are an intelligent assistant."}
    ]

    print("Welcome to ChatGPT CLI (type 'exit' to quit)")

    while True:
        message = input("You: ").strip()
        
        if message.lower() == "exit":
            print("Goodbye!")
            break

        messages.append({"role": "user", "content": message})
        save_message("user", message)

        try:
            chat = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            reply = chat['choices'][0]['message']['content']
            print(f"ChatGPT: {reply}")

            messages.append({"role": "assistant", "content": reply})
            save_message("assistant", reply)

        except Exception as e:
            print(f"[Error]: {e}")

if __name__ == "__main__":
    main()
