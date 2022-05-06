from unicodedata import category
from notification.models import Notification
from django.core.checks import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Categorylb, Categoryleetcode, Comment, Commentcpp, Commentjava, Commentlb, Commentleetcode, Commentpython, Post, Postcpp, Postjava, Postlb, Postleetcode, Postpython,Categorycpp,Categoryjava,Categorypython
from .forms import CommentForm, CommentFormcpp, CommentFormjava, CommentFormlb, CommentFormleetcode, CommentFormpython,PostForm, PostFormPython, PostFormcpp, PostFormjava, PostFormlb, PostFormleetcode
from django.http import HttpResponseRedirect, JsonResponse
from users.models import Profile
from itertools import chain
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
import random
from .models import Post

from django.shortcuts import render
def cut(request,post_id):
    title = get_object_or_404(Post, pk=request.GET.get('post_id'))
    title.complete = True
    title.save()
    return redirect('ba')

def uncut(request,post_id):
    title = get_object_or_404(Post, pk=request.GET.get('post_id'))
    title.complete = False
    title.save()
    return redirect('ba')


from django.http import HttpResponse
from .models import Post

from django.http import JsonResponse


def toggle_note_clear(request):
    post = get_object_or_404(Post, pk=request.GET.get('post_id'))
    post.is_working = not post.is_working
    post.save()
    return redirect('post:detail')

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

