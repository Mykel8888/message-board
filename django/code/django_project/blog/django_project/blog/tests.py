from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
from django.urls import reverse


# Create your tests here.

class BlogTest(TestCase):
    @classmethod
    def setUpClass(cls):
       cls.user = get_user_model().objects.create_user(username='testuser',email='test@email.com',password="secrete") # to get user test
       cls.Post = Post.objects.create(title='life of a man', body = 'you dont give up on your dream', author=cls.user,)
    #tested individual post
    def test_post_model(self):
        self.assertEqual(self.Post.title,"life of a man")
        self.assertEqual(self.Post.body,"you dont give up on your dream")
        self.assertEqual(self.Post.author.username,"testuser")
        self.assertEqual(str(self.Post),'life of a man')
        self.assertEqual(self.Post.get_absolute_url(),'/post/1/') #test the refering url
    
    def test_url_exist_at_correct_location_listview(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_exist_at_correct_location_detailview(self):
        response = self.client.get('/post/1/')
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'life of a man')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_details_view(self):
        response =self.client.get(reverse('post_detail', kwargs={'pk':self.Post.pk}))
        no_response=self.client.get('/Post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'life of a man')
        self.assertTemplateUsed(response, 'post_detail.html')




