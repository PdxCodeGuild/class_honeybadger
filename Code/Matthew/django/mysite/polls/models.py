from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text + ', ' + str(self.choices.count()) + ' choices'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.question.question_text + ' - ' + self.choice_text

