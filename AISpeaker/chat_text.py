import openai
import os

# OpenAI API 키 설정
openai.api_key = "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"

while True:
    prompt = input("질문을 입력하세요: ")
    if prompt == "나가":
        break
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=60
    )
    print(response.choices[0].text.strip())