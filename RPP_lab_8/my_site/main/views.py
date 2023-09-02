from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.db import models
from django.core.cache import cache
from django.views import View
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.db.models import ProtectedError

from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import *

from main.forms import UserCreationForm

users2 = User.objects.all()
authors = Authors.objects.all()
posts = Posts.objects.all()
topics = Topics.objects.all()
users = Users.objects.all()
comments = Commentaries.objects.all()

list_aut = ['ID', 'Посты', 'Просмотры', 'Лайки']
list_com = ['ID', 'ID поста', 'ID пользователя', 'Дата', 'Содержание', 'Лайки']
list_post = ['ID', 'Дата поста', 'Просмотры', 'Лайки', 'Комментарии', 'ID автора', 'ID тема']
list_top = ['ID', 'Название', 'Дата создания', 'Посты', 'Просмотры', 'Лайки']
list_us = ['ID', 'Фамилия', 'Имя', 'Отчество', 'Ник', 'Дата рождения', 'Дата регистрации']

error_access = "Вы не обладаете достаточными правами для данного действия"

def tables(request):
    context = {
        'list_aut': list_aut,
        'list_com': list_com,
        'list_post': list_post,
        'list_top': list_top,
        'list_us': list_us,
        'authors': authors,
        'comments': comments,
        'posts': posts,
        'topics': topics,
        'users': users,
    }
    return render(request, 'home.html', context)

