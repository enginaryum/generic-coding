from django.db import models


class Author(models.Model):
  isActive = models.BooleanField(default=False)
  notifyAllTopics = models.BooleanField(default=False)
  notifyAllEntries = models.BooleanField(default=False)


class Topic(models.Model):
  author = models.ForeignKey(Author)
  
  
class Entry(models.Model):
  author = models.ForeignKey(Author)
  topic = models.ForeignKey(Topic)
  subscribed = models.BooleanField(default=False)
