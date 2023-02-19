import openai

openai.api_key = "sk-"

def imagin(prompt):
    # Use a breakpoint in the code line below to debug your script.
    image_resp = openai.Image.create(prompt = prompt, n=4, size="512x512")
    return image_resp['data'][0]['url']


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = imagin('Disney Pokémon Pikachu 8k realistic')
    print(url)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
