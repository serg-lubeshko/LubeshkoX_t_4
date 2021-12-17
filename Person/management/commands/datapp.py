

from django.core.management.base import BaseCommand

from Course.models import Course, TeachCour, StudCour
from Person.management.data import user_data, course_data, teachcours_data, studcours_data
from Person.models import MyUser



class Command(BaseCommand):
    """ Класс для загрузки основных параметров проекта в БД """

    def handle(self, *args, **options):
        if MyUser.objects.all().count() == 0:
            for item_user in user_data.users_test:
                MyUser.objects.create_user(**item_user)

        if Course.objects.all().count() == 0:
            for item in course_data.course_test:
                Course.objects.create(**item)

        if TeachCour.objects.all().count() == 0:
            for item in teachcours_data.tcours_test:
                TeachCour.objects.create(**item)

        if StudCour.objects.all().count() == 0:
            for item in studcours_data.studcours_test:
                StudCour.objects.create(**item)