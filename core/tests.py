from django.test import TestCase
from django.contrib.auth import get_user_model

from . import models


class BasicTests(TestCase):

    def test_create_new_user(self):
        """ Test creating a new user """
        username = 'test'
        password = 'test@123456'
        user = get_user_model().objects.create_user(
            username=username,
            password=password
        )

        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))


class ChoiceModelTest(TestCase):
    """ Test creating a new choice """
    def setUp(self):
        models.Choice.objects.create(
            title='Test'
        )

    def test_object_name_is_title(self):
        choice = models.Choice.objects.get(id=1)
        self.assertEqual(str(choice), f'{choice.title}')


class QuestionModelTest(TestCase):
    """ Test creating a new question """
    def setUp(self):
        choice_one = models.Choice.objects.create(
            title='Test'
        )
        choice_two = models.Choice.objects.create(
            title='Test Two'
        )
        choice_three = models.Choice.objects.create(
            title='Test Three'
        )
        choice_four = models.Choice.objects.create(
            title='Test Four'
        )
        models.Question.objects.create(
            title='Test',
            correct_answer=2,
            choice_one=choice_one,
            choice_two=choice_two,
            choice_three=choice_three,
            choice_four=choice_four
        )

    def test_object_name_is_title(self):
        question = models.Question.objects.get(id=1)
        self.assertEqual(str(question), f'{question.title}')


class ExamModelTest(TestCase):
    """ Test creating a new exam """
    def setUp(self):
        choice_one = models.Choice.objects.create(
            title='Test'
        )
        choice_two = models.Choice.objects.create(
            title='Test Two'
        )
        choice_three = models.Choice.objects.create(
            title='Test Three'
        )
        choice_four = models.Choice.objects.create(
            title='Test Four'
        )
        question = models.Question.objects.create(
            title='Test',
            correct_answer=2,
            choice_one=choice_one,
            choice_two=choice_two,
            choice_three=choice_three,
            choice_four=choice_four
        )
        exam = models.Exam.objects.create(
            title='Test'
        )
        exam.questions.add(question)

    def test_object_name_is_title(self):
        exam = models.Exam.objects.get(id=1)
        self.assertEqual(str(exam), f'{exam.title}')


class CourseModelTest(TestCase):
    """ Test creating a new course """
    def setUp(self):
        choice_one = models.Choice.objects.create(
            title='Test'
        )
        choice_two = models.Choice.objects.create(
            title='Test Two'
        )
        choice_three = models.Choice.objects.create(
            title='Test Three'
        )
        choice_four = models.Choice.objects.create(
            title='Test Four'
        )
        question = models.Question.objects.create(
            title='Test',
            correct_answer=2,
            choice_one=choice_one,
            choice_two=choice_two,
            choice_three=choice_three,
            choice_four=choice_four
        )
        exam = models.Exam.objects.create(
            title='Test'
        )
        exam.questions.add(question)
        models.Course.objects.create(
            title='Test',
            description='description',
            content='content',
            exam=exam
        )

    def test_object_name_is_title(self):
        course = models.Course.objects.get(id=1)
        self.assertEqual(str(course), f'{course.title}')
