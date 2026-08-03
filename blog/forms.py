from django import forms
from .models import Post


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, label="نام", widget=forms.TextInput(attrs={"placeholder": "نام را وارد نمائید"})
    )
    email = forms.EmailField(label="ایمیل")
    subject = forms.CharField(max_length=200, label="موضوع")
    message = forms.CharField(label="پیام", widget=forms.Textarea(attrs={"rows": 5}))

    def clean_message(self):
        message = self.cleaned_data["message"]
        if len(message) < 20:

            raise forms.ValidationError("پیام باید حداقل 20 کاراکتر داشته باشد")
        return message

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name", "")
        email = cleaned_data.get("email", "")
        if name and email and name.lower() in email.lower():
            raise forms.ValidationError("ایمیل نباید شامل نام باشد")

        return cleaned_data


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "is_published"]
        # fields = "__all__"
        exclude = ["created_at"]
        labels = {
            "title": "عنوان پست",
            "content": "محتوا",
            "is_published": "منتشر شد؟",
        }
        widgets = {"title": forms.TextInput(attrs={"placeolder": "عنوان پست را وارد نمائید", "class": "form-control"})}
        def clean_title(self):
            title = self.clean_data['title']
            