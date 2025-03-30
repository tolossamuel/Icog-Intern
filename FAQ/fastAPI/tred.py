from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

response  = client.chat.completions.create(
  model="deepseek/deepseek-v3-base:free",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)


print(response.choices[0].message.content)