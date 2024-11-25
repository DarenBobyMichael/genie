from openai import OpenAI

#  set your OpenAI API key 
def query(user_input):
    client = OpenAI()
    # Using GPT-4 with the ChatCompletion endpoint for a direct query
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": f"Help me to {user_input}. Be concise and to the point.",
            },
        ],
    )
    return completion.choices[0].message.content
