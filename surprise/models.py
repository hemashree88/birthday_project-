from django.db import models

class LoveMessage(models.Model):
    message = models.TextField()

    def __str__(self):
        return "Birthday Message"


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery')

    def __str__(self):
        return "Gallery Image"
