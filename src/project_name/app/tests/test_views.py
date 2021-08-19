from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from ..models.sample import Sample


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the tests client and other tests variables."""
        self.client = APIClient()
        self.highlight_data = {'user_id': '1', 'name': 'User1'}
        self.response = self.client.post(
            reverse('create'),
            self.highlight_data,
            format="json")

    def test_api_can_create_an_object(self):
        """Test the api has highlight creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_an_object(self):
        """Test the api can get a given object."""
        sample = Sample.objects.get()
        response = self.client.get(
            reverse('details',
                    kwargs={'pk': sample.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertContains(response, sample)

    def test_api_can_update_highlight(self):
        """Test the api can update given object."""
        sample = Sample.objects.get()
        change_sample = {'user_id': '1', 'name': 'User1'}
        res = self.client.put(
            reverse('details', kwargs={'pk': sample.id}),
            change_sample, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_highlight(self):
        """Test the api can delete an object."""
        sample = Sample.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': sample.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
