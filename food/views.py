from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
# def login(request):
#     # return HttpResponse('login')
#     pass
# Create your views here.
from .models import abc


# ob1 = abc()
# ob1.head ='CHOCOLATE'
# ob1.descr = 'SWEET'
# ob1.date = '02.10.10'
#
#
# ob2 = abc()
# ob2.head = 'PLACE'
# ob2.descr ='DUBAI'
# ob2.date = '01.02.14'

# objects=[ob1,ob2]
def home(request):
    objects = abc.objects.all()
    recent = abc.objects.order_by('-date')[0:3]
    return render(request, 'marketing-index.html', {'ob': objects,'re':recent})


def my(request):
    if request.method == 'POST':
        a = request.POST['firstname']
        b = request.POST['lastname']
        print(type(a),type(b))
        user = auth.authenticate(username=a, password=b)
        if user is not None:
            auth.login(request, user)
            return redirect('food:home')
        else:
            messages.error(request,'incorrect password or username')
            return redirect('food:my')


        # return render(request, 'marketing-index.html')
        # print(a, b)

    return render(request, 'my.html')


def logout(request):
    auth.logout(request)
    return redirect('food:home')



def register(request):

        if request.method == 'POST':
            a = request.POST['firstname']
            b = request.POST['lastname']
            c = request.POST['username']
            d = request.POST['password']
            e = request.POST['psw-repeat']
            f = request.POST['emailid']
            if d == e:
                if User.objects.filter(username=c).exists():
                    messages.error(request,'username already exists')
                    return redirect('food:register')
                elif User.objects.filter(email=f).exists():
                    messages.error(request,'email already exists')
                    return redirect('food:register')
                else:
                    v = User.objects.create_user(first_name=a,last_name=b,username=c,password=d,email=f,is_staff=True,is_superuser=False)
                    v.save()
                    auth.login(request,v)
            else:
               messages.error(request,'incorrect username or password')
               return redirect('food:register')
               # print(type(a), type(b),type(c),type(d))
            return redirect('food:home')
    # auth.register(request)
        return render(request ,'register.html')
def listing(request):
    object = abc.objects.all()
    paginator = Paginator(object, 5)

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'list.html', {'objects': 'objects'})
