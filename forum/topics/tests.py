from django.test import TestCase
from .models import Topic


def add(x, y):
    return x + y

class A:
    a = 1

a = A()

def f(x):
    return a.a * x


class TestAdd(TestCase):
    fixtures = ['test']

    def test_add(self):
        self.assertEqual(Topic.objects.count(), 2, "Add failed")
