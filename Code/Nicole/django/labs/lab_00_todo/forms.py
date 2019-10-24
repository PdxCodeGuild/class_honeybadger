from django import forms


class ToDoForm(forms.Form):
    todo_text = forms.CharField(label='Todo Text', max_length=100)
