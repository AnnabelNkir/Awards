from django.test import TestCase
from .models import *
import datetime as dt

# Create your tests here.
class ProfileTestClass(TestCase):

    def setUp(self):
        self.Pro= Profile(name = 'Jeff', bio='Made with love')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Pro,Profile))

    def test_save_method(self):
        self.Pro.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_data(self):
        self.assertTrue(self.Pro.name,"test")

    def test_delete(self):
        post = Profile.objects.filter(id=1)
        post.delete()
        posts = Profile.objects.all()
        self.assertTrue(len(posts)==0)

    def test_get_post_by_id(self):
        self.Pro.save()
        posts = Profile.objects.get(id=1)
        self.assertTrue(posts.name,'kol')

class ProjectsTestClass(TestCase):

    def setUp(self):
        self.Pro= Projects(name = 'Jeff', description='Made with love')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Pro,Projects))

    def test_save_method(self):
        self.Pro.save_project()
        project = Projects.objects.all()
        self.assertTrue(len(project) > 0)

    def test_data(self):
        self.assertTrue(self.Pro.name,"test")

    def test_delete(self):
        post = Projects.objects.filter(id=1)
        post.delete()
        posts = Projects.objects.all()
        self.assertTrue(len(posts)==0)

    def test_get_post_by_id(self):
        self.Pro.save()
        posts = Projects.objects.get(id=1)
        self.assertTrue(posts.name,'kol')



class CommentTestClass(TestCase):

    def setUp(self):
        self.Com= Comment(comment='Made with love')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Com,Comment))

    def test_save_method(self):
        self.Com.save_comment()
        comment = Comment.objects.all()
        self.assertTrue(len(comment) > 0)

    def test_data(self):
        self.assertTrue(self.Com.comment,"test")

    def test_delete(self):
        post = Comment.objects.filter(id=1)
        post.delete()
        posts = Comment.objects.all()
        self.assertTrue(len(posts)==0)

    def test_get_post_by_id(self):
        self.Com.save()
        posts = Comment.objects.get(id=1)
        self.assertTrue(posts.comment,'kol')


class RateTestClass(TestCase):

    def setUp(self):
        self.Rat= Rates(design='10')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Rat,Rates))

   