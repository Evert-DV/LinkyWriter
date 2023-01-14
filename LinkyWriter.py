import os
import random
from pyChatGPT import ChatGPT
from tools import *
from DeepL import DeepL_Translator

# Initiate the ChatGPT session
session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..r1NDxwXXfSIEDR9U.WCw2r7ezF3LNfBHuMjI8yvBLjNkaxMwqYujaH5E3xIb2dMJw5PnjkcurKwI9ja54bddLtfsjUNaP1Cd_-2K6N2qwvSBOtyPCefsD3U6A2KMfemOXKVHQbTvhtdJlFeWDuVsX1wZaOTwbD1A7p_LA_b6F97elindtSCsiONbPZolSqh-156UCjQBHQfTK8uMHELwdY54dMWRx73iyfnLfyJf1CWSXVtkZk0M-FT5hrwfUXVIgeHqDNlURES5eEUGg0LM-mf91iBQjBmESAGiq7TDQVfTQTqKXRBQdbMAoJePLkrlmq6mXgzwMZN1R1SuuVjife12LrZX8SnhPK7g-Bw-bO2hnqKYPWhtJsy1ANpfFbhKTr0hQADH3U0m99Lq_ZoM5bnrioVzznbbOoxv9ZsqOqmybBtOHx7iyALs7rQ12fC74b0eSsr4EBZcYs3nscdbMTrbU1Criimwi8kJTiygzrUrliBnaaMb_5tGP6JqjaZLjlvIAW4GYW2HOGmrEZz8z7vi43EG8Ooo6blsPRAMM46dNarVCBvdIwrMuM70EHGg8vOABPbMMJD4RuArr784_iyIGjTpt-P7PrRAEYj6-d1MIO-GMOTDLl0PP_FIQCNw8w61smYxVUHZI-S0koXOmQmmlJSJIKiWlx5t_CJ-5hHTLehPSxugw8B_s5-ols8kSdPeLs64z1A-bzjgK13EdxZRnirA_-8MS8OeWpa25HmkpgCXkYVcFNAO23azSKbq8silKOgO-uGjIdzGKj1oH9B7iDYmy0LIxh_68I-W_C9apvvqK5-yqZjvAKJEGiuI4Obb26dPJ6hxSeHIP2e7Dc-koXqt3qhjLAHt8GREMBVQpdAOJ7sMWQSITmx2RYTJBHxTXmXKHfE9osbAwLoVeFRwtBcfg46Zd0lANtvJkfHlTNWNrxuyHvVKcPwSc0BZn-OrKAa1mRegFeUsDuxgqF4AGVAaw3quio3h1hmPy5V3fL6GDfrkveaoglrQ_Q4Wr_pwkrrVnp7HDGv7DqgsNXvv7cG-yj0dg6swwjLPs5RIOxgDYzYfRBwlM-xjhNELA8h1czrTrzAETALd9sZoxwBDDTP7drSQitdcYKg2M-CoWmOx24S3_YXl9hBomKzsoFJN2EqmCL44ckU_FJb77ryj9q7Xurxg1WUCgHqVL25NfaSUNirfnwpjY8De-wpvxS7DHDm5lkJTaa-Vy-E4W1typwgDTq0uyFwmqzB2DkxpxZ5_BQqc3AMWA5rrbdaavlbkhLZDFRB_2cRVLXbPl0MOO9lTCVABuHl9ygJsw7muBB4nVVXUZ5QOGh79pu73-b9V4pdkXHoQwQ6YYIkk5qYq7qAUvvRYpttTYeKWBGJM2u8nArSyOE1hxOtyMF_T0kG3X2g2HHkFhs_U79DmgW7ykVTlEuReAcLRSoY3v-NSgm4JNZSyuVg2NohFxF-KaV8L-JnWXBnkvMhEqUdsy72YH_7VrxjGImk7a7JwCuW3Sg3PPIU5Kx9VIm1P4r6NwB6REFSjU0pegY1ePu3RNo3SfJWsC1mgxVf7h7tbfRZRImXnykSFWL8JQ5LdcQsIz_x42XfaycAPi9t8e86Cmyn8agj06gSGfrIuZx8qpgUdELhF_KF7x5Y78Wo1ZHGgtwePtPKDtnCIiljOahWBgxjtJzyh6O_1TtEs6Q0CdDSn9QCmM5yTGwsu20EnY-xZ82DVv13wMi8T4Ul2mli6-efKS66qDn7baJmoWOgFDGB0aTfuf7b6Ji1Dwhmq-KleIl7mp5Z2Nvr5gAZHhekvt8v-SJcYz5gTVFiCpvrcNF2Q_ZXBiFuF-FkYVgiGpfXcDnpGqGs4dA-d2adQKMyZ1lvywaeo34_uKkVmG-v-mdu9DgX7PcZGFy-gQV5m4lFTWOc9H_4GBkWtuWWGEd6DcWgrrNuYWBQ_s-M3LNKDzRyD65BUaQhexnzANlQev3T1wrdte4snZoAkjbE5BfTqx1iDX_CF2GIaO8-w3AxSkay88_8LJbPItkbCy1lPf28jg_hsfV9wHs3Jrd4a_GncEQERVBdPsZEJ9JNN27c7zBoBAfVo8NQTVF1ikmXKrFh542bM8zXHHJeTzFNXhO38RdnqDGNQ3xP4ojeQo7GXMbpLNASdW-6rjWpYqgF7F-BoZi7GImYiBfT2vwyOaA26pFZWwWx-sN8n__Pe0b-Cpv7TvQI3P3tJkTpqFhOPnHTo8mJ-uU4Pt5-bGvJ53SBOrAHnzfQQ5VIYEyvvMtEDsdLGVu5xuuTnsT4awyqsXz3n3FJbPbCTe7E5bB8HbbyjLXmQ_CMr1IKrzb6GGYurCxhCrI0lDb0lUAtpiYhT3YaAz9wq3cYx4Q9gt3cpqgVeODQYdroRv6gJP.7SVilKlUfcRpp1ULKvg4gA"
chat_id = ''
api = ChatGPT(session_token, conversation_id=chat_id)

