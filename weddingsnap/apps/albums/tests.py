from django.test import TestCase


class TestGET(TestCase):
    """ $ ./env/bin/python weddingsnap/manage.py test albums """
    def test_albums(self):
        resp = self.client.get('/album/')
        self.assertEqual(resp.status_code, 200)

    def test_albums_json(self):
        resp = self.client.get('/album/all/json')
        self.assertEqual(resp.status_code, 200)

    def test_pictures(self):
        resp = self.client.get('/album/1/pictures')
        self.assertEqual(resp.status_code, 404)

    def test_pictures_json(self):
        resp = self.client.get('/album/1/pictures/json')
        self.assertEqual(resp.status_code, 404)
