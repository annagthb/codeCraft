from django import forms
from .models import DefaultModel


# creating a form
class DefaultForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = DefaultModel

		# specify fields to be used
		fields = [
			"title",
			"description",
		]
