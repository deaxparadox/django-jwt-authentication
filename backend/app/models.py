from collections.abc import Iterable
from typing import Any
from django.db import models
import uuid
from django.db.models.signals import post_save, pre_init
from django.dispatch import receiver
from django.utils.text import slugify


class Question(models.Model):
    name = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs) -> None:
        return super().save(**kwargs)
    


class Option(models.Model):
    name = models.CharField(max_length=120)
    votes = models.PositiveIntegerField(default=0)
    question = models.ForeignKey(Question, related_name="options", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    

class Poll(models.Model):
    question = models.ForeignKey(Question, related_name="poll", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.description[:100] if self.description is not None else self.question.name
    
    def save(self, *args, **kwargs) -> None:
        return super().save(*args, **kwargs)


@receiver(post_save, sender=Question, dispatch_uid="create_poll_object")
def create_poll(sender, instance, *args, **kwargs):
    """
    Create a Poll object after successfull Question object creation.
    
    If the Poll object is created for newly created Question object,
    then create Poll.
    """
    try:
        Poll.objects.get(question=instance)
        print("Poll object exists")
    except:
        p = Poll.objects.create(question=instance)
        print(f"Poll object: {p}")
    
    
    