from practical06.Language.language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    language_list = [ruby, python, visual_basic]

    for language in language_list:
        print(language)

    print()
    dynamic_list = [language for language in language_list if language.is_dynamic()]

    print("The dynamically typed languages are: ")
    for language in dynamic_list:
        print(language.name)


if __name__ == '__main__':
    main()
