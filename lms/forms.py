from django import forms
from lms.models import Question,Answer

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['question']