""" Home page with all posts """
def first(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/first.html', context)

""" Posts of following user profiles """
@login_required
def posts_of_following_profiles(request):

    profile = Profile.objects.get(user = request.user)
    users = [user for user in profile.following.all()]
    posts = []
    qs = None
    for u in users:
        p = Profile.objects.get(user=u)
        p_posts = p.user.post_set.all()
        posts.append(p_posts)
    my_posts = profile.profile_posts()
    posts.append(my_posts)
    if len(posts)>0:
        qs = sorted(chain(*posts), reverse=True, key=lambda obj:obj.date_posted)

    paginator = Paginator(qs, 5)
    page = request.GET.get('page')
    try:
        posts_list = paginator.page(page)
    except PageNotAnInteger:
        posts_list = paginator.page(1)
    except EmptyPage:
        posts_list = paginator.page(paginator.num_pages)
  
    return render(request,'blog/feeds.html',{'profile':profile,'posts':posts_list})


""" Post Like """
@login_required
def LikeView(request):

    post = get_object_or_404(Post, id=request.POST.get('id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
        notify = Notification.objects.filter(post=post, sender=request.user, notification_type=1)
        notify.delete()
    else:
        post.likes.add(request.user)
        liked = True
        notify = Notification(post=post, sender=request.user, user=post.author, notification_type=1)
        notify.save()

    context = {
        'post':post,
        'total_likes':post.total_likes(),
        'liked':liked,
    }

    if is_ajax(request=request):
        html = render_to_string('blog/like_section.html',context, request=request)
        return JsonResponse({'form':html})

@login_required
def LikeViewleetcode(request):
    postleetcode = get_object_or_404(Postleetcode, id=request.POST.get('postleetcode_id'))
    liked = False
    if postleetcode.likesleetcode.filter(id=request.user.id).exists():
        postleetcode.likesleetcode.remove(request.user)
        liked = False
        # notify = Notification.objects.filter(post=postcpp, sender=request.user, notification_type=1)
        # notify.delete()
    else:
        postleetcode.likesleetcode.add(request.user)
        liked = True
        # notify = Notification(post=postcpp, sender=request.user, user=postcpp.author, notification_type=1)
        # notify.save()

    context = {
        'postleetcode':postleetcode,
        'total_likes_leetcode':postleetcode.total_likes_leetcode(),
        'liked':liked,
    }

    if is_ajax(request=request):
        html = render_to_string('blog/like_section_leetcode.html',context, request=request)
        return JsonResponse({'form':html})

@login_required
def LikeViewlb(request):
    postlb= get_object_or_404(Postlb, id=request.POST.get('postlb_id'))
    liked = False
    if postlb.likeslb.filter(id=request.user.id).exists():
        postlb.likeslb.remove(request.user)
        liked = False
        # notify = Notification.objects.filter(post=postcpp, sender=request.user, notification_type=1)
        # notify.delete()
    else:
        postlb.likeslb.add(request.user)
        liked = True
        # notify = Notification(post=postcpp, sender=request.user, user=postcpp.author, notification_type=1)
        # notify.save()

    context = {
        'postlb':postlb,
        'total_likes_lb':postlb.total_likes_lb(),
        'liked':liked,
    }

    if is_ajax(request=request):
        html = render_to_string('blog/like_section_lb.html',context, request=request)
        return JsonResponse({'form':html})

@login_required
def LikeViewcpp(request):
    postcpp = get_object_or_404(Postcpp, id=request.POST.get('postcpp_id'))
    liked = False
    if postcpp.likescpp.filter(id=request.user.id).exists():
        postcpp.likescpp.remove(request.user)
        liked = False
        # notify = Notification.objects.filter(post=postcpp, sender=request.user, notification_type=1)
        # notify.delete()
    else:
        postcpp.likescpp.add(request.user)
        liked = True
        # notify = Notification(post=postcpp, sender=request.user, user=postcpp.author, notification_type=1)
        # notify.save()

    context = {
        'postcpp':postcpp,
        'total_likes_cpp':postcpp.total_likes_cpp(),
        'liked':liked,
    }

    if is_ajax(request=request):
        html = render_to_string('blog/like_section_cpp.html',context, request=request)
        return JsonResponse({'form':html})

@login_required
def LikeViewjava(request):

    postjava = get_object_or_404(Postjava, id=request.POST.get('id'))
    liked = False
    if postjava.likes.filter(id=request.user.id).exists():
        postjava.likes.remove(request.user)
        liked = False
        notify = Notification.objects.filter(post=postjava, sender=request.user, notification_type=1)
        notify.delete()
    else:
        postjava.likes.add(request.user)
        liked = True
        notify = Notification(post=postjava, sender=request.user, user=postjava.author, notification_type=1)
        notify.save()

    context = {
        'post':postjava,
        'total_likes_java':postjava.total_likes_java(),
        'liked':liked,
    }

    if is_ajax(request=request):
        html = render_to_string('blog/like_section_java.html',context, request=request)
        return JsonResponse({'form':html})

@login_required
def LikeViewpython(request):

    postpython = get_object_or_404(Postpython, id=request.POST.get('id'))
    liked = False
    if postpython.likes.filter(id=request.user.id).exists():
        postpython.likes.remove(request.user)
        liked = False
        notify = Notification.objects.filter(post=postpython, sender=request.user, notification_type=1)
        notify.delete()
    else:
        postpython.likes.add(request.user)
        liked = True
        notify = Notification(post=postpython, sender=request.user, user=postpython.author, notification_type=1)
        notify.save()

    context = {
        'post':postpython,
        'total_likes_python':postpython.total_likes_python(),
        'liked':liked,
    }

    if is_ajax(request=request):
        html = render_to_string('blog/like_section_java.html',context, request=request)
        return JsonResponse({'form':html})


""" Post save DSA """
@login_required
def SaveView(request):

    post = get_object_or_404(Post, id=request.POST.get('id'))
    saved = False
    if post.saves.filter(id=request.user.id).exists():
        post.saves.remove(request.user)
        saved = False
    else:
        post.saves.add(request.user)
        saved = True
    
    context = {
        'post':post,
        'total_saves':post.total_saves(),
        'saved':saved,
    }

    if is_ajax(request=request):
        html = render_to_string('blog/save_section.html',context, request=request)
        return JsonResponse({'form':html})

""" Post save C++ """
@login_required
def SaveViewcpp(request):

    post = get_object_or_404(Postcpp, id=request.POST.get('id'))
    savedcpp = False
    if post.saves.filter(id=request.user.id).exists():
        post.saves.remove(request.user)
        savedcpp = False
    else:
        post.saves.add(request.user)
        savedcpp = True
    
    context = {
        'post':post,
        'total_saves_cpp':post.total_saves_cpp(),
        'savedcpp':savedcpp,
    }

    if is_ajax(request=request):
        html = render_to_string('blog/save_section_cpp.html',context, request=request)
        return JsonResponse({'form':html})

""" Post save Java """
@login_required
def SaveViewjava(request):

    postjava = get_object_or_404(Postjava, id=request.POST.get('id'))
    saved = False
    if postjava.saves.filter(id=request.user.id).exists():
        postjava.saves.remove(request.user)
        saved = False
    else:
        postjava.saves.add(request.user)
        saved = True
    
    context = {
        'post':postjava,
        'total_saves_java':postjava.total_saves_java(),
        'saved':saved,
    }

    if is_ajax(request=request):
        html = render_to_string('blog/save_section_java.html',context, request=request)
        return JsonResponse({'form':html})

""" Post save Python """
@login_required
def SaveViewpython(request):

    postpython = get_object_or_404(Postpython, id=request.POST.get('id'))
    saved = False
    if postpython.saves.filter(id=request.user.id).exists():
        postpython.saves.remove(request.user)
        saved = False
    else:
        postpython.saves.add(request.user)
        saved = True
    
    context = {
        'post':postpython,
        'total_saves_python':postpython.total_saves_python(),
        'saved':saved,
    }

    if is_ajax(request=request):
        html = render_to_string('blog/save_section_python.html',context, request=request)
        return JsonResponse({'form':html})

""" Like post comments """
@login_required
def LikeCommentView(request): # , id1, id2              id1=post.pk id2=reply.pk
    post = get_object_or_404(Comment, id=request.POST.get('id'))
    cliked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        cliked = False
    else:
        post.likes.add(request.user)
        cliked = True

    cpost = get_object_or_404(Post, id=request.POST.get('pid'))
    total_comments2 = cpost.comments.all().order_by('-id')
    total_comments = cpost.comments.all().filter(reply=None).order_by('-id')
    tcl={}
    for cmt in total_comments2:
        total_clikes = cmt.total_clikes()
        cliked = False
        if cmt.likes.filter(id=request.user.id).exists():
            cliked = True

        tcl[cmt.id] = cliked


    context = {
        'comment_form':CommentForm(),
        'post':cpost,
        'comments':total_comments,
        'total_clikes':post.total_clikes(),
        'clikes':tcl
    }

    if is_ajax(request=request):
        html = render_to_string('blog/comments.html',context, request=request)
        return JsonResponse({'form':html})

""" Like post comments C++ """
@login_required
def LikeCommentViewcpp(request): # , id1, id2              id1=post.pk id2=reply.pk
    postcpp = get_object_or_404(Commentcpp, id=request.POST.get('id'))
    clikedcpp = False
    if postcpp.likes.filter(id=request.user.id).exists():
        postcpp.likes.remove(request.user)
        clikedcpp = False
    else:
        postcpp.likes.add(request.user)
        clikedcpp = True

    cpostcpp = get_object_or_404(Postcpp, id=request.POST.get('pid'))
    total_comments2_cpp = cpostcpp.commentscpp.all().order_by('-id')
    total_comments_cpp = cpostcpp.commentscpp.all().filter(reply=None).order_by('-id')
    tcl_cpp={}
    for cmt in total_comments2_cpp:
        total_clikes_cpp = cmt.total_clikes_cpp()
        clikedcpp = False
        if cmt.likes.filter(id=request.user.id).exists():
            clikedcpp = True

        tcl_cpp[cmt.id] = clikedcpp


    context = {
        'comment_form':CommentFormcpp(),
        'post':cpostcpp,
        'comments':total_comments_cpp,
        'total_clikes_cpp':postcpp.total_clikes_cpp(),
        'clikes':tcl_cpp
    }

    if is_ajax(request=request):
        html = render_to_string('blog/comments_cpp.html',context, request=request)
        return JsonResponse({'form':html})


""" Like post comments Java """
@login_required
def LikeCommentViewjava(request): # , id1, id2              id1=post.pk id2=reply.pk
    postjava = get_object_or_404(Commentjava, id=request.POST.get('id'))
    clikedjava = False
    if postjava.likes.filter(id=request.user.id).exists():
        postjava.likes.remove(request.user)
        clikedjava = False
    else:
        postjava.likes.add(request.user)
        clikedjava = True

    cpostjava = get_object_or_404(Postjava, id=request.POST.get('pid'))
    total_comments2_java = cpostjava.comments.all().order_by('-id')
    total_comments_java = cpostjava.comments.all().filter(reply=None).order_by('-id')
    tcl_java={}
    for cmt in total_comments2_java:
        total_clikes_java = cmt.total_clikes_java()
        clikedjava = False
        if cmt.likes.filter(id=request.user.id).exists():
            clikedjava = True

        tcl_java[cmt.id] = clikedjava


    context = {
        'comment_form':CommentFormjava(),
        'post':cpostjava,
        'comments':total_comments_java,
        'total_clikes_java':postjava.total_clikes_java(),
        'clikes':tcl_java
    }

    if is_ajax(request=request):
        html = render_to_string('blog/comments_java.html',context, request=request)
        return JsonResponse({'form':html})

""" Like post comments Python """
@login_required
def LikeCommentViewpython(request): # , id1, id2              id1=post.pk id2=reply.pk
    postpython = get_object_or_404(Commentpython, id=request.POST.get('id'))
    clikedpython = False
    if postpython.likes.filter(id=request.user.id).exists():
        postpython.likes.remove(request.user)
        clikedpython = False
    else:
        postpython.likes.add(request.user)
        clikedpython = True

    cpostpython = get_object_or_404(Postpython, id=request.POST.get('pid'))
    total_comments2_python = cpostpython.comments.all().order_by('-id')
    total_comments_python = cpostpython.comments.all().filter(reply=None).order_by('-id')
    tcl_python={}
    for cmt in total_comments2_python:
        total_clikes_python = cmt.total_clikes_python()
        clikedpython = False
        if cmt.likes.filter(id=request.user.id).exists():
            clikedpython = True

        tcl_python[cmt.id] = clikedpython


    context = {
        'comment_form':CommentFormpython(),
        'post':cpostpython,
        'comments':total_comments_python,
        'total_clikes_python':postpython.total_clikes_python(),
        'clikes':tcl_python
    }

    if is_ajax(request=request):
        html = render_to_string('blog/comments_python.html',context, request=request)
        return JsonResponse({'form':html})


""" Home page with all posts """
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' 
    context_object_name = 'posts'
    ordering = ['date_posted']
    paginate_by = 5

    def get_context_data(self, *args,**kwargs):
        context = super(PostListView, self).get_context_data()
        users = list(User.objects.exclude(pk=self.request.user.pk))
        if len(users) > 3:
            cnt = 3
        else:
            cnt = len(users)
        random_users = random.sample(users, cnt)
        context['random_users'] = random_users
        return context


""" All the posts of the user """
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' 
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('date_posted')



""" Post detail view DSA """
def PostDetailView(request,pk):

    stuff = get_object_or_404(Post, id=pk)
    total_likes = stuff.total_likes()
    total_saves = stuff.total_saves()
    total_comments = stuff.comments.all().filter(reply=None).order_by('-id')
    total_comments2 = stuff.comments.all().order_by('-id')

    context = {}

    if request.method == "POST":
        comment_qs = None
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            form = request.POST.get('body')
            reply_id = request.POST.get('comment_id')
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            
            comment = Comment.objects.create(name=request.user,post=stuff,body=form, reply=comment_qs)
            comment.save()
            if reply_id:
                notify = Notification(post=stuff, sender=request.user, user=stuff.author, text_preview=form, notification_type=4)
                notify.save()
            else:
                notify = Notification(post=stuff, sender=request.user, user=stuff.author, text_preview=form, notification_type=3)
                notify.save()
            total_comments = stuff.comments.all().filter(reply=None).order_by('-id')
            total_comments2 = stuff.comments.all().order_by('-id')
    else:
        comment_form = CommentForm()
             

    tcl={}
    for cmt in total_comments2:
        total_clikes = cmt.total_clikes()
        cliked = False
        if cmt.likes.filter(id=request.user.id).exists():
            cliked = True

        tcl[cmt.id] = cliked
    context["clikes"]=tcl


    liked = False
    if stuff.likes.filter(id=request.user.id).exists():
        liked = True
    context["total_likes"]=total_likes
    context["liked"]=liked


    saved = False
    if stuff.saves.filter(id=request.user.id).exists():
        saved = True
    context["total_saves"]=total_saves
    context["saved"]=saved
    

    context['comment_form'] = comment_form

    context['post']=stuff
    context['comments']=total_comments

    if is_ajax(request=request):
        html = render_to_string('blog/comments.html',context, request=request)
        return JsonResponse({'form':html})

    return render(request, 'blog/post_detail.html', context)

def post_likes(request, self):
    posts = get_object_or_404(Post, slug=self.kwargs['slug'])
    post_likes = posts.likes.all()
    context = {'post_likes': post_likes, }
    return render(request, 'blog/post_detail.html', context)

""" Post detail view C++"""
def PostDetailViewcpp(request,pk):

    stuff = get_object_or_404(Postcpp, id=pk)
    total_likes_cpp = stuff.total_likes_cpp()
    total_saves_cpp = stuff.total_saves_cpp()
    total_comments_cpp = stuff.commentscpp.all().filter(reply=None).order_by('-id')
    total_comments2_cpp= stuff.commentscpp.all().order_by('-id')

    context = {}

    if request.method == "POST":
        comment_qs_cpp = None
        comment_form_cpp = CommentFormcpp(request.POST or None)
        if comment_form_cpp.is_valid():
            form = request.POST.get('body')
            reply_id = request.POST.get('comment_id')
            if reply_id:
                comment_qs_cpp = Commentcpp.objects.get(id=reply_id)
            
            commentcpp = Commentcpp.objects.create(name=request.user,postcpp=stuff,body=form, reply=comment_qs_cpp)
            commentcpp.save()
    
            total_comments_cpp = stuff.commentscpp.all().filter(reply=None).order_by('-id')
            total_comments2_cpp = stuff.commentscpp.all().order_by('-id')
    else:
        comment_form_cpp = CommentFormcpp()
             

    tcl_cpp={}
    
    for cmt in total_comments2_cpp:
        total_clikes_cpp = cmt.total_clikes_cpp()
        clikedcpp = False
        if cmt.likes.filter(id=request.user.id).exists():
            clikedcpp = True

        tcl_cpp[cmt.id] = clikedcpp
    context["clikes"]=tcl_cpp


    liked = False
    if stuff.likescpp.filter(id=request.user.id).exists():
        liked = True
    context["total_likes_cpp"]=total_likes_cpp
    context["liked"]=liked


    saved = False
    if stuff.savescpp.filter(id=request.user.id).exists():
        saved = True
    context["total_saves_cpp"]=total_saves_cpp
    context["saved"]=saved
    

    context['comment_form_cpp'] = comment_form_cpp

    context['post']=stuff
    context['comments']=total_comments_cpp

    if is_ajax(request=request):
        html = render_to_string('blog/comments_cpp.html',context, request=request)
        return JsonResponse({'form':html})

    return render(request, 'blog/post_detail_cpp.html', context)

""" Post detail view LeetCode """
def PostDetailViewleetcode(request,pk):

    stuff = get_object_or_404(Postleetcode, id=pk)
    total_likes_leetcode = stuff.total_likes_leetcode()
    total_saves_leetcode = stuff.total_saves_leetcode()
    total_comments_leetcode = stuff.commentsleetcode.all().filter(reply=None).order_by('-id')
    total_comments2_leetcode= stuff.commentsleetcode.all().order_by('-id')

    context = {}

    if request.method == "POST":
        comment_qs_leetcode = None
        comment_form_leetcode = CommentFormleetcode(request.POST or None)
        if comment_form_leetcode.is_valid():
            form = request.POST.get('body')
            reply_id = request.POST.get('comment_id')
            if reply_id:
                comment_qs_leetcode = Commentleetcode.objects.get(id=reply_id)
            
            commentleetcode = Commentleetcode.objects.create(name=request.user,postleetcode=stuff,body=form, reply=comment_qs_leetcode)
            commentleetcode.save()
    
            total_comments_leetcode = stuff.commentsleetcode.all().filter(reply=None).order_by('-id')
            total_comments2_leetcode = stuff.commentsleetcode.all().order_by('-id')
    else:
        comment_form_leetcode = CommentFormleetcode()
             

    tcl_leetcode={}
    
    for cmt in total_comments2_leetcode:
        total_clikes_leetcode = cmt.total_clikes_leetcode()
        clikedleetcode = False
        if cmt.likes.filter(id=request.user.id).exists():
            clikedleetcode = True

        tcl_leetcode[cmt.id] = clikedleetcode
    context["clikes"]=tcl_leetcode


    liked = False
    if stuff.likes.filter(id=request.user.id).exists():
        liked = True
    context["total_likes_leetcode"]=total_likes_leetcode
    context["liked"]=liked


    saved = False
    if stuff.saves.filter(id=request.user.id).exists():
        saved = True
    context["total_saves_leetcode"]=total_saves_leetcode
    context["saved"]=saved
    

    context['comment_form_leetcode'] = comment_form_leetcode

    context['post']=stuff
    context['comments']=total_comments_leetcode

    if is_ajax(request=request):
        html = render_to_string('blog/comments_leetcode.html',context, request=request)
        return JsonResponse({'form':html})

    return render(request, 'blog/post_detail_leetcode.html', context)

""" Post detail view LeetCode """
def PostDetailViewlb(request,pk):

    stuff = get_object_or_404(Postlb, id=pk)
    total_likes_lb= stuff.total_likes_lb()
    total_saves_lb = stuff.total_saves_lb()
    total_comments_lb = stuff.commentslb.all().filter(reply=None).order_by('-id')
    total_comments2_lb = stuff.commentslb.all().order_by('-id')

    context = {}

    if request.method == "POST":
        comment_qs_lb = None
        comment_form_lb = CommentFormlb(request.POST or None)
        if comment_form_lb.is_valid():
            form = request.POST.get('body')
            reply_id = request.POST.get('comment_id')
            if reply_id:
                comment_qs_lb = Commentlb.objects.get(id=reply_id)
            
            commentlb = Commentlb.objects.create(name=request.user,postlb=stuff,body=form, reply=comment_qs_lb)
            commentlb.save()
    
            total_comments_lb = stuff.commentslb.all().filter(reply=None).order_by('-id')
            total_comments2_lb = stuff.commentslb.all().order_by('-id')
    else:
        comment_form_lb = CommentFormlb()
             

    tcl_lb={}
    
    for cmt in total_comments2_lb:
        total_clikes_lb = cmt.total_clikes_lb()
        clikedlb = False
        if cmt.likes.filter(id=request.user.id).exists():
            tcl_lb = True

        tcl_lb[cmt.id] = tcl_lb
    context["clikes"]=tcl_lb


    liked = False
    if stuff.likes.filter(id=request.user.id).exists():
        liked = True
    context["total_likes_lb"]=total_likes_lb
    context["liked"]=liked


    saved = False
    if stuff.saves.filter(id=request.user.id).exists():
        saved = True
    context["total_saves_lb"]=total_saves_lb
    context["saved"]=saved
    

    context['comment_form_lb'] = comment_form_lb

    context['post']=stuff
    context['comments']=total_comments_lb

    if is_ajax(request=request):
        html = render_to_string('blog/comments_lb.html',context, request=request)
        return JsonResponse({'form':html})

    return render(request, 'blog/post_detail_lb.html', context)


""" Post detail view Java """
def PostDetailViewjava(request,pk):

    stuff = get_object_or_404(Postjava, id=pk)
    total_likes_java = stuff.total_likes_java()
    total_saves_java = stuff.total_saves_java()
    total_comments_java = stuff.commentsjava.all().filter(reply=None).order_by('-id')
    total_comments2_java= stuff.commentsjava.all().order_by('-id')

    context = {}

    if request.method == "POST":
        comment_qs_java = None
        comment_form_java = CommentFormjava(request.POST or None)
        if comment_form_java.is_valid():
            form = request.POST.get('body')
            reply_id = request.POST.get('comment_id')
            if reply_id:
                comment_qs_java = Commentjava.objects.get(id=reply_id)
            
            commentjava = Commentjava.objects.create(name=request.user,postjava=stuff,body=form, reply=comment_qs_java)
            commentjava.save()
    
            total_comments_java = stuff.commentsjava.all().filter(reply=None).order_by('-id')
            total_comments2_java = stuff.commentsjava.all().order_by('-id')
    else:
        comment_form_java = CommentFormjava()
             

    tcl_java={}
    
    for cmt in total_comments2_java:
        total_clikes_java = cmt.total_clikes_java()
        clikedjava = False
        if cmt.likes.filter(id=request.user.id).exists():
            clikedjava = True

        tcl_java[cmt.id] = clikedjava
    context["clikes"]=tcl_java


    liked = False
    if stuff.likes.filter(id=request.user.id).exists():
        liked = True
    context["total_likes_java"]=total_likes_java
    context["liked"]=liked


    saved = False
    if stuff.saves.filter(id=request.user.id).exists():
        saved = True
    context["total_saves_java"]=total_saves_java
    context["saved"]=saved
    

    context['comment_form_java'] = comment_form_java

    context['post']=stuff
    context['comments']=total_comments_java

    if is_ajax(request=request):
        html = render_to_string('blog/comments_java.html',context, request=request)
        return JsonResponse({'form':html})

    return render(request, 'blog/post_detail_java.html', context)

""" Post detail view Java """
def PostDetailViewpython(request,pk):

    stuff = get_object_or_404(Postpython, id=pk)
    total_likes_python = stuff.total_likes_python()
    total_saves_python = stuff.total_saves_python()
    total_comments_python = stuff.commentspython.all().filter(reply=None).order_by('-id')
    total_comments2_python= stuff.commentspython.all().order_by('-id')

    context = {}

    if request.method == "POST":
        comment_qs_python = None
        comment_form_python = CommentFormpython(request.POST or None)
        if comment_form_python.is_valid():
            form = request.POST.get('body')
            reply_id = request.POST.get('comment_id')
            if reply_id:
                comment_qs_python = Commentpython.objects.get(id=reply_id)
            
            commentpython = Commentpython.objects.create(name=request.user,postpython=stuff,body=form, reply=comment_qs_python)
            commentpython.save()
    
            total_comments_python = stuff.commentspython.all().filter(reply=None).order_by('-id')
            total_comments2_python = stuff.commentspython.all().order_by('-id')
    else:
        comment_form_python = CommentFormpython()
             

    tcl_python={}
    
    for cmt in total_comments2_python:
        total_clikes_python = cmt.total_clikes_python()
        clikedpython = False
        if cmt.likes.filter(id=request.user.id).exists():
            clikedpython = True

        tcl_python[cmt.id] = clikedpython
    context["clikes"]=tcl_python


    liked = False
    if stuff.likes.filter(id=request.user.id).exists():
        liked = True
    context["total_likes_python"]=total_likes_python
    context["liked"]=liked


    saved = False
    if stuff.saves.filter(id=request.user.id).exists():
        saved = True
    context["total_saves_python"]=total_saves_python
    context["saved"]=saved
    

    context['comment_form_python'] = comment_form_python

    context['post']=stuff
    context['comments']=total_comments_python

    if is_ajax(request=request):
        html = render_to_string('blog/comments_python.html',context, request=request)
        return JsonResponse({'form':html})

    return render(request, 'blog/post_detail_python.html', context)

""" Create post DSA """
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
   
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

""" Create post Leetcode """
class PostCreateViewleetcode(LoginRequiredMixin, CreateView):
    model = Postleetcode
    form_class = PostFormleetcode
   
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

""" Create post Logic Building """
class PostCreateViewlb(LoginRequiredMixin, CreateView):
    model = Postlb
    form_class = PostFormlb
   
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

""" Create post C++ """
class PostCreateViewcpp(LoginRequiredMixin, CreateView):
    model = Postcpp
    form_class = PostFormcpp
   
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

""" Create post Java """
class PostCreateViewjava(LoginRequiredMixin, CreateView):
    model = Postjava
    form_class = PostFormjava
   
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

""" Create post Python """
class PostCreateViewpython(LoginRequiredMixin, CreateView):
    model = Postpython
    form_class = PostFormPython
   
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

""" Update post """
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields =['title', 'content','level', 'link','inputfield','outputfield', 'explanation']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


""" Delete post """
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


""" About page """
def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

def companypdf(request):
    return render(request, 'blog/companypdf.html', {'title':'Company PDF'})

def randomdsa(request):
    return render(request, 'blog/random.html', {'title':'DSA Randomiser'})

def languages(request):
    return render(request, 'blog/languages.html', {'title':'Languages'})

def randomcf(request):
    return render(request, 'blog/randomcf.html', {'title':'CF Random Generator'})

def randomcfrating(request):
    return render(request, 'blog/randomcfrating.html', {'title':'CF Rating Based'})

def randomcfratingmain(request):
    return render(request, 'blog/main.html', {'title':'CF Rating Based'})
    
def cfuserdetails(request):
    return render(request, 'blog/cfuserdetails.html', {'title':'CF User Details'})

def cfcontests(request):
    return render(request, 'blog/cfcontests.html', {'title':'CF Contests'})

def contact(request):
    return render(request, 'blog/contact.html', {'title':'Contact'})

""" Search by post title or username """
def search(request):
    query = request.GET['query']
    if len(query) >= 150 or len(query) < 1:
        allposts = Post.objects.none()
    elif len(query.strip()) == 0:
        allposts = Post.objects.none()
    else:
        allpostsTitle = Post.objects.filter(title__icontains=query)
        allpostsAuthor = Post.objects.filter(author__username = query)
        allposts = allpostsAuthor.union(allpostsTitle)
    
    params = {'allposts': allposts}
    return render(request, 'blog/search_results.html', params)


""" Liked posts """
@login_required
def AllLikeView(request):
    user = request.user
    liked_posts = user.blogpost.all()
    context = {
        'liked_posts':liked_posts
    }
    return render(request, 'blog/liked_posts.html', context)

""" Liked posts C++ """
@login_required
def AllLikeViewcpp(request):
    user = request.user
    liked_posts_cpp = user.blogpostcpp.all()
    context = {
        'liked_posts_cpp':liked_posts_cpp
    }
    return render(request, 'blog/liked_posts_cpp.html', context)

""" Liked posts Java """
@login_required
def AllLikeViewjava(request):
    user = request.user
    liked_posts_java = user.blogpostjava.all()
    context = {
        'liked_posts_java':liked_posts_java
    }
    return render(request, 'blog/liked_posts_java.html', context)

""" Liked posts Python """
@login_required
def AllLikeViewpython(request):
    user = request.user
    liked_posts_python= user.blogpostpython.all()
    context = {
        'liked_posts_python':liked_posts_python
    }
    return render(request, 'blog/liked_posts_python.html', context)

@login_required
def AllLikeCategoryView(request):
    ordering = ["-id"]
    user = request.user
    liked_posts = user.blogpost.all()
    context = {
        'liked_posts':liked_posts
    }
    return render(request, 'blog/categories.html', context)

""" Saved posts """
@login_required
def AllSaveView(request):
    user = request.user
    saved_posts = user.blogsave.all()
    context = {
        'saved_posts':saved_posts
    }
    return render(request, 'blog/saved_posts.html', context)

""" Saved posts """
@login_required
def AllSaveViewcpp(request):
    user = request.user
    saved_posts_cpp = user.blogsavecpp.all()
    context = {
        'saved_posts_cpp':saved_posts_cpp
    }
    return render(request, 'blog/saved_posts_cpp.html', context)

""" Saved posts Java """
@login_required
def AllSaveViewjava(request):
    user = request.user
    saved_posts_java = user.blogsavejava.all()
    context = {
        'saved_posts_java':saved_posts_java
    }
    return render(request, 'blog/saved_posts_java.html', context)

""" Saved posts Python """
@login_required
def AllSaveViewPython(request):
    user = request.user
    saved_posts_python = user.blogsavepython.all()
    context = {
        'saved_posts_python':saved_posts_python
    }
    return render(request, 'blog/saved_posts_python.html', context)

def category_list_leetcode(request):
    categoriesleetcode = Categoryleetcode.objects.all() # this will get all categories, you can do some filtering if you need (e.g. excluding categories without posts in it)
    return render (request, 'blog/category_list_leetcode.html', {'categoriesleetcode': categoriesleetcode}) # blog/category_list.html should be the template that categories are listed.


def category_list_leetcode(request):
    categoriesleetcode = Categoryleetcode.objects.all() # this will get all categories, you can do some filtering if you need (e.g. excluding categories without posts in it)
    return render (request, 'blog/category_list_leetcode.html', {'categoriesleetcode': categoriesleetcode}) # blog/category_list.html should be the template that categories are listed.


def category_list(request):
    categories = Category.objects.all() # this will get all categories, you can do some filtering if you need (e.g. excluding categories without posts in it)
    return render (request, 'blog/category_list.html', {'categories': categories}) # blog/category_list.html should be the template that categories are listed.

def category_list_cpp(request):
    categoriescpp = Categorycpp.objects.all() # this will get all categories, you can do some filtering if you need (e.g. excluding categories without posts in it)
    return render (request, 'blog/category_list_cpp.html', {'categoriescpp': categoriescpp}) # blog/category_list.html should be the template that categories are listed.

def category_list_java(request):
    categoriesjava = Categoryjava.objects.all() # this will get all categories, you can do some filtering if you need (e.g. excluding categories without posts in it)
    return render (request, 'blog/category_list_java.html', {'categoriesjava': categoriesjava}) # blog/category_list.html should be the template that categories are listed.

def category_list_python(request):
    categoriespython = Categorypython.objects.all() # this will get all categories, you can do some filtering if you need (e.g. excluding categories without posts in it)
    return render (request, 'blog/category_list_python.html', {'categoriespython': categoriespython}) # blog/category_list.html should be the template that categories are listed.


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)

    return render(request, 'blog/category_detail.html', {'category': category}) # in this template, you will have access to category and posts under that category by (category.post_set).

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__' 

def CategoryView(request, cats):
    ordering = ["-id"]
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', 
  		  {'cats':cats, 'category_posts':category_posts})

def CategoryView(request, cats):
    ordering = ["-id"]
    category_posts = Post.objects.filter(
    	             category=cats.replace('-', ' '))
    return render(request, 'categories.html', 
                  {'cats':cats.replace('-', ' '), 
                  'category_posts':category_posts})



def CategoryViewcpp(request, cats):
    ordering = ["-id"]
    category_posts_cpp = Postcpp.objects.filter(
    	             category=cats.replace('-', ' '))
    return render(request, 'categories_cpp.html', 
                  {'cats':cats.replace('-', ' '), 
                  'category_posts_cpp':category_posts_cpp})
  
def CategoryViewleetcode(request, cats):
    ordering = ["-id"]
    category_posts= Postleetcode.objects.filter(
    	             category=cats.replace('-', ' '))
    return render(request, 'categories_leetcode.html', 
                  {'cats':cats.replace('-', ' '), 
                  'category_posts':category_posts})


def CategoryViewjava(request, cats):
    ordering = ["-id"]
    category_posts_java = Postjava.objects.filter(
    	             category=cats.replace('-', ' '))
    return render(request, 'categories_java.html', 
                  {'cats':cats.replace('-', ' '), 
                  'category_posts_java':category_posts_java})

def CategoryViewpython(request, cats):
    ordering = ["-id"]
    category_posts_python = Postpython.objects.filter(
    	             category=cats.replace('-', ' '))
    return render(request, 'categories_python.html', 
                  {'cats':cats.replace('-', ' '), 
                  'category_posts_python':category_posts_python})

class HomeView(ListView):
    def get_context_data(self, *args, **kwargs):
        ordering = ["-id"]
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryListViewleetcode(request):
	cat_menu_list_leetcode = Categoryleetcode.objects.all()
	return render(request, 'category_list_leetcode.html', {'cat_menu_list_leetcode':cat_menu_list_leetcode})

def CategoryListViewlb(request):
	cat_menu_list_lb = Categorylb.objects.all()
	return render(request, 'category_list_lb.html', {'cat_menu_list_lb':cat_menu_list_lb})

def CategoryListView(request):
	cat_menu_list = Category.objects.all()
	return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})

def CategoryListViewcpp(request):
	cat_menu_list_cpp = Categorycpp.objects.all()
	return render(request, 'category_list_cpp.html', {'cat_menu_list_cpp':cat_menu_list_cpp})

def CategoryListViewjava(request):
	cat_menu_list_java = Categoryjava.objects.all()
	return render(request, 'category_list_java.html', {'cat_menu_list_java':cat_menu_list_java})

def CategoryListViewpython(request):
	cat_menu_list_python = Categorypython.objects.all()
	return render(request, 'category_list_python.html', {'cat_menu_list_python':cat_menu_list_python})