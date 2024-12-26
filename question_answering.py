import groq
import os

client = groq.Groq(api_key="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")

def answer_question(question, context):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on the given context. Provide concise and accurate answers."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}\n\nAnswer:"}
        ],
        model="mixtral-8x7b-32768",
        max_tokens=200
    )
    return chat_completion.choices[0].message.content
