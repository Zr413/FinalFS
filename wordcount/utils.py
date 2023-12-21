import re


class WordCounter:
    def __init__(self):
        self.words = {}

    def load_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = file.read()
                words = re.findall(r'\b[a-zA-Z]+\b', data)
                for word in words:
                    word = word.lower()
                    if word in self.words:
                        self.words[word] += 1
                    else:
                        self.words[word] = 1
                print("Файл успешно загружен.")
        except FileNotFoundError:
            print("Файл не найден.")

    def word_count(self, word):
        word = word.lower()
        if word in self.words:
            print(f"Вхождения '{word}': {self.words[word]}")
        else:
            print(f"'{word}' не найдено.")

    def clear_memory(self):
        self.words = {}
        print("Память очищена.")

    def show_help(self):
        print("Доступные команды:")
        print("load <имя файла> — Загрузить слова из файла")
        print("wordcount <слово> — Отображение количества вхождений слова")
        print("clear-memory — Очистить все загруженные слова из памяти")
        print("exit — Выйти из программы")


if __name__ == "__main__":
    word_counter = WordCounter()
    while True:
        command = input("Введите команду: ").split()
        if command[0] == "help":
            word_counter.show_help()
        elif command[0] == "load" and len(command) == 2:
            word_counter.load_file(command[1])
        elif command[0] == "wordcount" and len(command) == 2:
            word_counter.word_count(command[1])
        elif command[0] == "clear-memory":
            word_counter.clear_memory()
        elif command[0] == "exit":
            break
        else:
            print("Неверная команда. Введите «help», чтобы увидеть доступные команды..")
