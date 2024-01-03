from django.db import models


class ContactMessageModel(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    SUBJECT_CHOICES = [
        ('subject1', 'Influencer'),
        ('subject2', 'Working Together'),
        ('subject3', 'Question & Help'),
    ]
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    message = models.TextField()
    send_at = models.DateTimeField(auto_now_add=True)

    def formatted_send_at(self):
        return self.send_at.strftime('%d %b %Y %H:%M')  # Türkçe tarih formatı

    def __str__(self):
        return self.full_name
