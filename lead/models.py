from django.db import models
from django.contrib.auth.models import User


class Lead(models.Model):
    NEW = 'new'
    CONTACTED = 'contacted'
    INPROGRESS = 'inprogress'
    LOST = 'lost'
    WON = 'won'

    CHOICE_STATUS = (
        (NEW, 'new'),
        (CONTACTED, 'contacted'),
        (INPROGRESS, 'inprogress'),
        (LOST, 'lost'),
        (WON, 'won'),

    )

    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    CHOICE_PRIORITY = (
        (LOW, 'low'),
        (MEDIUM, 'medium'),
        (HIGH, 'high'),
    )
    company = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    website = models.CharField(max_length=255, blank=True, null=True)
    confidence = models.IntegerField(blank=True, null=True)
    estimated_value = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=25, choices=CHOICE_STATUS, default=NEW)
    priority = models.CharField(max_length=25, choices=CHOICE_PRIORITY, default=MEDIUM)
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


