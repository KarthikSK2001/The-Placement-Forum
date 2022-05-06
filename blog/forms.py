from logging import PlaceHolder
from django import forms
from django.forms import fields, widgets
from .models import Categorylb, Categoryleetcode, Commentlb, Commentleetcode, Post, Comment, Category,Postcpp,Categorycpp,Commentcpp,Categoryjava, Postjava,Commentjava, Postlb, Postleetcode,Postpython, Categorypython, Commentpython

# choices =  Category.objects.all().values_list('name','name')
# choice_list = []

# for item in choices:
# 	choice_list.append(item)
''' DSA Category '''
choices = Category.objects.all().values_list('title','title') 
#name is from model field
choice_list = []

for item in choices:
    choice_list.append(item)

''' LeetCode Category '''
choicesleetcode = Categoryleetcode.objects.all().values_list('titleleetcode','titleleetcode') 
#name is from model field
choice_list_leetcode = []

for itemleetcode in choicesleetcode:
    choice_list_leetcode.append(itemleetcode)

''' Logic Building Category '''
choiceslb = Categorylb.objects.all().values_list('titlelb','titlelb') 
#name is from model field
choice_list_lb = []

for itemlb in choiceslb:
    choice_list_lb.append(itemlb)

''' C++ Category '''
choicescpp = Categorycpp.objects.all().values_list('titlecpp','titlecpp') 
#name is from model field
choice_list_cpp = []

for itemcpp in choicescpp:
    choice_list_cpp.append(itemcpp)

''' Java Category '''
choicesjava = Categoryjava.objects.all().values_list('titlejava','titlejava') 
#name is from model field
choice_list_java = []

for itemjava in choicesjava:
    choice_list_java.append(itemjava)

''' Python Category '''
choicespython = Categorypython.objects.all().values_list('titlepython','titlepython') 
#name is from model field
choice_list_python = []

for itempython in choicespython:
    choice_list_python.append(itempython)

''' DSA Forms '''
class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='')
    class Meta:
        model = Comment
        fields = ['body',]

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Description')
    title = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Title')
    level = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question level')
    link = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Link')

    category = forms.CharField(widget=forms.Select(choices=choice_list, 
             attrs={'class': 'form-control'}))
    # 'category': forms.Select(attrs={'class': 'form-control'})
    # topics = forms.Select(choices=choice_list, attrs={'class': 'form-control'})
    class Meta:
        model = Post
        fields = ['content','title','level','link','category']

''' LeetCode Forms '''
class CommentFormleetcode(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='')
    class Meta:
        model = Commentleetcode
        fields = ['body',]

class PostFormlb(forms.ModelForm):
    titlelb1 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Title 1')
    titlelb2 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Title 2')
    titlelb3 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Title 3')
    titlelb4 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Title 4')
    linklb1 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Link 1')
    linklb2 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Link 2')
    linklb3 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Link 3')
    linklb4 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Link 4')

    categorylb= forms.CharField(widget=forms.Select(choices=choice_list_lb, 
             attrs={'class': 'form-control'}))
    # 'category': forms.Select(attrs={'class': 'form-control'})
    # topics = forms.Select(choices=choice_list, attrs={'class': 'form-control'})
    class Meta:
        model = Postlb
        fields = ['titlelb1','titlelb2','titlelb3','titlelb4','linklb1','linklb2','linklb3','linklb4']

''' Logic Building Forms '''
class CommentFormlb(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='')
    class Meta:
        model = Commentlb
        fields = ['body',]

class PostFormleetcode(forms.ModelForm):

    titleleetcode1 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Title 1')
    titleleetcode2 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Title 2')
    titleleetcode3 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Title 3')
    titleleetcode4 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Title 4')
    titleleetcode5 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Title 5')
    titleleetcode6 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Title 6')
    titleleetcode7 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Title 7')
    titleleetcode8 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Title 8')
    titleleetcode9 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Title 9')
    titleleetcode10 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Title 10')
    link1 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Link 1')
    link2 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Link 2')
    link3 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Link 3')
    link4 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Link 4')
    link5 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Link 5')
    link6 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Link 6')
    link7 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Link 7')
    link8 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Link 8')
    link9 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Link 9')
    link10 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Link 10')
    videolink1 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Editorial Link 1')
    videolink2 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Editorial Link 2')
    videolink3 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Editorial Link 3')
    videolink4 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Editorial Link 4')
    videolink5 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Editorial Link 5')
    videolink6 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Editorial Link 6')
    videolink7 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Editorial Link 7')
    videolink8 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Editorial Link 8')
    videolink9 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Editorial Link 9')
    videolink10 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Editorial Link 10')
    categoryleetcode = forms.CharField(widget=forms.Select(choices=choice_list_leetcode, 
             attrs={'class': 'form-control'}))
    # 'category': forms.Select(attrs={'class': 'form-control'})
    # topics = forms.Select(choices=choice_list, attrs={'class': 'form-control'})
    class Meta:
        model = Postleetcode
        fields = ['titleleetcode1','content1','link1','videolink1','titleleetcode2','content2','link2','videolink2','titleleetcode3','content3','link3','videolink3','titleleetcode4','content4','link4','videolink4','titleleetcode5','content5','link5','videolink5','titleleetcode6','content6','link6','videolink6','titleleetcode7','content7','link7','videolink7','titleleetcode8','content8','link8','videolink8','titleleetcode9','content9','link9','videolink9',
        'titleleetcode10','content10','link10','videolink10']


''' C++ Forms '''
class CommentFormcpp(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='')
    class Meta:
        model = Commentcpp
        fields = ['body',]

class PostFormcpp(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Content Description')
    titlecpp = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Content Title')
    videodetails = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Video Links')
    qndetails = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Links')
    docdetails = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Doc Links')
    categorycpp = forms.CharField(widget=forms.Select(choices=choice_list_cpp, 
             attrs={'class': 'form-control'}))
    # 'category': forms.Select(attrs={'class': 'form-control'})
    # topics = forms.Select(choices=choice_list, attrs={'class': 'form-control'})
    class Meta:
        model = Postcpp
        fields = ['content','titlecpp','videodetails','qndetails','docdetails']


''' Java Forms '''
class CommentFormjava(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='')
    class Meta:
        model = Commentjava
        fields = ['body',]

class PostFormjava(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Content Description')
    titlejava = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Content Title')
    videodetails = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Video Links')
    qndetails = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Links')
    docdetails = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Doc Links')
    categoryjava = forms.CharField(widget=forms.Select(choices=choice_list_java, 
             attrs={'class': 'form-control'}))
    # 'category': forms.Select(attrs={'class': 'form-control'})
    # topics = forms.Select(choices=choice_list, attrs={'class': 'form-control'})
    class Meta:
        model = Postjava
        fields = ['content','titlejava','videodetails','qndetails','docdetails']

''' Python Forms '''
class CommentFormpython(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='')
    class Meta:
        model = Commentpython
        fields = ['body',]

class PostFormPython(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Content Description')
    titlepython = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Content Title')
    videodetails = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Video Links')
    qndetails = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Question Links')
    docdetails = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='Doc Links')
    categorypython = forms.CharField(widget=forms.Select(choices=choice_list_python, 
             attrs={'class': 'form-control'}))
    # 'category': forms.Select(attrs={'class': 'form-control'})
    # topics = forms.Select(choices=choice_list, attrs={'class': 'form-control'})
    class Meta:
        model = Postpython
        fields = ['content','titlepython','videodetails','qndetails','docdetails']