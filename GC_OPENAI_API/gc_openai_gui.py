import tkinter as tk
from openai import OpenAI

#============> SETTINGS <============#
OPENAI_API_KEY='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'
OPENAI_MODEL = "gpt-3.5-turbo"

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=OPENAI_API_KEY,
)

def generate_response():
    # Get the user's input
    user_input = text_box.get("1.0", "end-1c")

    # Generate a response using the OpenAI API
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model=OPENAI_MODEL,
    )

    TOKENS_USED = "TOKENS_USED" + str(response.usage.total_tokens)

    # Update the chat window with the response
    chat_window.insert(tk.END, "OpenAI: " + response.choices[0].message.content + "\n" + TOKENS_USED + "\n" )

    print(response.choices[0].message.content)

'''
# Create the Tkinter window
window = tk.Tk()
window.title("OpenAI Chat")

# Create a text box for the user's input
text_box = tk.Text(window, width=80, height=10)
text_box.pack()

# Create a button to generate a response
generate_button = tk.Button(window, text="Generate Response", command=generate_response)
generate_button.pack()

# Create a text box to display the chat history
chat_window = tk.Text(window, width=80, height=20)
chat_window.pack()

# Start the main loop
window.mainloop()
'''

# Create the Tkinter window
window = tk.Tk()
window.title("OpenAI Chat")
window.configure(bg="#FFFFFF")

# Create a frame for the user's input
input_frame = tk.Frame(window, bg="#FFFFFF")
input_frame.pack(side=tk.TOP, fill="x")

# Create a label for the user's input
input_label = tk.Label(input_frame, text="Your Input:", bg="#FFFFFF", fg="#000000", font=("Arial", 12))
input_label.pack(side=tk.LEFT)

# Create a text box for the user's input
text_box = tk.Text(input_frame, width=80, height=10, bg="#FFFFFF", fg="#000000", font=("Arial", 12))
text_box.pack(side=tk.LEFT, padx=10)

# Create a frame for the chat history
chat_frame = tk.Frame(window, bg="#FFFFFF")
chat_frame.pack(side=tk.TOP, fill="both", expand=True)

# Create a label for the chat history
chat_label = tk.Label(chat_frame, text="Chat History:", bg="#FFFFFF", fg="#000000", font=("Arial", 12))
chat_label.pack(side=tk.TOP, anchor="w")

# Create a text box for the chat history
chat_window = tk.Text(chat_frame, width=80, height=20, bg="#FFFFFF", fg="#000000", font=("Arial", 12))
chat_window.pack(side=tk.TOP, fill="both", expand=True, padx=10, pady=10)

# Create a frame for the generate button
generate_frame = tk.Frame(window, bg="#FFFFFF")
generate_frame.pack(side=tk.BOTTOM, fill="x")

# Create a button to generate a response
generate_button = tk.Button(generate_frame, text="Generate Response", bg="#007BFF", fg="#FFFFFF", font=("Arial", 12), command=generate_response)
generate_button.pack(side=tk.LEFT, padx=10, pady=10)

# Start the main loop
window.mainloop()