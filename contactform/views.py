from django.shortcuts import render
from contactform.forms  import TouchForm

# Create your views here.
def contactform(request):
    form = TouchForm()
    if request.method == 'Post':
        form = TouchForm(request.post)
        if form.is_valid():
            form.save(commit =True)
            return ()
        else:
            print('flase credential')
    return render(request, 'contactform/contactform.html', {'form':form})
