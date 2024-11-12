from django.db import models


class FAQ(models.Model):

    question = models.CharField(max_length=255)
    answer = models.TextField( blank=False)

    def __str__(self):
        return self.question