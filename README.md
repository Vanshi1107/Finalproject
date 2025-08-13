# The Translation App

A simple Python program that translates text from English (or any language detected automatically) to a language of your choice using the Google Translate API.

---

## Features

* Translate text into multiple languages.
* Supports continuous translation without restarting the program.
* Option to continue translating into the same language or switch to a different language.
* User-friendly input validation for language names.

---

## Requirements

* Python 3.6+
* `googletrans` library

Install the library using pip:

```bash
pip install googletrans==4.0.0-rc1
```

> ⚠️ Note: Make sure to use version `4.0.0-rc1` as it is the most stable release for this library.

---

## How to Use

1. Clone the repository or download the script.
2. Run the script:

```bash
python translation_app.py
```

3. Follow the prompts:

   * Enter the text you want to translate.
   * Enter the language you want to translate into (e.g., `french`, `spanish`).
   * Decide whether to continue translating into the same language or a new one.
   * Repeat as needed.

4. Exit by typing `n` when asked if you want to continue.

---

## Example

```
Enter text to be translated: Hello, how are you?
Enter language to translate: french

The translation is: Bonjour, comment ça va?

Do you want to continue? (y/n): y
Do you want to continue with the same language as last time? (y/n): y
Enter text to be translated: I am learning Python.
The translation is: J'apprends Python.
```

---

## Functions

* `translated_output(translator, text, lang_code)` – Translates the input text into the specified language.
* `get_a_valid_lang_input(language_dict)` – Ensures the user enters a valid language name.
* `get_language_code(lang_to_translate_into, languages)` – Retrieves the language code required for translation.

---

## License

This project is open-source and free to use.

---

If you want, I can also make a **shorter, more aesthetic version** of the README that’s Instagram/post-friendly. It would be very concise and neat. Do you want me to do that?
