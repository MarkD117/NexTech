from django.db import models


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True, max_length=100)
    subscribed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email