translator = None

destination_file = set_output_file()

# Define the styles and moods for the two languages
styles = {'nl': ['algemeen', 'informatief', 'professioneel', 'informeel', 'formeel', 'basic', 'oppervlakkig',
                 'diepgaand', 'samenhangend', 'relaxed', 'educatief', 'eenvoudig', 'vrolijk', 'luchtig', 'Vlaams'],
          'en': ['general purpose', 'informative', 'professional', 'informal', 'formal', 'basic', 'superficial',
                 'in-depth', 'coherent', 'light-hearted', 'educational', 'extensive']}

while True:
    use_deepl = False
    mode = input("\nGeneral prompt (g), new text (t), product description (p) or new file (n)? Quit (q): ")

    if mode == "n":
        destination_file = set_output_file()
        continue

    elif mode == "t" or mode == "p":
        lang = 'nl'
        keywords = ''

        n_words, n_pars = set_words_paragraphs()

        if n_words > 310:
            lang = 'en'
            use_deepl = True

            if translator is None:
                print("\n* contacting DeepL *\n...")
                translator = DeepL_Translator()
                print("* ready *\n")

        zoekterm = input("Keywords: ")
        zoekterm = zoekterm.split(',')
        for w in zoekterm:
            keywords += f'"{w.strip(" ")}", '

        style = random.sample(styles[lang], k=2)

        if mode == 'p':
            msg = f"Schrijf een productomschrijving van {n_words} woorden en {n_pars} alinea's. Maak de tekst" \
                  f" adverterend, {style[0]} en {style[1]}. Gebruik de woorden {keywords.strip(', ')}. Geef elke " \
                  f"alinea een nummer."
        else:
            msg = create_prompt(n_words, n_pars, style, keywords, use_deepl)

    elif mode == 'q':
        print("\n* resetting and shutting down *")
        api.reset_conversation()
        break

    else:
        msg = input("ChatGPT prompt: ")

    print(msg)

    response = api.send_message(msg)
    response_text = response["message"]

    if use_deepl:
        # Keep track of translated characters (for possible future API service costs)
        update_count(response_text)

    print("\n* response received *")

    if use_deepl:
        translated = translator.translate(response_text)
        response_text = translated
        print("\n* translation complete *")

    with open(f"C:\\Users\\Evert\\Documents\\Python\\LinkyWriter\\texts\\{destination_file}", 'a') as f:
        f.write("\n =========== \n")
        f.write(response_text)

    written_words = len(response_text.split(' '))

    print(f"\n* {int(written_words)} words written to {destination_file} *\n")

api.driver.close()
api.driver.quit()

# Set the directory you want to delete the files from
directory = "C:/Users/Evert/AppData/Roaming/undetected_chromedriver"

# Iterate over all the files in the directory
for filename in os.listdir(directory):
    # Construct the full filepath
    filepath = os.path.join(directory, filename)
    try:
        # If the file is a regular file, delete it
        if os.path.isfile(filepath) or os.path.isdir(filepath):
            os.unlink(filepath)
    except Exception as e:
        print('exeption: ', e)
