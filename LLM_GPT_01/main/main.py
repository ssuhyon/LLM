import openai
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

# API 키 가져오기
api_key = os.getenv("OPEN_API_KEY")
client = openai.Client(api_key=api_key)

prompt = "You are very kind person."
messages = [{"role": "system", "content": prompt}]

while True:
    user_input = input("User : ")
    if user_input.lower() == "exit":
        print("대화를 종료합니다.")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    assistant_reply = response.choices[0].message.content
    print(f"GPT: {assistant_reply}\n")

    messages.append({"role": "assistant", "content": assistant_reply})
