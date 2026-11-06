
from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = [
            'titulo',
            'contenido',
            'estado',
            'imagen',
        ]

        widgets = {
            'titulo': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'contenido': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 6}
            ),
            'estado': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'imagen': forms.ClearableFileInput(
                attrs={'class': 'form-control'}
            ),
        }
