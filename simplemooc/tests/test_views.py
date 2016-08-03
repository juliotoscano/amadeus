
from django.test import TestCase, Client
from django.core.urlresolvers import reverse

class courseCreate(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('simplemooc:createCourse')

    def test_course_ok(self):
       response = self.client.get(self.url)
       self.assertEquals(response.status_code, 200)
       self.assertTemplateUsed(response, 'courseForm.html')
       data = {'name': 'Django para Zumbis', 'slug': 'DZ', 'description': 'Este curso e para zumbis', 'program': 'Esta e a programacao', 'qtd_available': '30', 'qtd_students': '20', 'begin_matric': ' ', 'end_matric': ' ', 'begin_course': ' ', 'end_course': ' ', 'image': ' ', 'is_approved': ' ', 'teacher': 'Gileno', 'category': 'Python', 'modules': 'Desenvolvendo uma aplicacao Web', 'keywords': 'Python'}
       response = self.client.post(self.url, data)
       self.assertEquals(response.status_code, 200)
       self.assertTrue('success' in response.context)

    def test_course_error(self):
        data = {'name': 'Django para Zumbis', 'slug': 'DZ', 'description': 'Este curso e para zumbis', 'qtd_available': '30', 'qtd_students': '20', 'teacher': 'Gileno', 'category': 'Python', 'modules': 'Desenvolvendo uma aplicacao Web'}
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('success' not in response.context)


