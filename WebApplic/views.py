from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from WebApplic.models import Post, Comment, Title
from WebApplic.forms import CommentForm
from django.template.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator
import time

# Create your views here.
def basic_one(request):
    view = "basic_one"
    html = "<html><body> This is %s view</body></html>" % view
    return HttpResponse(html)

def template_two(request):
    view = "template_two"
    t = get_template('myview.html')
    html = t.render(Context({'name' : view}))
    return HttpResponse(html)

def template_three_simple(request):
    view = "template three"
    return render_to_response('myview.html', {'name' : view})

def posts(request, page_number=1):
    all_posts = Post.objects.all()
    pages = Paginator(all_posts, 2)
    return render_to_response('posts.html', {'posts': pages.page(page_number), 'username': auth.get_user(request).username})

def post(request, post_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['post'] = Post.objects.get(id=post_id)
    args['comments'] = Comment.objects.filter(post_id=post_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return  render_to_response('post.html', args)

def title_settings(request):
    return render_to_response('title.html', {'title': Title.objects.get(id=1)})

def addlike(request, post_id, page_id):
    try:
        if post_id in request.COOKIES:
            return redirect('http://127.0.0.1:8000/allposts/%s/' % page_id)
        else:
            post = Post.objects.get(id=post_id)
            post.likes += 1
            post.save()
            response = redirect('http://127.0.0.1:8000/allposts/%s/' % page_id)
            response.set_cookie(post_id, 'test')
        return response
    except:
        raise Http404

def addcomment(request, post_id):
    if request.POST and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(id=post_id)
            comment.author = auth.get_user(request)
            comment.date = time.strftime("%Y-%m-%d %H:%M")
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('http://127.0.0.1:8000/posts/get/%s' % post_id)