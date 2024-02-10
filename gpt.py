import g4f

g4f.debug.logging = True  # Enable debug logging
g4f.debug.version_check = False  # Disable automatic version checking
print(g4f.Provider.Bing.params)  # Print supported args for Bing




## Normal response
def call(text):
    prompt = f"Create 3-4 questions and answers(use just the info provided in this prompt, no external sources) for flashcards for the following text: {text}. Return your answer in the format: (Question:(insert_question)), (Answer:(insert_answer))\n"


    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        provider="You",  # Specify the You provider
        messages=[
            {"role": "user", "content":prompt}
        ]
    )    
    return response