import os
from dotenv import load_dotenv
from openai import OpenAI

# .env 파일 로드
load_dotenv()

# 환경 변수에서 API 키 가져오기
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

# OpenAI API 호출
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "제주도는 어떤 곳이야?"}
    ]
)

# 응답 출력
print(response.choices[0].message.content)