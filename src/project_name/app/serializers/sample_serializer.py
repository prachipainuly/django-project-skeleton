from rest_framework import serializers
from ..models.sample import Sample


class SampleSerializers(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Sample
        fields = ('id', 'user_id', 'name')
