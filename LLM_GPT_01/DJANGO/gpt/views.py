import openai
from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatMessage
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# OpenAI 클라이언트 생성
client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))

def chat_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')

        if not user_message:
            return JsonResponse({"response": "메시지를 입력해주세요."})

        # 사용자 메시지 저장
        ChatMessage.objects.create(role="user", content=user_message)

        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
        
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            # 올바른 응답 처리
            assistant_message = response.choices[0].message.content.strip()

        except openai.OpenAIError as e:
            print(f"Error during OpenAI API call: {e}")
            return JsonResponse({"response": "OpenAI API 호출 중 오류가 발생했습니다."})

        # GPT 응답 저장
        ChatMessage.objects.create(role="assistant", content=assistant_message)

        return JsonResponse({"response": assistant_message})

    return render(request, "chat/chat.html")