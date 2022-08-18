from .test_setup import TestSetUp
from rest_framework import status 

class TestViews(TestSetUp):
    def test_user_cannot_register_with_no_date(self):
        res=self.client.post(self.register_url)
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)

        # import pdb
        # pdb.set_trace()

    def test_user_can_register_correctly(self):
        res=self.client.post(self.register_url, self.user_data,format='json')
        self.assertEqual(res.data['email'],self.user_data['email'])
        self.assertEqual(res.data['username'],self.user_data['username'])
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)