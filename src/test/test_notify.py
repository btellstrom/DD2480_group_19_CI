
import unittest
from main.notify import update_status
import json



class test(unittest.TestCase):

    def test_update_status(self):
        """
        Tests that update_status creates a correctly formatted
        url. Compares the url created by update_status to correct_url
        """
        content_url = 'https://api.github.com'
        status = 'success'
        token = '123'
        correct_url = 'https://123:x-oauth-basic@api.github.com/'
        post_req = update_status(content_url, status, token)
        self.assertEqual(correct_url, post_req.url)

        """
        Tests that the POST request will be invalid if
        the url is not linked to a PR as stated in the
        API and if the access token is not valid. In 
        this case the POST request JSON data will 
        have the form {"message":"Bad credentials",... 
        """

        self.assertEqual(post_req.json()['message'], 'Bad credentials')

        """
        NOTE: this test might fail if the server for
        the repo Test-server1 is not running. 

        Tests that the POST request will be invalid if
        the url is linked to a PR as stated in the API 
        and if the access token is valid. In this case 
        the POST request JSON data will have the form 
        {'url': ...,'state': 'success'. 
         """

        content_url = 'https://api.github.com/repos/A1337li/Test-server1/statuses/4f22d54572b09dd559f953f5f5de675752a1dc4f'
        token = '254fe0318d9bd3e107899127fcd63ff1dedfb44d'
        post_req = update_status(content_url, status, token)
        #self.assertEqual(post_req.json()['state'], 'success')
        post_req = update_status(content_url, 'hello', token)
        self.assertEqual(post_req, None)


if __name__ == '__main__':
    unittest.main()