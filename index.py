import requests

def get_definition(term):
    url = f"https://new-kbbi-api.herokuapp.com/cari/{term}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['data']:
            # Ambil definisi dari data
            return data['data'][0]['arti']
        else:
            return "Maaf, definisi tidak ditemukan."
    else:
        return "Terjadi kesalahan saat menghubungi API."

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "apa itu" in user_input:
        term = user_input.replace("apa itu", "").strip()
        definition = get_definition(term)
        return definition
    else:
        return "Saya tidak mengerti pertanyaan Anda."

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print(f"Bot: {response}")
  
