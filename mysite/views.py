from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import render
import datetime
from mysite.forms import ContactForm
from django.core.mail import send_mail, get_connection

def hello(request):
    return HttpResponse("Hello World")

def current_datetime(request):
    now = datetime.datetime.now()
    # t = get_template('current_datetime.html')
    # html = t.render({'current_date':now})
    # return HttpResponse(html)
    print(request.META['HTTP_USER_AGENT'])
    return render(request, 'current_datetime.html', {'current_date':now})

def hours_ahead(request, *matches):
    offset = matches[0]
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'hours_ahead.html', {'hour_offset': offset, 'next_time': dt})

def test_matches(request, *matches):
    digits = matches[0]
    chars = matches[1]
    html = """
    <html>
    <body>
        digits: %s <br>
        chars: %s <br>
    </body>
    </html>
    """ % (digits, chars)
    assert False
    return HttpResponse(html)

def display_meta(request):
    values = request.META
    html = []
    for k in sorted(values):
        html.append("""
        <tr>
            <td>%s</td>
            <td>%s</td>
        </tr>
        """ % (k, values[k]))
    print(*html, sep='\n')
    return HttpResponse('<table>%s</table>' % ('\n'.join(html)))

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data 
            # this is how you send email using django (development process)
            # console.EmailBackend will print everything out to console 
            # for easier testing  
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                connection=con 
            )
            return HttpResponseRedirect('/contact/thank/')
    else:
        form = ContactForm(
            initial={'subject':'i love your site!'}
        )
    return render(request, 'contact/contact_form.html', {'form':form})

def contact_thank(request):
    return render(request, 'contact/thank.html')