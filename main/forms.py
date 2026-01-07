from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "body"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Your name",
                    "maxlength": 80,
                    "class": (
                        "w-full rounded-md border border-neutral-700 "
                        "bg-[#010e28] px-3 py-2 text-neutral-100 "
                        "placeholder:text-neutral-500 focus:border-blue-500 "
                        "focus:outline-none focus:ring-2 focus:ring-blue-500/30"
                    ),
                }
            ),
            "body": forms.Textarea(
                attrs={
                    "placeholder": "Write a comment",
                    "rows": 5,
                    "maxlength": 1000,
                    "class": (
                        "w-full rounded-md border border-neutral-700 "
                        "bg-[#010e28] px-3 py-2 text-neutral-100 "
                        "placeholder:text-neutral-500 focus:border-blue-500 "
                        "focus:outline-none focus:ring-2 focus:ring-blue-500/30"
                    ),
                }
            ),
        }
