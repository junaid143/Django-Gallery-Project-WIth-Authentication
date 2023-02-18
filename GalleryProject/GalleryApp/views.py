from django.shortcuts import render,redirect
from .forms import LoginForm , RegisterForm , AddImageForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from .models import CategoryModel , ImageModel

# Create your views here.


def home_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            pass1 = request.POST['password']
            user = authenticate(username = username , password = pass1)

            if user is not None:
                login(request , user)
                return redirect('gallery')
        
        forms = LoginForm()
        context = { 'forms' : forms}
        return render(request , 'home.html' , context)
    else:
        return redirect('gallery')


def register_view(request):

    if request.method == 'POST':
        forms = RegisterForm(request.POST)
        # print(forms)
        if forms.is_valid():
            forms.save()

            return redirect('home')
        else:
            context = {'forms':forms}
            return render(request , 'register.html' , context)


    forms = RegisterForm()
    context = {'forms':forms}
    return render(request , 'register.html' , context)



def signout_view(request):
    logout(request)
    return redirect('home')



def gallery_view(request):

    categories = CategoryModel.objects.all()
    datas = ImageModel.objects.all()
    
    # print(username)

    context = { 'categories':categories , 'datas':datas}
    return render(request , 'gallery.html' , context)



def addimage_view(request):


    if request.method == 'POST':
        forms = AddImageForm(request.POST , request.FILES)
        #
        if forms.is_valid():
            task_list = forms.save(commit = False)
            task_list.uploaded_by = request.user
            task_list.save()

            return redirect('gallery')

    forms = AddImageForm()
    context = {'forms':forms}

    return render(request , 'addimage.html' , context)

def category_view(request , id):
    categories = CategoryModel.objects.all()
    cat = CategoryModel.objects.get(id = id)
    datas = ImageModel.objects.filter(cat = cat)

    context = { 'categories':categories , 'datas':datas}
    return render(request , 'gallery.html' , context)






