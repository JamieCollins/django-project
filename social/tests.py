from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Post, Comment


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Technology', slug='technology')

    def test_category_name(self):
        self.assertEqual(self.category.name, 'Technology')
    
    def test_category_slug(self):
        self.assertEqual(self.category.slug, 'technology')


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name='Technology', slug='technology')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            excerpt='This is a test post.',
            content='Lorem ipsum dolor sit amet.',
            category=self.category
        )
    
    def test_post_title(self):
        self.assertEqual(self.post.title, 'Test Post')
    
    def test_post_slug(self):
        self.assertEqual(self.post.slug, 'test-post')
    
    def test_post_author(self):
        self.assertEqual(self.post.author, self.user)
    
    def test_post_excerpt(self):
        self.assertEqual(self.post.excerpt, 'This is a test post.')
    
    def test_post_content(self):
        self.assertEqual(self.post.content, 'Lorem ipsum dolor sit amet.')
    
    def test_post_category(self):
        self.assertEqual(self.post.category, self.category)
    
    def test_number_of_likes(self):
        self.assertEqual(self.post.number_of_likes(), 0)


class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name='Technology', slug='technology')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            excerpt='This is a test post.',
            content='Lorem ipsum dolor sit amet.',
            category=self.category
        )
        self.comment = Comment.objects.create(
            post=self.post,
            name='John Doe',
            email='johndoe@example.com',
            body='This is a test comment.',
            approved=True
        )
    
    def test_comment_post(self):
        self.assertEqual(self.comment.post, self.post)
    
    def test_comment_name(self):
        self.assertEqual(self.comment.name, 'John Doe')
    
    def test_comment_email(self):
        self.assertEqual(self.comment.email, 'johndoe@example.com')
    
    def test_comment_body(self):
        self.assertEqual(self.comment.body, 'This is a test comment.')
    
    def test_comment_approved(self):
        self.assertTrue(self.comment.approved)
