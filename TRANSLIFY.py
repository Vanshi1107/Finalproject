'''THE TRANSLATION APP'''

''' This is a simple program which take input from the user about the text in english and the language he/she wants to translate the text into.
And this process can be continues until the user wants either with the same language or a different language'''


import googletrans
from googletrans import Translator


def main():

    translator = Translator()
    languages = googletrans.LANGUAGES       #This variable contains a dictionary of all the language code and their corresponding languages.

    #The inputs that are needed to run the code.
    text_to_be_translated = input("Enter text to be translated: ")
    lang_to_translate_into = get_a_valid_lang_input(languages)
    lang_code = get_language_code(lang_to_translate_into, languages)

    translate_text= translated_output(translator,text_to_be_translated,lang_code)
    print()
    print("The translation is :", translate_text)

    ans = "y"

    while ans == "y":
        ans = input("Do you want to continue? (y/n): ")
        print()

        if ans == "y":
            next_language = input("Do you want to continue with the same language as last time? (y/n): ")
            print()

            if next_language == "y":
                # Translating in the same language as last turn.
                text_to_be_translated = input("Enter text to be translated: ")
                translate_text = translated_output(translator, text_to_be_translated, lang_code)
                print()
                print(translate_text)

            elif next_language == "n":
                # Getting input of a new language and translating into that.
                lang_to_translate_into = get_a_valid_lang_input(languages)
                lang_code = get_language_code(lang_to_translate_into, languages)
                text_to_be_translated = input("Enter text to be translated: ")
                translate_text = translated_output(translator, text_to_be_translated, lang_code)
                print()
                print(translate_text)

            else:
                # When the input is invalid.
                while next_language != "y" and next_language != "n":  # Pushing for a valid answer from the user
                    next_language = input("Please enter a valid answer (y/n): ")
                    print()

        elif ans == "n": #The loop ends.
            break

        else:
            while ans != "y" and ans != "n":  # Pushing for a valid answer from the user
                ans = input("Please enter a valid answer (y/n): ")
                print()


    print()
    print("***********************")
    print()
    print("Thank you for your time!")
    print()
    print("***********************")



def translated_output(translator,text,lang_code):
    '''This function translated the obtained text and returns the translated text'''
    translated_text = translator.translate(text,src ="auto",dest=lang_code)
    return translated_text.text


def get_a_valid_lang_input(language_dict):
    '''This function gets a valid language input from the user i.e; with correct spelling or a existing language.'''
    lang_to_translate_into = input("Enter language to translate: ")

    while lang_to_translate_into.lower() not in language_dict.values():
        print("Check the spelling of the language properly.")
        lang_to_translate_into = input("Please enter a valid language to translate: ")
    return lang_to_translate_into


def get_language_code(lang_to_translate_into,languages):
    '''This function finds the language code of the given language from the dictionary.'''
    for code,name in languages.items():
        if name == lang_to_translate_into:
            return code



if __name__ == "__main__":
    main()