from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

openai_key = os.getenv('OPENAI_KEY')
openai_client = OpenAI(
	#defaults to os.environ.get("OPENAI_API_KEY")
	api_key=openai_key,
)
def call_ai(prompt: str):
	chat_completion = openai_client.chat.completions.create(
		messages=[
			{
				"role": "user",
				"content": prompt,
			}
		],
		model="gpt-4-1106-preview",
	)
	return (str(chat_completion.choices[0].message.content))


