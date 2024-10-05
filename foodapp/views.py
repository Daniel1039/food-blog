from django.shortcuts import render, get_object_or_404
from .models import Post
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.paginator import Paginator


from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

def post_list(request):
    posts= Post.objects.filter(status=1).order_by('-created_on')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    
    
    
    return render(request, 'post_detail.html', {'post': post})


def post(self, request):
    name= request.POST.get('name')
    email= request.POST.get('email')
    phone= request.POST.get('phone')
    subject= request.POST.get('subject')
    message= request.POST.get('message')
    created_on= request.POST.get('created_on')
    
    
    
   
    
    email = EmailMessage(
            subject= f"{name} from the developer.",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
     )
    email.send()
    return HttpResponse('email has been sent sucessfully')