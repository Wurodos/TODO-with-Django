from django import forms


class TaskForm(forms.Form):
    title_field = forms.CharField(label="Название", max_length=30)
    desc_field = forms.CharField(label="Описание")
    color_picker = forms.CharField(label="Цвет", max_length=10)