from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='Вопрос')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    choice_text = models.CharField(max_length=200, verbose_name='Текст выбора')
    votes = models.IntegerField(default=0, verbose_name='Голоса')

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = 'Выбор'
        verbose_name_plural = 'Выборы'