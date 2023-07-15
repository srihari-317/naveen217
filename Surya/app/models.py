from django.db import models


class Contact(models.Model):
    name= models.CharField(max_length=30,null=False)
    email= models.CharField(max_length=30)
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
def __str__(self):
    return "%s %s %s %s %"(self.name,self.email,self.subject,self.message)

    
