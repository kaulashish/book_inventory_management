from main.models import *
from django import forms


class SearchForm(forms.Form):
    search_book = forms.CharField(max_length=50)


class AddBookForm(forms.ModelForm):
    class Meta:
        model = StoreInventory
        fields = ["count"]


class CreateStoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = "__all__"
        exclude = ["user"]


class UpdateStoreForm(forms.ModelForm):
    class Meta:
        model = StoreInventory
        fields = "__all__"
        exclude = ["store"]
