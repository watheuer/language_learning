from django.db import models


class Word(models.Model):
    text = models.CharField(max_length=128)
    usages = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.text


class Document(models.Model):
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.body[:50] + ' from ' + self.created.date()