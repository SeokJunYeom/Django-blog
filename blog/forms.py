from django.forms import ModelForm
from .models import Character

class CharacterForm(ModelForm):
	class Meta:
		model = Character
		fields = [ 'id', 'image', 'name', 'birth', 'stature', 'blood_type' ]