from tabnanny import verbose
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

''' Category Model '''
class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title",blank=True,null=True)

    def __str__(self):
        return self.title

""" Post model """
class Post(models.Model):
    title = models.CharField(max_length=150,verbose_name="Title")
    category = models.CharField( max_length=255, default="coding")
    content = RichTextField(blank=True, null=True)
    level = RichTextField(blank=True, null=True)
    link = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topics = models.CharField(max_length=255, default='sample')
    likes = models.ManyToManyField(User, related_name="blogpost", blank=True)
    saves = models.ManyToManyField(User, related_name="blogsave", blank=True)

    def total_likes(self):
        return self.likes.count()

    def total_saves(self):
        return self.saves.count()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"pk":self.pk})


""" Comment model """
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments" , on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blogcomment", blank=True)
    reply = models.ForeignKey('self', null=True, related_name="replies", on_delete=models.CASCADE)

    def total_clikes(self):
        return self.likes.count()

    def __str__(self):
        return '%s - %s - %s' %(self.post.title, self.name, self.id)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"pk":self.pk})

''' Category Model LeetCode '''
class Categoryleetcode(models.Model):
    titleleetcode = models.CharField(max_length=255, verbose_name="Titleleetcode",blank=True,null=True)

    def __str__(self):
        return self.titleleetcode

''' Category Model Logic Building '''
class Categorylb(models.Model):
    titlelb = models.CharField(max_length=255, verbose_name="Titlelb",blank=True,null=True)

    def __str__(self):
        return self.titlelb

""" Post model LeetCode """
class Postleetcode(models.Model):
    titleleetcode1 = models.CharField(max_length=150,verbose_name="Titleleetcode")
    titleleetcode2 = models.CharField(max_length=150,verbose_name="Titleleetcode")
    titleleetcode3 = models.CharField(max_length=150,verbose_name="Titleleetcode")
    titleleetcode4 = models.CharField(max_length=150,verbose_name="Titleleetcode")
    titleleetcode5 = models.CharField(max_length=150,verbose_name="Titleleetcode")
    titleleetcode6 = models.CharField(max_length=150,verbose_name="Titleleetcode")
    titleleetcode7 = models.CharField(max_length=150,verbose_name="Titleleetcode")
    titleleetcode8 = models.CharField(max_length=150,verbose_name="Titleleetcode")
    titleleetcode9 = models.CharField(max_length=150,verbose_name="Titleleetcode")
    titleleetcode10 = models.CharField(max_length=150,verbose_name="Titleleetcode")
    categoryleetcode = models.CharField( max_length=255, default="coding")
    content1 = RichTextField(blank=True, null=True)
    content2 = RichTextField(blank=True, null=True)
    content3 = RichTextField(blank=True, null=True)
    content4 = RichTextField(blank=True, null=True)
    content5 = RichTextField(blank=True, null=True)
    content6 = RichTextField(blank=True, null=True)
    content7 = RichTextField(blank=True, null=True)
    content8 = RichTextField(blank=True, null=True)
    content9 = RichTextField(blank=True, null=True)
    content10 = RichTextField(blank=True, null=True)
    level = RichTextField(blank=True, null=True)
    link1 = RichTextField(blank=True, null=True)
    link2 = RichTextField(blank=True, null=True)
    link3 = RichTextField(blank=True, null=True)
    link4 = RichTextField(blank=True, null=True)
    link5 = RichTextField(blank=True, null=True)
    link6 = RichTextField(blank=True, null=True)
    link7 = RichTextField(blank=True, null=True)
    link8 = RichTextField(blank=True, null=True)
    link9 = RichTextField(blank=True, null=True)
    link10 = RichTextField(blank=True, null=True)
    videolink1 = RichTextField(blank=True, null=True)
    videolink2 = RichTextField(blank=True, null=True)
    videolink3 = RichTextField(blank=True, null=True)
    videolink4 = RichTextField(blank=True, null=True)
    videolink5 = RichTextField(blank=True, null=True)
    videolink6 = RichTextField(blank=True, null=True)
    videolink7 = RichTextField(blank=True, null=True)
    videolink8 = RichTextField(blank=True, null=True)
    videolink9 = RichTextField(blank=True, null=True)
    videolink10 = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topics = models.CharField(max_length=255, default='sample')
    likes = models.ManyToManyField(User, related_name="blogpostleetcode", blank=True)
    saves = models.ManyToManyField(User, related_name="blogsaveleetcode", blank=True)

    def total_likes_leetcode(self):
        return self.likes.count()

    def total_saves_leetcode(self):
        return self.saves.count()

    def get_absolute_url(self):
        return reverse('post-detail-leetcode', kwargs={"pk":self.pk})


