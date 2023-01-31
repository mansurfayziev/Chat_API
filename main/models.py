from django.db import models

class User(models.Model):
    id_user=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100,blank=True)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class Message(models.Model):
    id_message=models.AutoField(primary_key=True)
    message=models.TextField()
    author=models.CharField(max_length=100)
    time_create=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
