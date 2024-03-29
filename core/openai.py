from core import DISCORD_BOT
from openai import OpenAI

ai = OpenAI(api_key=DISCORD_BOT['CHATGPT_API_KEY'])

def chatgpt_response(messages:list):
    response = ai.chat.completions.create(
        model='gpt-3.5-turbo-1106',
        messages=messages,
        temperature=1,
        max_tokens=2000
    )

    if response:
        content_response =  response.choices[0].message.content

    return content_response
