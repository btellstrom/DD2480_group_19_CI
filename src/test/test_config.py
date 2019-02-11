import unittest
from src.main import config
from os.path import abspath

class test_config(unittest.TestCase):

    def test_init_with_file(self):
        """
        Test so that all variables are initialised properly 
        from the config-file
        """
        temp = abspath('src/test/config_example.ini')
        config.init(temp)

        # Test the api_token option
        self.assertTrue(
            config.api_token == "jibberish"
        )

        # Tests that the database name is properly initialised
        self.assertTrue(
            config.mongo_database_name == "CI-History"
        )

        # Test that the ip-address of the database is properly initialised
        self.assertTrue(
            config.mongo_ip == "192.168.0.1"
        )

        # Test that the database port is properly initialised
        self.assertTrue(
            config.mongo_port == '27017'
        )

        # Test that the database user is properly initialised
        self.assertTrue(
            config.mongo_user == "ci_19"
        )

        # Test that the database user password is properly initialised
        self.assertTrue(
            config.mongo_pass == "password"
        )

    def test_init_default(self):
        config.init()

        # Test that api_token is properly initialised as None
        self.assertTrue(
            config.api_token == ''
        )

        # Test that name is properly initialised
        self.assertTrue(
            config.mongo_database_name == "CI-History"
        )

if __name__ == '__main__':
    unittest.main()
