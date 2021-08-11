from django import forms

from .models import Post

'''class ImageUploadForm (form.Forms):
    image = forms.ImageField()'''

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image',)