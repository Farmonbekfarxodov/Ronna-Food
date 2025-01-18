from django import forms

from blogs.models import BlogCommentModel


class BlogCommentModelForm(forms.ModelForm):
    class Meta:
        model=BlogCommentModel
        fields = ['comment']