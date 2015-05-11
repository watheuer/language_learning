from django.db import models
from django.contrib.auth.models import User


class Word(models.Model):
    text = models.CharField(max_length=128)
    usages = models.IntegerField(default=0)

    definition1 = models.TextField(null=True, blank=True)
    definition2 = models.TextField(null=True, blank=True)
    definition3 = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.text


class Document(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.body[:50] + ' from ' + str(self.created.date())


class VocabList(models.Model):
    title = models.CharField(max_length=256)
    document = models.ForeignKey(Document, null=True, blank=True)
    words = models.ManyToManyField(Word)
    user = models.ForeignKey(User)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title + ' from ' + str(self.created.date())


class Definition(models.Model):
    word = models.ForeignKey(Word)
    text = models.TextField(null=True, blank=True)
    pos = models.CharField(max_length=8)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)