from django.shortcuts import render, HttpResponse
from news.models import Article


def home(request):
    return render(request, "index.htm")


def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {"year": year, "article_list": a_list}
    return render(request, "year_archive.html", context)

def month_archive(request, year, month):
    a_list = Article.objects.filter(pub_date__month=month, pub_date__year=year)
    context = {"year": year, "month": month, "article_list": a_list}
    return render(request, "month_archive.html", context)

def article_detail(request, year, month, pk):
    a_list = Article.objects.filter(pub_date__month=month, pub_date__year=year, pk=pk)
    context = {"year": year, "month": month, "pk": pk, "article_list": a_list}
    return render(request, "article_detail.html", context)