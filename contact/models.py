from django.db import models


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True, max_length=100)
    subscribed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    subject = models.CharField(max_length=254, null=False, blank=False)
    message = models.TextField()

    def __str__(self):
        return self.subject
