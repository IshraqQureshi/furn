from django.http import HttpResponse
from django.shortcuts import render
from apps.products.models import Product
from apps.reviews.models import Review
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string


# Create your views here.
def index(req):

    data = {
        'title': 'Homepage'
    }

    product_objs = Product.objects.all()
    products = product_objs.filter(isFeatured=0)[:8]
    featured_product = product_objs.filter(isFeatured=1).prefetch_related('review_set')

    data['products'] = products
    
    data['featured_product'] = featured_product

    return render(req, 'homepage/index.html', data)

def contact(req):
    contactForm = ContactForm()
    return render(req, 'contact/index.html', {
        'contactForm': contactForm
    })

def contactSubmit(req):

    if req.method == 'POST':
        form = ContactForm(req.POST)

        if form.is_valid():

            emailData = {
                'first_name': req.POST['first_name'],
                'last_name': req.POST['last_name'],
                'email': req.POST['email']
            }

            email_html = render_to_string('emails/contact.html', emailData)

            send_mail(
                'Contact Form',
                'Thank you for contact us',
                'norply@furn.com',
                ['ishraq.aslam@yopmail.com'],
                fail_silently=False,
                html_message=email_html
            )
            return HttpResponse('Mail Sent')
        else:
            return render(req, 'contact/index.html', {
                'contactForm': form
            })  
    else:
        return HttpResponse('<p>Method Not Accepted</p>')
