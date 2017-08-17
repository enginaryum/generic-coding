# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from models import Author, Topic, Entry
# from django.shortcuts import render

def createSampleData():
  import itertools

  authorKeys = ['isActive', 'notifyAllTopics', 'notifyAllEntries']

  print map(lambda j: map(lambda i: map(lambda x: Author.objects.create(**dict(map(lambda y: (y, True), x))), itertools.combinations(authorKeys, i)), range(0, 3)), range(0, 2))

  print map(lambda k: map(lambda x: Topic.objects.create(author=x), Author.objects.all()), range(0, 2))

  print map(lambda t: map(lambda a: Entry.objects.create(author=a, topic=t, subscribed=False), Author.objects.order_by('-id').all()), Topic.objects.all())

# createSampleData()

