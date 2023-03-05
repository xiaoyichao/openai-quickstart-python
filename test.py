# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import os
import requests

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

# print(response)
print(response['choices'][0]['message']['content'])

# import openai
# openai.api_key = "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"

# prompt = "Hello, how are you?"
# response = openai.Completion.create(
#     engine="gpt-3.5-turbo",
#     prompt=prompt,
#     max_tokens=50,
#     n=1,
#     stop=None,
#     temperature=0.5,
# )

# print(response.choices[0].text)


