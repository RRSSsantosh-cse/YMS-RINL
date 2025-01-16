from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib import messages

from django.template.loader import get_template

from io import BytesIO


# utils.py

from django.http import HttpResponse
from xhtml2pdf import pisa

def render_to_pdf(html):
    # Create a PDF document
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    
    # Generate PDF using HTML content
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('Error rendering PDF', status=500)
    return response
