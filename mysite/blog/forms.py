from django import forms

from blog.models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment #указываем, на основе какйо модели будем делать форму
        fields = ['name', 'email', 'body'] #указываем, какие поля будут у формы