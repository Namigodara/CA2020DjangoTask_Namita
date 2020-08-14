from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()  # get all records from Aritcle
    data = {
        "articles": articles,
    }
    return render( request, "index.html",data)

def detail(request, article_id):
    article = Article.objects.get(pk = article_id)
    data = {
        "article":article,
    }
    return render(request, "detail.html", data)

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

