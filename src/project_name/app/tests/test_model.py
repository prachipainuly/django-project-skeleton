from django.test import TestCase

from ..models.sample import Sample


class ModelTestCase(TestCase):
    """This class defines the tests suite for the sample model."""

    def setUp(self):
        """Define the tests client and other tests variables."""
        self.user_id = "1"
        self.name = "User1"
        self.highlight = Sample(user_id=self.user_id, name=self.name)

    def test_model_can_create_a_sample_object(self):
        """Test the sample model can create an object."""
        old_count = Sample.objects.count()
        self.highlight.save()
        new_count = Sample.objects.count()
        self.assertNotEqual(old_count, new_count)
