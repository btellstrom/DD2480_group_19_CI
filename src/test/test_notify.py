import unittest
from src.main.notify import update_status
import json


class test(unittest.TestCase):

    def test_update_status(self):
        """
        Tests that update_status creates a correctly formatted
        url. Compares the url created by update_status to correct_url
        """
        data = {'head_commit': {'id': '123'}, 'repository': {'statuses_url': 'https://api.github.com/{sha}'}}
        status = 'success'
        token = 'abc'
        correct_url = 'https://abc:x-oauth-basic@api.github.com/123'
        post_req = update_status(data, status, token)
        self.assertEqual(correct_url, post_req.url)
        """
        Tests that the POST request will be invalid if
        the url is not linked to a push as stated in the API and if
        the access token is not valid. In this case the POST request
        JSON data will have the form {"message":"Bad credentials",... 
        """
        self.assertEqual(post_req.json()['message'], 'Bad credentials')

        """
        Tests that the POST request is None if an invalid status 
        input is given to update_status
        """
        post_req = update_status(data, 'hello', token)
        self.assertEqual(post_req, None)


if __name__ == '__main__':
    unittest.main()
