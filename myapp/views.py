from django.shortcuts import render

from django.shortcuts import render

# home_view,about_view,chocolate_view,contact_view

def home_view(request):
    return render(request,"index.html")

def about_view(request):
    return render(request,"about.html")

def dukon_view(request):
    return render(request,"product.html")

def contact_view(request):
    return render(request,"contact.html")



from django.shortcuts import render,HttpResponseRedirect
#300,301,302
from .models import Article,Comment
from django.contrib import messages  # new
from django.urls import reverse  # new

from .forms import ArticleForm,CommentForm


def home(request):
    articles = Article.objects.filter(is_active=True).order_by("-id")[:3]
    context = {"articles":articles}
    return render(request,"about.html",context)

def main(request):
    articles = Article.objects.filter(is_active=True).order_by("-id")
    context = {"articles":articles}
    return render(request,"index.html",context)


def main(request):
    articles = Article.objects.filter(is_active=True).order_by("-id")
    context = {"articles":articles}
    return render(request,"contact.html",context)

def main(request):
    articles = Article.objects.filter(is_active=True).order_by("-id")
    context = {"articles":articles}
    return render(request,"product.html",context)


def main(request):
    articles = Article.objects.filter(is_active=True).order_by("-id")
    context = {"articles":articles}
    return render(request,"testimonial.html",context)




def article_detail(request,id):
    article = Article.objects.get(id=id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            first_name = form.data["first_name"]
            text = form.data["text"]
        
            comment = Comment(
                first_name=first_name,
                text=text,
                article=article
            )
            comment.save()
            messages.success(request, 'Izoh yuborildi')


    
    comments = Comment.objects.filter(article=id)
    form = CommentForm()
    context = {"about":article,"comments":comments,"form":form}
    return render(request,"about.html",context)


def create_article(request):

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']

            article = Article(
                title=title,
                description=description,
                image=image,
            )
            article.save()
            messages.success(request, '🥳 Maqolangiz adminga yuborildi, tekshiruvdan so\'ng chop etiladi')
            return HttpResponseRedirect(reverse('articles-list'))
        else:
            messages.error(request, 'Formani qaytadan to\'ldiring')
    else:
        form = ArticleForm()
    context = {"form": form}
    
    return render(request, "create_article.html", context)