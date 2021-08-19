from rest_framework import generics
from ..serializers.sample_serializer import SampleSerializers
from ..models.sample import Sample


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Sample.objects.all()
    serializer_class = SampleSerializers

    def perform_create(self, serializer):
        """Save the post data when creating a new highlight."""
        serializer.save()
