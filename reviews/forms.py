from django import forms
from reviews.models import Ticket, Review


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        labels = {
            'title': 'Titre',
            'description': 'Description',
            'image': 'Image'
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
        labels = {
            'headline': 'Titre de votre critique',
            'rating': 'Note (0 à 5)',
            'body': 'Commentaire',
        }
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, str(i)) for i in range(6)]),
            'body': forms.Textarea(attrs={'rows': 4}),
        }


class FollowUserForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur', max_length=150)