""" Comment model """
class Commentleetcode(models.Model):
    postleetcode = models.ForeignKey(Postleetcode, related_name="commentsleetcode" , on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blogcommentleetcode", blank=True)
    reply = models.ForeignKey('self', null=True, related_name="replies", on_delete=models.CASCADE)

    def total_clikes_leetcode(self):
        return self.likes.count()

    def __str__(self):
        return '%s - %s - %s' %(self.postleetcode.title, self.name, self.id)

    def get_absolute_url(self):
        return reverse('post-detail-leetcode', kwargs={"pk":self.pk})

""" Post model Logic Building """
class Postlb(models.Model):
    titlelb1 = models.CharField(max_length=150,verbose_name="Titlelb")
    titlelb2 = models.CharField(max_length=150,verbose_name="Titlelb")
    titlelb3 = models.CharField(max_length=150,verbose_name="Titlelb")
    titlelb4 = models.CharField(max_length=150,verbose_name="Titlelb")
    categorylb = models.CharField( max_length=255, default="coding")
    linklb1 = RichTextField(blank=True, null=True)
    linklb2 = RichTextField(blank=True, null=True)
    linklb3 = RichTextField(blank=True, null=True)
    linklb4 = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topics = models.CharField(max_length=255, default='sample')
    likes = models.ManyToManyField(User, related_name="blogpostlb", blank=True)
    saves = models.ManyToManyField(User, related_name="blogsavelb", blank=True)

    def total_likes_lb(self):
        return self.likes.count()

    def total_saves_lb(self):
        return self.saves.count()

    def get_absolute_url(self):
        return reverse('post-detail-lb', kwargs={"pk":self.pk})


""" Comment model """
class Commentlb(models.Model):
    postlb = models.ForeignKey(Postlb, related_name="commentslb" , on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blogcommentlb", blank=True)
    reply = models.ForeignKey('self', null=True, related_name="replies", on_delete=models.CASCADE)

    def total_clikes_lb(self):
        return self.likes.count()

    def __str__(self):
        return '%s - %s - %s' %(self.postlb.title, self.name, self.id)

    def get_absolute_url(self):
        return reverse('post-detail-lb', kwargs={"pk":self.pk})

''' Category Model C++ '''
class Categorycpp(models.Model):
    titlecpp = models.CharField(max_length=255, verbose_name="Titlecpp",blank=True,null=True)

    def __str__(self):
        return self.titlecpp

""" Post model C++ """
class Postcpp(models.Model):
    titlecpp = models.CharField(max_length=150,verbose_name="Titlecpp")
    categorycpp = models.CharField( max_length=255, default="coding")
    content = RichTextField(blank=True, null=True)
    videodetails = RichTextField(blank=True, null=True)
    qndetails = RichTextField(blank=True, null=True)
    docdetails = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topics = models.CharField(max_length=255, default='sample')
    likescpp = models.ManyToManyField(User, related_name="blogpostcpp", blank=True)
    savescpp = models.ManyToManyField(User, related_name="blogsavecpp", blank=True)

    def total_likes_cpp(self):
        return self.likescpp.count()

    def total_saves_cpp(self):
        return self.savescpp.count()

    def get_absolute_url(self):
        return reverse('post-detail-cpp', kwargs={"pk":self.pk})


""" Comment model C++ """
class Commentcpp(models.Model):
    postcpp = models.ForeignKey(Postcpp, related_name="commentscpp" , on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blogcommentcpp", blank=True)
    reply = models.ForeignKey('self', null=True, related_name="replies", on_delete=models.CASCADE)

    def total_clikes_cpp(self):
        return self.likes.count()

    def __str__(self):
        return '%s - %s - %s' %(self.postcpp.titlecpp, self.name, self.id)

    def get_absolute_url(self):
        return reverse('post-detail-cpp', kwargs={"pk":self.pk})

''' Category Model Java '''
class Categoryjava(models.Model):
    titlejava = models.CharField(max_length=255, verbose_name="Titlejava",blank=True,null=True)

    def __str__(self):
        return self.titlejava

""" Post model Java """
class Postjava(models.Model):
    titlejava = models.CharField(max_length=150,verbose_name="Titlejava")
    categoryjava = models.CharField( max_length=255, default="coding")
    content = RichTextField(blank=True, null=True)
    videodetails = RichTextField(blank=True, null=True)
    qndetails = RichTextField(blank=True, null=True)
    docdetails = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topics = models.CharField(max_length=255, default='sample')
    likes = models.ManyToManyField(User, related_name="blogpostjava", blank=True)
    saves = models.ManyToManyField(User, related_name="blogsavejava", blank=True)

    def total_likes_java(self):
        return self.likes.count()

    def total_saves_java(self):
        return self.saves.count()

    def get_absolute_url(self):
        return reverse('post-detail-java', kwargs={"pk":self.pk})


""" Comment model Java """
class Commentjava(models.Model):
    postjava = models.ForeignKey(Postjava, related_name="commentsjava" , on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blogcommentjava", blank=True)
    reply = models.ForeignKey('self', null=True, related_name="replies", on_delete=models.CASCADE)

    def total_clikes_java(self):
        return self.likes.count()

    def __str__(self):
        return '%s - %s - %s' %(self.postjava.titlejava, self.name, self.id)

    def get_absolute_url(self):
        return reverse('post-detail-java', kwargs={"pk":self.pk})

''' Category Model Python '''
class Categorypython(models.Model):
    titlepython = models.CharField(max_length=255, verbose_name="Titlepython",blank=True,null=True)

    def __str__(self):
        return self.titlepython

""" Post model Python """
class Postpython(models.Model):
    titlepython = models.CharField(max_length=150,verbose_name="Titlepython")
    categorypython = models.CharField( max_length=255, default="coding")
    content = RichTextField(blank=True, null=True)
    videodetails = RichTextField(blank=True, null=True)
    qndetails = RichTextField(blank=True, null=True)
    docdetails = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topics = models.CharField(max_length=255, default='sample')
    likes = models.ManyToManyField(User, related_name="blogpostpython", blank=True)
    saves = models.ManyToManyField(User, related_name="blogsavepython", blank=True)

    def total_likes_python(self):
        return self.likes.count()

    def total_saves_python(self):
        return self.saves.count()

    def get_absolute_url(self):
        return reverse('post-detail-python', kwargs={"pk":self.pk})


""" Comment model Python """
class Commentpython(models.Model):
    postpython = models.ForeignKey(Postpython, related_name="commentspython" , on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blogcommentpython", blank=True)
    reply = models.ForeignKey('self', null=True, related_name="replies", on_delete=models.CASCADE)

    def total_clikes_python(self):
        return self.likes.count()

    def __str__(self):
        return '%s - %s - %s' %(self.postpython.titlepython, self.name, self.id)

    def get_absolute_url(self):
        return reverse('post-detail-python', kwargs={"pk":self.pk})