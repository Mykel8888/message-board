from django.test import TestCase

# Create your tests here.

from .models import Post

class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post=Post.objects.create(text='life is not in favour to lazy')

    def test_model_content(self):
        self.assertEqual(self.post.text, 'life is not in favour to lazy')