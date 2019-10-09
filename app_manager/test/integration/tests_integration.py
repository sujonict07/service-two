from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class ReverseStringAPITest(APITestCase):

    def test_create_reverse_string(self):
        url = reverse('message-list')
        data = {'message': 'new message'}
        response = self.client.post(url, data, format='json')
        expected_response = data.get('message')[::-1]
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('message'), expected_response)
        self.assertEqual(len(response.data), 1)
