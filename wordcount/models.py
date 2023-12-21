from django.db import models


# Модель для хранения загруженных файлов
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


#  Модель для хранения результатов работы словаря
class WordCountResult(models.Model):
    word = models.CharField(max_length=100)
    count = models.IntegerField()
    calculated_at = models.DateTimeField(auto_now_add=True)
