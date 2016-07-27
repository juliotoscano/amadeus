
from django.test import TestCase, Client
from django.core.urlresolvers import reverse

class courseCreate(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('createCourse')

    def test_course_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'courseForm.html')
        data = {
            'name':'Django para Zumbis',
            'slug':'DZ',
            'description':'Este curso e para zumbis',
            'qtd_available':'30',
            'qtd_students':'20',
            'teacher':'gileno',
            'category':'python'
            }
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('success' in response.context)

    def test_course_error(self):
        data ={
            'name':'Django para Zumbis',
            'slug':'DZ',
            'description':'Este curso e para zumbis',
            'qtd_available':'30',
            'qtd_students':'20',
            'teacher':'gileno',
        }
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('success' not in response.context)



