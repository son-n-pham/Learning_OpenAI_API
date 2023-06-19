import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

messages = []
while True:
    try:
        user_input = input("You: ")
        messages.append({"role": "user", "content": user_input})
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages)

        bot_answer = res.choices[0].message.content
        print(f"Bot: {bot_answer}\n")

        messages.append({"role": "assistant", "content": bot_answer})
        # print(f"ALL MESSAGES: {messages}\n")
        # print(res)

    except KeyboardInterrupt:
        print("\nExiting...")
        break
