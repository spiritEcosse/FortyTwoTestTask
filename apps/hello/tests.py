from django.test import TestCase
from apps.hello.models import Contacts
# Create your tests here.


class ContactsTest(TestCase):
    def setUp(self):
        Contacts.objects.create(name='igor', surname='shevchenko')
        Contacts.objects.create(name='igor1', surname='shevchenko1')
        Contacts.objects.create(name='igor2', surname='shevchenko2')

    def test_contact_check_count_row(self):
        "check count row"
        contacts = Contacts.objects.all()
        self.assertEqual(contacts.count(), 2)

    def test_contact_check_data_name(self):
        "check data from database"
        contact = Contacts.objects.get(name='igor')
        self.assertEqual(contact.name, 'some name')

    def test_contact_check_data_surname(self):
        "check data from database"
        contact = Contacts.objects.get(surname='shevchenko1')
        self.assertEqual(contact.surname, 'some last name')