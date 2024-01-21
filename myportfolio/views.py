from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'home.html')

def innerpage(request):
    return render(request, 'innerpage.html')

def pagedetail(request):
    if request.method =='post':
        first_name = request.post['first_name']
        last_name = request.post['last_name']
        email =request.post['email']
        Phone = request.post['Phone']
        message = request.post['message']
        #send email
        send_mail(
        'first_name',
        'last_name',
        'email',
        'Phone',
        ['dialloa626@yahoo.fr'],
        )
        print('your message were sent succsesfully')
        return render(request, 'pagedetail.html', {'first_name':first_name})
    else:
        return render(request, 'pagedetail.html', {})
