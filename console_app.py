from assistant import Assistant

def main():
    assistant = Assistant()

    while True:
        command = input("Введіть команду (/add, /list, /search, /exit): ")

        if command == "/add":
            note = input("Введіть нотатку: ")
            assistant.add_note(note)
            print("Нотатку додано.")
        elif command == "/list":
            notes = assistant.list_notes()
            if notes:
                print("Нотатки:")
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note}")
            else:
                print("Список нотаток порожній.")
        elif command == "/search":
            keyword = input("Введіть ключове слово: ")
            results = assistant.search_notes(keyword)
            if results:
                print("Знайдено нотатки:")
                for note in results:
                    print(f"- {note}")
            else:
                print("Нічого не знайдено.")
        elif command == "/exit":
            break
        else:
            print("Невідома команда.")

if __name__ == "__main__":
    main()
