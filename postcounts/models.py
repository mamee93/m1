from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class PostCount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True) 
    count = models.IntegerField(default=0)
    def __str__(self):
        return str(self.count)

    @property
    def total_num(self):
        return self.count.all().count

class AllCounts(models.Model):
    all_count = models.ForeignKey(PostCount, null=True, related_name='+',on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.all_count)

    