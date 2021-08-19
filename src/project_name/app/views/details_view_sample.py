from rest_framework import generics
from ..serializers.sample_serializer import SampleSerializers
from ..models.sample import Sample


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Sample.objects.all()
    serializer_class = SampleSerializers
