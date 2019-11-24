from flaskblog import app
import unittest



class Testapp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_main(self):
        req = self.app.get('/rent')
        assert req.status == '200 OK'

    def test_404(self):
        rv = self.app.get('/test')
        self.assertEqual(rv.status, '404 NOT FOUND')
