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

    pars = int(words // 100) * 2

    return words, pars
