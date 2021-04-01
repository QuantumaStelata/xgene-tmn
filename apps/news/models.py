from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Article(models.Model):
    name = models.CharField(verbose_name='Название статьи', max_length=250)
    text = RichTextUploadingField(verbose_name='Текст статьи')
    date = models.DateTimeField(verbose_name='Дата публикации')
    is_publicate = models.BooleanField(verbose_name='Опубликовать?', default=False)

    def __str__(self):
        return self.name

    def __was__(self):
        return self.date

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    article = models.ForeignKey(Article, verbose_name='Коментарий к статье', on_delete=models.CASCADE)
    nick = models.CharField(verbose_name='Ник автора', max_length=100)
    text = models.CharField(verbose_name='Текст комментария', max_length=300)
    date = models.DateTimeField(verbose_name='Дата комментария', auto_now_add=True)

    def __str__(self):
        return self.nick

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'