context1 = {'tb': 1, 'name': 'Пользователи', 'table': users, 'list': list_us}
context2 = {'tb': 2, 'name': 'Посты', 'table': posts, 'list': list_post}
context3 = {'tb': 3, 'name': 'Темы обсуждения', 'table': topics, 'list': list_top}
context4 = {'tb': 4, 'name': 'Авторы', 'table': authors, 'list': list_aut}
context5 = {'tb': 5, 'name': 'Комментарии', 'table': comments, 'list': list_com}
class Tabs(View):

    # Страницы редактирования сущностей
    def in_users(request):
        return render(request, 'tabs/edit.html', context=context1)

    def in_posts(request):
        return render(request, 'tabs/edit.html', context=context2)

    def in_topics(request):
        return render(request, 'tabs/edit.html', context=context3)

    def in_authors(request):
        return render(request, 'tabs/edit.html', context=context4)

    def in_comments(request):
        return render(request, 'tabs/edit.html', context=context5)


    def delete(request, tb, id):
        error = False
        if tb == 1:
            context = context1
            if request.user.has_perm('main.delete_users'):
                record = Users.objects.get(id=id)
            else:
                error = True
        elif tb == 2:
            context = context2
            if request.user.has_perm('main.delete_posts'):
                record = Posts.objects.get(id=id)
            else:
                error = True
        elif tb == 3:
            context = context3
            if request.user.has_perm('main.delete_topics'):
                record = Topics.objects.get(id=id)
            else:
                error = True
        elif tb == 4:
            context = context4
            if request.user.has_perm('main.delete_authors'):
                record = Authors.objects.get(id_user=id)
            else:
                error = True
        else:
            context = context5
            if request.user.has_perm('main.delete_commentaries'):
                record = Commentaries.objects.get(id=id)
            else:
                error = True
        if error:
            context['error'] = error_access
            return render(request, 'tabs/edit.html', context=context)
        try:
            record.delete()
        except ProtectedError:
            context['error'] = 'Удаление записи с ID ' + str(id) + ' невозможно, так как запись является вторичным ключом для других записей'
            return render(request, 'tabs/edit.html', context=context)

        if tb == 1:
            context1['table'] = Users.objects.all()
            return redirect('users')
        elif tb == 2:
            context2['table'] = Posts.objects.all()
            return redirect('posts')
        elif tb == 3:
            context3['table'] = Topics.objects.all()
            return redirect('topics')
        elif tb == 4:
            context4['table'] = Authors.objects.all()
            return redirect('authors')
        else:
            context5['table'] = Commentaries.objects.all()
            return redirect('comments')

    def update(request, tb, id):
        error = False
        if tb == 1:
            context = context1
            if request.user.has_perm('main.change_users'):
                record = Users.objects.get(id=id)
            else:
                error = True
        elif tb == 2:
            context = context2
            if request.user.has_perm('main.change_posts'):
                record = Posts.objects.get(id=id)
                context['aut'] = record.id_author.values_list('id_user', flat=True)
                context['top'] = record.id_topic.values_list('id', flat=True)
                context['list_a'] = authors.values_list('id_user', flat=True)
                context['list_t'] = topics.values_list('id', flat=True)
            else:
                error = True
        elif tb == 3:
            context = context3
            if request.user.has_perm('main.change_topics'):
                record = Topics.objects.get(id=id)
            else:
                error = True
        elif tb == 4:
            context = context4
            if request.user.has_perm('main.change_authors'):
                record = Authors.objects.get(id_user=id)
            else:
                error = True
        else:
            context = context5
            if request.user.has_perm('main.change_commentaries'):
                record = Commentaries.objects.get(id=id)
                context['list_ps'] = posts.values_list('id', flat=True)
                context['list_us'] = users.values_list('id', flat=True)
            else:
                error = True
        if error:
            context['error'] = error_access
            return render(request, 'tabs/edit.html', context=context)
        if tb != 4:
            context['id'] = id
        else:
            context['id'] = record.id_user.id
        context['r'] = record
        return render(request, 'tabs/update.html', context=context)

    def save(request, tb, new_id):
        if tb == 1:
            try:
                us = Users.objects.get(id=new_id)
            except Users.DoesNotExist:
                us = Users(id=new_id)
        elif tb == 2:
            try:
                ps = Posts.objects.get(id=new_id)
            except Posts.DoesNotExist:
                ps = Posts(id=new_id)
        elif tb == 3:
            try:
                tp = Topics.objects.get(id=new_id)
            except Topics.DoesNotExist:
                tp = Topics(id=new_id)
        elif tb == 4:
            if new_id:
                at = Authors.objects.get(id_user=new_id)
            else:
                at = Authors()
                at.id_user_id = request.POST.get("id_user")
        else:
            try:
                cm = Commentaries.objects.get(id=new_id)
            except Commentaries.DoesNotExist:
                cm = Commentaries(id=new_id)

        if request.method == "POST":
            if tb == 1:
                us.surname = request.POST.get("surname")
                us.name = request.POST.get("name")
                us.pat_name = request.POST.get("pat_name")
                us.nick = request.POST.get("nick")
                us.date_reg = request.POST.get("date_reg")
                us.date_b = request.POST.get("date_b")
                us.save()
                context = context1
                context['table'] = Users.objects.all()
                return redirect('users')
            elif tb == 2:
                ps.date_post = request.POST.get("date_post")
                ps.n_view = request.POST.get("n_view")
                ps.n_like = request.POST.get("n_like")
                ps.n_comm = request.POST.get("n_comm")
                ps.save()
                ps.id_author.clear()
                aut_s = request.POST.getlist("au_s[]")
                for a in aut_s:
                    aut = Authors.objects.get(id_user=a)
                    ps.id_author.add(aut)
                ps.id_topic.clear()
                top_s = request.POST.getlist("top_s[]")
                for t in top_s:
                    top = Topics.objects.get(id=t)
                    ps.id_topic.add(top)
                ps.save()
                context = context2
                context['table'] = Posts.objects.all()
                return redirect('posts')
            elif tb == 3:
                tp.name_t = request.POST.get("name_t")
                tp.date_cr = request.POST.get("date_cr")
                tp.n_post = request.POST.get("n_post")
                tp.n_view = request.POST.get("n_view")
                tp.n_like = request.POST.get("n_like")
                tp.save()
                context = context3
                context['table'] = Topics.objects.all()
                return redirect('topics')
            elif tb == 4:
                at.n_post = request.POST.get("n_post")
                at.n_view = request.POST.get("n_view")
                at.n_like = request.POST.get("n_like")
                at.save()
                context = context4
                context['table'] = Authors.objects.all()
                return redirect('authors')
            else:
                cm.id_post_id = request.POST.get("id_post")
                cm.id_user_id = request.POST.get("id_user")
                cm.date = request.POST.get("date")
                cm.text = request.POST.get("text")
                cm.n_like = request.POST.get("n_like")
                cm.save()
                context = context5
                context['table'] = Commentaries.objects.all()
                return redirect('comments')
        else:
            if tb == 1:
                redirect('users')
            elif tb == 2:
                redirect('posts')
            elif tb == 3:
                redirect('topics')
            elif tb == 4:
                redirect('authors')
            else:
                redirect('comments')



    def create(request, tb):
        error = False
        if tb == 1:
            context = context1
            if request.user.has_perm('main.add_users'):
                try:
                    user = Users.objects.order_by('id').last()
                    context['new_id'] = user.id + 1
                except AttributeError:
                    context['new_id'] = 1
            else:
                error = True
        elif tb == 2:
            context = context2
            if request.user.has_perm('main.add_posts'):
                context['list_a'] = authors.values_list('id_user', flat=True)
                context['list_t'] = topics.values_list('id', flat=True)
                try:
                    post = Posts.objects.order_by('id').last()
                    context['new_id'] = post.id + 1
                except AttributeError:
                    context['new_id'] = 1
            else:
                error = True
        elif tb == 3:
            context = context3
            if request.user.has_perm('main.add_topics'):
                try:
                    topic = Topics.objects.order_by('id').last()
                    context['new_id'] = topic.id + 1
                except AttributeError:
                    context['new_id'] = 1
            else:
                error = True
        elif tb == 4:
            context = context4
            if request.user.has_perm('main.add_authors'):
                list_id = []
                id_au = authors.values_list('id_user', flat=True)
                for u in users2.values_list('id', flat=True):
                    if not(u in id_au):
                        list_id.append(u)
                context['list_id'] = list_id
                context['new_id'] = 0
            else:
                error = True
        else:
            context = context5
            if request.user.has_perm('main.add_commentaries'):
                try:
                    comm = Commentaries.objects.order_by('id').last()
                    context['list_ps'] = posts.values_list('id', flat=True)
                    context['list_us'] = users.values_list('id', flat=True)
                    context['new_id'] = comm.id + 1
                except AttributeError:
                    context['new_id'] = 1
            else:
                error = True
        if error:
            context['error'] = error_access
            return render(request, 'tabs/edit.html', context=context)
        return render(request, 'tabs/create.html', context=context)



class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)








