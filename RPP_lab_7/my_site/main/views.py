from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
from django.core.cache import cache

from .models import *

def index(request):  #request - ссылка на сайт HttpRequest
    return render(request, 'main/index.html')


def tables(request):
    authors = Authors.objects.all()
    posts = Posts.objects.all()
    topics = Topics.objects.all()
    users = Users.objects.all()
    comments = Commentaries.objects.all()
    context = {
        'authors': authors,
        'comments': comments,
        'posts': posts,
        'topics': topics,
        'users': users,
    }
    return render(request, 'main/tables.html', context=context)

def change_tab(request):
    comments = Commentaries.objects.all()
    context = {
        'comments': comments,
    }
    if 'del' in request.GET:
        id_rec = request.GET.get('id_rec')
        del_rec = Commentaries.objects.get(id=id_rec)
        del_rec.delete()
        comments = Commentaries.objects.all()
    if 'up' in request.GET:
        id_rec = request.GET.get('id_rec')
        len_ps = str(len(Posts.objects.all()))
        len_us = str(len(Users.objects.all()))
        this_com = Commentaries.objects.get(id=id_rec)
        context = {
            'id_rec': id_rec,
            'this_com': this_com,
            'len_ps': len_ps,
            'len_us': len_us
        }
        return render(request, 'main/update_rec.html',  context=context)
    if 'cr' in request.GET:
        next_id = str(len(Commentaries.objects.all()) + 1)
        len_ps = str(len(Posts.objects.all()))
        len_us = str(len(Users.objects.all()))
        context = {
            'next_id': next_id,
            'len_ps': len_ps,
            'len_us': len_us
        }
        return render(request, 'main/create_rec.html', context = context)
    if 'update' in request.GET:
        id_rec = request.GET.get('id_rec')
        new_id_ps = request.GET.get('new_id_ps')
        new_id_us = request.GET.get('new_id_us')
        new_date = request.GET.get('new_date')
        new_text = request.GET.get('new_text')
        new_like = request.GET.get('new_like')
        if new_id_ps != "" and new_id_us != "" and new_date != "" and new_like != "":
            up_rec = Commentaries.objects.filter(id=id_rec)
            up_rec.update(id_post=new_id_ps)
            up_rec.update(id_user=new_id_us)
            up_rec.update(date=new_date)
            up_rec.update(text=new_text)
            up_rec.update(n_like=new_like)
    if 'create' in request.GET:
        next_id = request.GET.get('next_id')
        next_id_ps = request.GET.get('next_id_ps')
        next_id_us = request.GET.get('next_id_us')
        next_date = request.GET.get('next_date')
        next_text = request.GET.get('next_text')
        next_like = request.GET.get('next_like')
        if next_id_ps != "" and next_id_us != "" and next_date != "":
            Commentaries.objects.create(
                id_post_id=next_id_ps,
                id_user_id=next_id_us,
                date=next_date,
                text=next_text,
                n_like=next_like
            )
        comments = Commentaries.objects.all()

    cache.clear()
    return render(request, 'main/change_tab.html',  {'comments': comments })

def create_rec(request):
    comments = Commentaries.objects.all()
    len_comm = str(len(comments))

    context = {
        'comments': comments,
        'len_comm': len_comm,
    }
    return render(request, 'main/create_rec.html', context=context)


def update_rec(request):
    comments = Commentaries.objects.all()
    len_comm = str(len(comments))
    context = {
        'comments': comments,
        'len_comm': len_comm,
    }
    return render(request, 'main/update_rec.html', context=context)
