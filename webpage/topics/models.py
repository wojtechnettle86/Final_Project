from django.db import models

class Topic(models.Model):
  topic_name = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.topic_name}"
