from django.shortcuts import render,get_object_or_404
from .models import Gallery,Profile,Header,Bio,Inquiry
from .forms import ContactForm,InquiryForm

# Create your views here.

def index(request):
    avi = Profile.objects.all()
    head = Header.objects.all()
    bio = Bio.objects.all()
    context = {
        'avi' : avi,
        'head' : head,
        'bio' : bio
    }
    return render(request,"index.html",context)

def gallery(request):
    data = Gallery.objects.all()
    context = {
        'data' : data
    }
    return render(request,"gallery.html",context)

""" def booking(request):
    context = {}
    context['form'] = ContactForm
    return render(request,"booking.html",context) """

def booking(request):
    #inquiry = get_object_or_404(Inquiry)
    new_inquiry = None

    if request.method == 'POST':
        inquiry_form = InquiryForm(data=request.POST)
        
        if inquiry_form.is_valid():
            # Create Comment object but don't save to database yet
            new_inquiry = inquiry_form.save(commit=False)
            # Assign the current inquiry to the comment
            #new_inquiry.inquiry = inquiry
            #Save inquiry to database
            new_inquiry.save()
        
    else:
        inquiry_form = InquiryForm()
    
    context = {}
    context['form'] = InquiryForm
    
    return render(request, "booking.html",context)