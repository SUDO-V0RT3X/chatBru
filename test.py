import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 2,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="You are a South African person who knows everything. Explain things simply when asked , and keep your responses brief. Be funny in your responses and always use South African slang, even when displaying errors. Use emojis in your responses to be more relateable. Your name is chatBru. \n",
)

history = []

print("\nAwe howzit! Ek se I'm chatBru what can I help you with today? (Exit by  typing \"exit\")\n")


while True:
    user_input = input("You: ")

    chat_session = model.start_chat(
        history=history
    )

    if user_input == "exit":
        break

    response = chat_session.send_message(user_input)

    model_response = response.text

    print("chatBru: ", model_response)
    print()

    history.append({"role":"user", "parts": [user_input]})
    history.append({"role":"model", "parts": [model_response]})


print("Shot bru! Check you next time amphetu.")
print()