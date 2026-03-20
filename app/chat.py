from app.llm import openai_client, get_system_promot_content

WINDOW_SIZE = 4


def get_windowed_messages(messages):
    return [messages[0]] + messages[-WINDOW_SIZE:]


def chat(messages):
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=500,
        messages=messages,
    )
    return response.choices[0].message.content


def main():
    system_prompt = get_system_promot_content("app/prompts/system_prompt.md")
    messages = [{"role": "system", "content": system_prompt}]

    print(f"Hotel Assistant - Sliding Window ({WINDOW_SIZE} messages)")
    print("Type 'exit' to quit")
    print("-" * 40)

    while True:
        user_input = input("\nYou: ").strip()
        if not user_input:
            continue
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})
        windowed = get_windowed_messages(messages)
        reply = chat(windowed)
        messages.append({"role": "assistant", "content": reply})
        print(f"\nAssistant: {reply}")


if __name__ == "__main__":
    main()