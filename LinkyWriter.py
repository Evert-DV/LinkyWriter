import os
from pyChatGPT import ChatGPT
from tools import *
from DeepL import DeepL_Translator

session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0.._kyY2FxnKx85hu7_.MIYbgBqtp9OhSAYBcqNsbOOkwxCdUUMoRARgy1QGsj0v4TMwYEzNnnzCaTeE8w3y0bBLGu1Au7c5hznU8V-ojtggzHGsK8KZQ6bfXZ--3MF8uOXn11BUH0JooHIL4b1FPP8CReKvMzC6rsjciHYw7vA_UhxVQTIA9ChvFqy77QRXHBmnvVtZ4DqEV1-Nzd0Xzl48LfJZH-ngzLi0ISL4xMD9ovy00h8oU-3ETc3fpNbTrOJJ0VKTK95oVfE6y4Sx3QAgxvaIk2rg20rQlqC5h4zwdQSQO2Hb2O4xZ9u9N5aEHIzse6ZRk4pnondOw4chKJqE4NUefFZ5Bms2c3iB5E4UNIZA5oyDuW1r6Kz0NDa-ki1M8UtQJXFWeBN-9BqLOVycrfvqHyaqolvlSt8hQyvKhyubojzeMFNLpR0u0c84VWZe0IvMLeBUeA7sn5RxTwA3gGaWtNNoKgv4Zi8AMYwlhaq1EvY9dL_473rdjcswR3FdUVo2Yfgt2wnoM5NJmTwegu6womDZHB3bleaiOm30ve3iHSzkChjMc7iUSPSQ4uxSKyCWrZR2cW2U1KNR3jW7Pq7G7oHL8z0JXHJ3RbwlESLrAHjSMl9qdF9Cy2sW80rAyqAhy2_ojKdymzW_gT8u8nvBkf2t0IxK80SMrEqPkLMMjoFNtLRAONUxm0D3qqpPfsUyaLm4EPuG-n4aiE1wLE0vfISOs4fIPA878fA5cRbpt7SVAIgdFe3SxZriUmutzDr6D8mJKr5jV5yONbirlFBkjq6DcCu59jePWaxNkROBpWV4ejmaOKpUtvRVZJE4-XaZrCQZ3e1WSJCugwFxAuw-kuXnT12HKbiy4EjvC3eWNphAUARCViSM0teNqAqEAVFgSAjobPbyPVd_ui6RgN70jDc13r60O-pWY8CjEYJpR9BG8FClrJc7Q2BZ4UqYUsoDbr4k1jnT1TPteLcWcJI3SOm904ME3ZMgMI7aH1X-mzy1UrunFqnzBPKw2a_tgsmfmwmTLI4l2VZRabhgA0IZBBPubxv5S5l1jAOL23vn0JqyLZoptr0lrq4-6Ft5kbFzNMhZHmbchp-u7Hj-ZjBPLSmpaq0Eac67Cfjbzw4ln9IpnWeuFlcn2DjnBVuBw6YM2Vb4BErbOWJaXghQiuCwo0__3CfKiFOIx3c8PJItTiEsDgkp-miCbBhrjazCDMKQOMpmvVaIcD69Ft2JmV-r3RnU1VVR9Wf2G81gL3DBKX6duiyUeGHdnGNlM3COI1dy-uEwl7cO_Xl2mnD3gemf7LyDc8-6ul3DNoEedhu8bNjgJWt_h3Qc-l-AAPw0tO0NEa_2U43EUnhnXzQXGZlBcrrlet7zVFUT5RpTFXG2Tvintyu0YxCM5b41P3U0sn9uzUkw6wLkfrMVg-eGW4okbNrdJS0_g5Tk2gj5WEPckH91gxnY-pHeLBwWPBvt8SgHfGwDOouRI59266zJ_AdXTVYp19RVi2HvKFqq86SalgF8X-lvMTmMgc4IF9QONoT-GTBGs75NJ_kSdZCaYAKdlT-sV6by1WCm2FW5PRLNiykZetmhgh-3Kt3I8yBxwFqwogmdOjzaCVv2PhwcNCvHEyvfH77RIMfApjftZFLn-dAK9L3Y7wcbXEztHUubVcyct8uQFhtoyb1JO2EZcHgu36CAHAGd_EJuH6Fse9u5N587rdBS_JLsy-Pwibkfex_7hqRuOvDdxbwESdvq-aicetgOHyakhoZGW7lRNvgsu6V6YaRn9-sBccAhQhEZXRkeQOmcnPGcXToV_GM-7lvLu3_YFrzmup7NdmcvgdJc3pwcVqRvGz1Jyca7wD_1JVcSPt_k6KMJI9p9fVgirCPY70hBGqsUh5deF45l6ZaQpYpEa4OZF8YMn1UV-6DpcO3QCM8yXgB7jbvjL-_X_mBjJZM_RMvlzL6XWhQ854_4kX1Ix7YJZTnc0sN9DIanejfWt0ITZDN746zBnT1JD1Eb6r3rJJXD1xtcqh-vUbZ7E8L0vCqsNVO0Wz1yFH_jbdg2xAB0-Hcx3L-6m8Z3DRywtU5jYDDJUq_MiZuej3y6CwefQNW2K4Lp755tJLo9aKt5ZO9ldk-1YiwiQRuUAvfNT7_lMfHN5BeK79HyTCR_EOjhg1i9PuHGdiR-qXdSmZOXvJ-xwfmUZq32nXULIDIm65gOf-tABs0PKSXNi264hASf5DRnUummpyCGhVayjPZaHW0dhDjkp5vpr-69Rk4ls5kDbUcXhJX2HjUKHrIlaDjiV0pPYO8CGh9fBdbCEjgTHvAtAc5ENCtJUkKr8KXeLcs_2NERVaPMC5ub3eKx2MDTI2xdm08FxtjDf_GAoyClU1lNIE-EF147fwqsOiJFR4NvlqYV.VfR7TCoKmVfxBROfg_l_4g"

