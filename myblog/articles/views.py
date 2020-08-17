from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from .models import Article
from .forms import ArticleForm
from .forms import SignUpForm

# Create your views here.
def home(request):
    return render( request, "home.html")

@login_required
def index(request):
    articles = Article.objects.all()  # get all records from Aritcle
    data = {
        "articles": articles,
    }
    return render( request, "index.html",data)

@login_required
def detail(request, article_id):
    article = Article.objects.get(pk = article_id)
    data = {
        "article":article,
    }
    return render(request, "detail.html", data)

@login_required
def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save(commit=False)
        article.save()
        form = ArticleForm()
    data = {
        "form": form,
    }
    return render(request,"create.html",data)


@login_required
def update (request, article_id):
    article = Article.objects.get(pk = article_id)
    form =ArticleForm(request.POST or None, instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        article.save()
    data = {
        "article": article,
        "form": form,
    }
    return render(request,'create.html',data)

def delete (request, article_id = None):
    article = Article.objects.get(pk = article_id)
    article.delete()
    return redirect('index')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned.data.get('username')
            raw_password = form.cleaned.data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    data = {
        "form": form,
    }
    return render(request, 'signup.html', data)

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {
#         'form': form
#     })





