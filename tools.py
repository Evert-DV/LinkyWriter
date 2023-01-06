import random


def set_output_file():
    output_file = input("Destination file (.txt): ")

    if output_file[-4:] != '.txt':
        output_file += '.txt'

    print(f"\n* Output file changed to {output_file} *")

    return output_file


def set_words_pars():
    while True:
        try:
            words = int(input("Number of words: "))
            break
        except ValueError:
            print("Enter a valid integer")

    goal = words // 100
    pars = words // 60
    pars += (goal - pars % goal)

    return words, pars


def create_prompt(n_words, n_pars, style, keywords, use_deepl):
    if use_deepl:
        msg = f"Write a text of {int(n_words)} words and {int(n_pars)} paragraphs. Make the text {style[0]} and" \
              f" {style[1]}, don't make it commercial or advertising. It should contain the keyword(s)" \
              f" {keywords.strip(', ')}. Give each paragraph a number."
    else:
        msg = f"Schrijf een tekst van {int(n_words)} woorden en {int(n_pars)} alinea's. Maak de tekst {style[0]} en " \
              f"{style[1]}, maak het niet commercieel of adverterend. De tekst moet de zoekterm(en) " \
              f"{keywords.strip(', ')} bevatten. Geef elke alinea een nummer."
    return msg
