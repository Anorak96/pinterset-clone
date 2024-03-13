from django.db import models
from user.models import User

class Tag(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag
    
class Pin(models.Model):
    profile = models.ForeignKey(User, on_delete=models.DO_NOTHING,  related_name="profile_post")
    pin = models.ImageField(upload_to='pins')
    tag = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.description[:10]