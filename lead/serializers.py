from .models import Lead
from rest_framework import serializers


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = (
            'company',
            'contact_person'
            'email',
            'phone',
            'website',
            'confidence',
            'estimated_value',
            'status',
            'priority',
            'created_by',
            'created_at',
            'modified_at',
        )
