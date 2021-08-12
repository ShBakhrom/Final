
from . import classifier as clsfr
# Create your views here.
from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .models import Quote, Images
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ImageForm, QuoteForm
from django.http import JsonResponse

def index(request):
    ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=1)

    if request.method == 'POST':
        quoteForm = QuoteForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())
    
    
        if quoteForm.is_valid() and formset.is_valid():
            quote_form = quoteForm.save(commit=False)
            quote_form.save()
            images = []
            for form in formset.cleaned_data:
                #this helps to not crash if the user   
                #do not upload all the photos
                if form:
                    image = form['image']
                    photo = Images(quote=quote_form, image=image)
                    photo.save()
                    images.append(photo)
            
            # print(images[0])
            
            
            request.session['msg'] = 'Upon checking the model has identified that '+quote_form.fistName+' '+quote_form.lastName+' '+clsfr.checkIfItsDogOrCat() 
            

            
            return redirect(request.path)
        else:
            print(postForm.errors, formset.errors)
        
    else:
        msg = request.session.get('msg', False)
        if ( msg ) : del(request.session['msg']) 
        quoteForm = QuoteForm()
        formset = ImageFormSet(queryset=Images.objects.none())

        
        
    
    return render(request, 'index.html',
                  {'quoteForm': quoteForm, 'formset': formset, 'message' : msg, })