api = ChatGPT(session_token)
translator = None

destination_file = set_output_file()

styles = {'nl': ['algemeen', 'informatief', 'professioneel', 'informeel', 'formeel', 'basic', 'oppervlakkig',
                 'diepgaand', 'samenhangend', 'relaxed', 'educatief', 'eenvoudig', 'vrolijk', 'luchtig'],
          'en': ['general purpose', 'informative', 'professional', 'informal', 'formal', 'basic', 'superficial',
                 'in-depth', 'coherent', 'light-hearted']}

while True:
    use_deepl = False
    mode = input("\nGeneral prompt (g), new text (t) or new file (n)? Quit (q): ")

    if mode == "n":
        destination_file = set_output_file()
        continue

    elif mode == "t":
        lang = 'nl'
        keywords = ''

        n_words, n_pars = set_words_pars()

        if n_words > 310:
            lang = 'en'
            use_deepl = True

            if translator is None:
                translator = DeepL_Translator()

        zoekterm = input("Keywords: ")
        zoekterm = zoekterm.split(',')
        for w in zoekterm:
            keywords += f'"{w.strip(" ")}", '

        style = random.sample(styles[lang], k=2)

        msg = create_prompt(n_words, n_pars, style, keywords, use_deepl)

    elif mode == 'q':
        break

    else:
        msg = input("ChatGPT prompt: ")

    print(msg)

    response = api.send_message(msg)
    response_text = response["message"]

    if use_deepl:
        with open('C:\\Users\\Evert\\Documents\\Python\\LinkyWriter\\Char_count.txt', 'r+') as f:
            contents = f.read()
            count = int(contents)
            count += len(response_text)
            f.seek(0)
            f.write(str(count))

    print("\n* response received *")

    if use_deepl:
        translated = translator.translate(response_text)
        response_text = translated
        print("\n* translation complete *")

    with open(f"C:\\Users\\Evert\\Documents\\Python\\LinkyWriter\\texts\\{destination_file}", 'a') as f:
        f.write("\n =========== \n")
        f.write(response_text)

    print(f"\n* written to {destination_file} *\n")

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
        print(e)
