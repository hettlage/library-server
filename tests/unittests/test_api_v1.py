import json

from flask import url_for

from tests.unittests.base import BaseTestCase
from app.models import Astronomer, Keyword, Librarian

class ApiRoutesTestCase(BaseTestCase):
    def test_get_librarians(self):
        # create librarians
        Librarian.generate_fake(5)

        # get librarians
        res = self.client.get('/librarians')
        self.assertTrue(200 == res.status_code)

        # check that we found all librarians with all content
        librarians = json.loads(res.data.decode('utf-8'))
        self.assertTrue(len(librarians) == 5)
        for librarian in librarians:
            self.assertTrue('given_name' in librarian)
            self.assertTrue('surname' in librarian)
            self.assertTrue('email' in librarian)

    def test_get_librarian(self):
        Librarian.generate_fake(1)
        librarian = Librarian.query.first()

        # a librarian can be retrieved
        res = self.client.get('/librarians/{uuid}'.format(uuid=librarian.uuid))
        self.assertEqual(200, res.status_code)

        # and all content is returned
        json_response = json.loads(res.data.decode('utf-8'))
        self.assertTrue(json_response['given_name'] == librarian.given_name)
        self.assertTrue(json_response['surname'] == librarian.surname)
        self.assertTrue(json_response['email'] == librarian.email)

    def test_create_librarian(self):
        # create a librarian
        librarian = {
            'given_name': 'Peter',
            'surname': 'Murray',
            'email': 'murray@saao.ac.za'
        }
        res = self.client.post('/librarians', data=json.dumps(librarian))
        self.assertTrue(201 == res.status_code)

        # check that all content is present
        self.assertTrue('Location' in res.headers)
        json_response = json.loads(res.data.decode('utf-8'))
        self.assertTrue(json_response['given_name'] == librarian['given_name'])
        self.assertTrue(json_response['surname'] == librarian['surname'])
        self.assertTrue(json_response['email'] == librarian['email'])

        # get the new librarian
        location = res.headers['Location']
        res = self.client.get(location)

        # check that all content is present
        json_response = json.loads(res.data.decode('utf-8'))
        self.assertTrue(json_response['given_name'] == librarian['given_name'])
        self.assertTrue(json_response['surname'] == librarian['surname'])
        self.assertTrue(json_response['email'] == librarian['email'])

    def test_update_librarian(self):
        # create a librarian
        Librarian.generate_fake(1)
        librarian = Librarian.query.first()

        # update the librarian
        librarian_update = dict(surname="Magoda")
        res = self.client.put('/librarians/{uuid}'.format(uuid=librarian.uuid), data=json.dumps(librarian_update))
        self.assertTrue(200 == res.status_code)
        json_response = json.loads(res.data.decode('utf-8'))
        self.assertTrue(json_response['given_name'] == librarian.given_name)
        self.assertTrue(json_response['surname'] == librarian_update['surname'])
        self.assertTrue(json_response['email'] == librarian.email)

        # update the librarian again
        librarian_update = {
            'given_name': 'Xoliswa',
            'surname': 'Thamsanqa',
            'email': 'thamsanqa@saao.ac.za'
        }
        res = self.client.put('/librarians/{uuid}'.format(uuid=librarian.uuid), data=json.dumps(librarian_update))
        self.assertTrue(200 == res.status_code)
        json_response = json.loads(res.data.decode('utf-8'))
        self.assertTrue(json_response['given_name'] == librarian_update['given_name'])
        self.assertTrue(json_response['surname'] == librarian_update['surname'])
        self.assertTrue(json_response['email'] == librarian_update['email'])

        # get the updated librarian
        res = self.client.get('/librarians/{uuid}'.format(uuid=librarian.uuid))
        self.assertTrue(200 == res.status_code)

        # check that all content is present
        json_response = json.loads(res.data.decode('utf-8'))
        self.assertTrue(json_response['given_name'] == librarian_update['given_name'])
        self.assertTrue(json_response['surname'] == librarian_update['surname'])
        self.assertTrue(json_response['email'] == librarian_update['email'])

    def test_delete_librarian(self):
        # create a librarian
        Librarian.generate_fake(1)
        librarian = Librarian.query.first()

        # delete the librarian
        res = self.client.delete('/librarians/{uuid}'.format(uuid=librarian.uuid))
        self.assertTrue(204 == res.status_code)

        # check that the librarian has been deleted
        self.assertTrue(Librarian.query.filter_by(uuid=librarian.uuid).count() == 0)

    def test_get_astronomers(self):
        # create astronomers
        Astronomer.generate_fake(5)

        # get astronomers
        res = self.client.get('/astronomers')
        self.assertTrue(200 == res.status_code)

        # check that we found all astronomers with all content
        astronomers = json.loads(res.data.decode('utf-8'))
        self.assertTrue(len(astronomers) == 5)
        for astronomer in astronomers:
            self.assertTrue('given_name' in astronomer)
            self.assertTrue('surname' in astronomer)
            self.assertTrue('email' in astronomer)

    def test_get_astronomer(self):
        Astronomer.generate_fake(1)
        astronomer = Astronomer.query.first()

        # an astronomer can be retrieved
        res = self.client.get('/astronomers/{uuid}'.format(uuid=astronomer.uuid))
        self.assertEqual(200, res.status_code)

        # all content is returned
        json_response = json.loads(res.data.decode('utf-8'))
        self.assertTrue(json_response['given_name'] == astronomer.given_name)
        self.assertTrue(json_response['surname'] == astronomer.surname)
        self.assertTrue(json_response['email'] == astronomer.email)

    def test_create_astronomer(self):
        # create an astronomer
        astronomer = {
            'given_name': 'Peter',
            'surname': 'Murray',
            'email': 'murray@saao.ac.za'
        }
        res = self.client.post('/astronomers', data=json.dumps(astronomer))
        self.assertTrue(201 == res.status_code)

        # check that all content is present
        self.assertTrue('Location' in res.headers)
        json_response = json.loads(res.data.decode('utf-8'))
        self.assertTrue(json_response['given_name'] == astronomer['given_name'])
        self.assertTrue(json_response['surname'] == astronomer['surname'])
        self.assertTrue(json_response['email'] == astronomer['email'])

        # get the new astronomer
        location = res.headers['Location']
        res = self.client.get(location)
        self.assertTrue(200 == res.status_code)

        # check that all content is present
        json_response = json.loads(res.data.decode('utf-8'))
        self.assertTrue(json_response['given_name'] == astronomer['given_name'])
        self.assertTrue(json_response['surname'] == astronomer['surname'])
        self.assertTrue(json_response['email'] == astronomer['email'])

    def test_update_astronomer(self):
        # create an astronomer
        Astronomer.generate_fake(1)
        astronomer = Astronomer.query.first()

        # update the astronomer
        astronomer_update = dict(surname="Magoda")
        res = self.client.put('/astronomers/{uuid}'.format(uuid=astronomer.uuid), data=json.dumps(astronomer_update))
        self.assertTrue(200 == res.status_code)
        json_response = json.loads(res.data.decode('utf-8'))
        self.assertTrue(json_response['given_name'] == astronomer.given_name)
        self.assertTrue(json_response['surname'] == astronomer_update['surname'])
        self.assertTrue(json_response['email'] == astronomer.email)

        # update the astronomer again
        astronomer_update = {
            'given_name': 'Xoliswa',
            'surname': 'Thamsanqa',
            'email': 'thamsanqa@saao.ac.za'
        }
        res = self.client.put('/astronomers/{uuid}'.format(uuid=astronomer.uuid), data=json.dumps(astronomer_update))
        self.assertTrue(200 == res.status_code)
        json_response = json.loads(res.data.decode('utf-8'))
        self.assertTrue(json_response['given_name'] == astronomer_update['given_name'])
        self.assertTrue(json_response['surname'] == astronomer_update['surname'])
        self.assertTrue(json_response['email'] == astronomer_update['email'])

        # get the updated astronomer
        res = self.client.get('/astronomers/{uuid}'.format(uuid=astronomer.uuid))
        self.assertTrue(200 == res.status_code)

        # check that all content is present
        json_response = json.loads(res.data.decode('utf-8'))
        self.assertTrue(json_response['given_name'] == astronomer_update['given_name'])
        self.assertTrue(json_response['surname'] == astronomer_update['surname'])
        self.assertTrue(json_response['email'] == astronomer_update['email'])

    def test_delete_astronomer(self):
        # create an astronomer
        Astronomer.generate_fake(1)
        astronomer = Astronomer.query.first()

        # delete the astronomer
        res = self.client.delete('/astronomers/{uuid}'.format(uuid=astronomer.uuid))
        self.assertTrue(204 == res.status_code)

        # check that the astronomer has been deleted
        self.assertTrue(Astronomer.query.filter_by(uuid=astronomer.uuid).count() == 0)

    def test_get_keywords(self):
        # create keywords
        Keyword.generate_fake(5)

        # get astronomers
        res = self.client.get('/keywords')
        self.assertTrue(200 == res.status_code)

        # check that we found all astronomers with all content
        keywords = json.loads(res.data.decode('utf-8'))
        self.assertTrue(len(keywords) == 5)
        for keyword in keywords:
            self.assertTrue('keyword' in keyword)

    def test_get_keyword(self):
        # create a keyword
        Keyword.generate_fake(1)
        keyword = Keyword.query.first()

        # get the keyword
        res = self.client.get('/keywords/{uuid}'.format(uuid=keyword.uuid))
        self.assertTrue(200 == res.status_code)

        # all content is returned
        json_response = json.loads(res.data.decode('utf-8'))
        self.assertTrue(json_response['keyword'] == keyword.keyword)

    def test_create_keyword(self):
        # create a keyword
        keyword = {
            'keyword': 'MONET South'
        }
        res = self.client.post('/keywords', data=json.dumps(keyword))
        self.assertTrue(201 == res.status_code)

        # check that all content is there
        self.assertTrue('Location' in res.headers)
        json_response = json.loads(res.data.decode('utf-8'))
        self.assertTrue(json_response['keyword'] == keyword['keyword'])

        # get the new keyword
        self.assertTrue('Location' in res.headers)
        location = res.headers['Location']
        res = self.client.get(location)
        self.assertTrue(200 == res.status_code)

        # check that all content is present
        json_response = json.loads(res.data.decode('utf-8'))
        self.assertTrue(json_response['keyword'] == keyword['keyword'])

    def test_update_keyword(self):
        # create a keyword
        Keyword.generate_fake(1)
        keyword = Keyword.query.first()

        # update the keyword
        keyword_update = {
            'keyword': 'LCOGT'
        }
        res = self.client.put('/keywords/{uuid}'.format(uuid=keyword.uuid), data=json.dumps(keyword_update))
        self.assertTrue(200 == res.status_code)

        # check that all content is present
        json_response = json.loads(res.data.decode('utf-8'))
        self.assertTrue(json_response['keyword'] == keyword_update['keyword'])

        # get the updated keyword
        res = self.client.get('/keywords/{uuid}'.format(uuid=keyword.uuid))
        self.assertTrue(200 == res.status_code)

        # check that all content is present
        json_response = json.loads(res.data.decode('utf-8'))
        self.assertTrue(json_response['keyword'] == keyword_update['keyword'])

    def test_delete_keyword(self):
        # create a keyword
        Keyword.generate_fake(1)
        keyword = Keyword.query.first()

        # delete the keyword
        res = self.client.delete('/keywords/{uuid}'.format(uuid=keyword.uuid))
        self.assertTrue(204 == res.status_code)

        # check that the keyword has been deleted
        self.assertTrue(Keyword.query.filter_by(uuid=keyword.uuid).count() == 0)