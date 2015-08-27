from django.test import TestCase
from apps.hello.models import Contacts
# Create your tests here.


class ContactsTest(TestCase):
    def setUp(self):
        Contacts.objects.create(name='igor', surname='shevchenko')
        Contacts.objects.create(name='igor', surname='shevchenko')
        Contacts.objects.create(name='igor', surname='shevchenko')

    def test_contact_check_count_row(self):
        "check count row"

    def test_contact_check_data(self):
        "check data from database"

    def test_create_record(self):
        "check create record"