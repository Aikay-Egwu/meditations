from django import forms

class AddRhemaForm(forms.Form):
  title = forms.CharField(label='Title', max_length=200)
  verse = forms.CharField(label='Bible Verse', max_length=100, required=False)
  bible_text = forms.CharField(label='Bible Text', required=False)
  notes = forms.CharField(label='Notes')