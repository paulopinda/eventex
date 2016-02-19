from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class TestSubscriptionFormTest(TestCase):

	def setUp(self):
		self.form = SubscriptionForm()

	def test_form_has_fields(self):
		""" Form must have 4 fields. """
		expected = ['name', 'cpf', 'email', 'phone']
		self.assertSequenceEqual(expected, list(self.form.fields))


	# def test_cpf_is_digit(self):
	#	""" CPF must only accept digits """
	#	data = dict(name='Henrique Bastos', cpf='12345678901',
	#				email='henrique@bastos.net', phone='21-99618-6180')


	#	form = SubscriptionForm(data)
	#	form.is_valid()

	#	self.assertListEqual(['cpf'], list(form.errors))

