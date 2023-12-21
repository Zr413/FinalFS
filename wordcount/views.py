from django.shortcuts import render
from django.http import HttpResponse
from utils import WordCounter

word_counter = WordCounter()  # Создаем экземпляр WordCounter


# Создаем функцию для обработки запроса к приложению
def index(request):
    return render(request, 'index.html')


#  Функция для загрузки файла
def load_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        # Далее можно сохранить файл и передать его содержимое в нашу WordCounter
        word_counter.load_file(file.read().decode('utf-8'))
        return HttpResponse("Файл успешно загружен.")
    else:
        return HttpResponse("Загрузка файла не удалась.")


#  Функция для обработки запроса подсчета количества вхождений
def word_count(request):
    if request.method == 'POST' and 'word' in request.POST:
        word = request.POST['word']
        count = word_counter.word_count(word)
        return HttpResponse(f"Вхождения '{word}': {count}")
    else:
        return HttpResponse("Подсчет слов не удался.")


#   Функция для очистки памяти от результатов подсчета количества вхождений
def clear_memory(request):
    word_counter.clear_memory()
    return HttpResponse("Память очищена.")
