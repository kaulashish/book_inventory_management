from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
import requests

# Create your views here.
class Login(LoginView):
    template_name = "login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("homepage")


class Register(FormView):
    template_name = "signup.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)


class HomePage(LoginRequiredMixin, View):
    def get(self, request):
        stores = Store.objects.filter(user=request.user)
        context = {"stores": stores}
        return render(request, "home.html", context)


class AddStore(LoginRequiredMixin, View):
    def get(self, request):
        form = CreateStoreForm()
        context = {"form": form}
        return render(request, "addstore.html", context)

    def post(self, request):
        form = CreateStoreForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
        return redirect("homepage")


class StoreView(LoginRequiredMixin, View):
    def get(self, request, pk):
        store_obj = Store.objects.get(id=pk)
        store_inventory = StoreInventory.objects.filter(store=store_obj)
        context = {"store": store_obj, "store_inventory": store_inventory}
        return render(request, "storeview.html", context)


class SearchBook(LoginRequiredMixin, View):
    def get(self, request, pk):
        form = SearchForm()
        context = {"form": form, "store_id": pk}
        return render(request, "index.html", context)

    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)
        storeid = request.GET["storeid"]
        if form.is_valid():
            search_query = self.request.POST.get("search_book").replace(" ", "-")
            response = requests.get(
                f"https://www.googleapis.com/books/v1/volumes?q={search_query}&startIndex=0&maxResults=5"
            ).json()
        context = {"form": form, "books": response["items"], "store_id": storeid}
        return render(request, "index.html", context)


class BookInfo(LoginRequiredMixin, View):
    def get(self, request):
        try:
            book_id = request.GET["q"]
            store_id = request.GET["storeid"]
            response = requests.get(
                f"https://www.googleapis.com/books/v1/volumes/{book_id}"
            ).json()
            context = {"book_info": response, "store_id": store_id}
            return render(request, "bookinfo.html", context)
        except:
            book_id = request.GET["q"]
            inventory_obj = StoreInventory.objects.get(id=int(request.GET["id"]))
            response = requests.get(
                f"https://www.googleapis.com/books/v1/volumes/{book_id}"
            ).json()
            error_txt = "(this button will not work now)"
            count_html = f"<u><p><b>Book Count:</b> {inventory_obj.count} books in inventory<p></u>"
            context = {
                "book_info": response,
                "error_txt": error_txt,
                "count_html": count_html,
            }
            return render(request, "bookinfo.html", context)


class BookAdd(LoginRequiredMixin, View):
    def get(self, request):
        form = AddBookForm()
        context = {"form": form}
        return render(request, "addbook.html", context)

    def post(self, request, *args, **kwargs):
        form = AddBookForm(request.POST)
        store_id = request.GET["storeid"]
        store_obj = Store.objects.get(id=store_id)
        book_id = request.GET["q"]
        response = requests.get(
            f"https://www.googleapis.com/books/v1/volumes/{book_id}"
        ).json()
        book = response["volumeInfo"]["title"]
        author = ", ".join(response["volumeInfo"]["authors"])
        google_id = response["id"]
        isbn = response["volumeInfo"]["industryIdentifiers"][0]["identifier"]

        form.instance.store = store_obj
        form.instance.book = book
        form.instance.author = author
        form.instance.google_id = google_id
        form.instance.isbn = isbn

        if form.is_valid():
            form.save()
            return redirect("store-view", pk=store_id)
        else:
            print(form.errors)


class DeleteInventoryItem(LoginRequiredMixin, View):
    def get(self, request, pk):
        store_id = request.GET["storeid"]
        item = StoreInventory.objects.get(id=pk)
        item.delete()
        return redirect("store-view", pk=store_id)


class EditInventoryItem(LoginRequiredMixin, View):
    def get(self, request, pk):
        obj = StoreInventory.objects.get(id=pk)
        form = UpdateStoreForm(instance=obj)
        context = {"form": form}
        return render(request, "updateinventory.html", context)

    def post(self, request, pk):
        store_id = int(request.GET["storeid"])
        obj = StoreInventory.objects.get(id=pk)
        form = UpdateStoreForm(request.POST, instance=obj)
        form.instance.store = Store.objects.get(id=store_id)
        if form.is_valid():
            form.save()
            return redirect("store-view", pk=store_id)
        else:
            print(form.errors)

        context = {"form": form}

        return render(request, "updateinventory.html", context)
