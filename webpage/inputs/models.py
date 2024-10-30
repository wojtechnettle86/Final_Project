from django.db import models

class Input(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  question_name = models.CharField(max_length=255)
  question_text = models.TextField(max_length=3000)
  doctor = models.CharField(max_length=255, null=True, blank=True)
  answer = models.TextField(max_length=3000, null=True, blank=True)
  privacy = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.question_name}"
