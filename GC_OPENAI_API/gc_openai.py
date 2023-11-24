#Install the OpenAI Python library
#pip install --upgrade openai
#pip list

# importing openai module into your openai environment 
from openai import OpenAI

#============> SETTINGS <============#
OPENAI_API_KEY='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'
OPENAI_MODEL = "gpt-3.5-turbo"
OPENAI_PROMPT = "Mi sai aiutare?"

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=OPENAI_API_KEY,
)

#models = client.models.list()
#for model in models:
#    print(model.id, model.model_parametrized_name)

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": OPENAI_PROMPT,
        }
    ],
    model=OPENAI_MODEL,
)

print(response.choices[0].message.content)

print(f"\nTotal tokens: {response.usage.total_tokens}")










