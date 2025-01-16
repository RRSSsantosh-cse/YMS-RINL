from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import * 
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from django.views.generic import View
from yms.utils import render_to_pdf
import datetime
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login
import pandas as pd
import csv

# Create your views here.
def generate_csv(request):
    # Query your database to fetch data (example query)
    queryset = Hook.objects.all()

    # CSV column headers (example: replace with your field names)
    headers = ['platform', 'h_number', 'Status','count']

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    # Create CSV writer
    writer = csv.writer(response)
    writer.writerow(headers)

    # Write data rows to CSV file
    for obj in queryset:
        row = [getattr(obj, field) for field in headers]
        writer.writerow(row)
    return response
    return redirect(reverse('home'))
def generat_csv(request):
    header_values = ["PLATFORM", "INDENT NUMBER", "DESTINATIONS", "STATUS", "WAGONCOUNT"]

 
    queryset = Rake.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="rake.csv"'
    writer = csv.writer(response)
    writer.writerow(header_values)
    for obj in queryset:
        # Extract data values corresponding to the header values
        row_values = [obj.pt, obj.ino, obj.stat, obj.desti, obj.rcont]
        writer.writerow(row_values)

    return response
def Home(request):
    f=Hook.objects.all() 
    kl=User.objects.get(val=1)
    l=kl.tme.strftime("%d/%m/%Y %H:%M:%S")
    ms=Mseg.objects.all().order_by('-t')
    return render(request,'cdy/admin.html',{'f':f,'kl':kl,'k12':l,'ms':ms})
def index(request,id):
     li={}
     lo={}
     f=Hook.objects.all() 
     st=Hook.objects.get(pk=id)
     x=st.h_number
     studi=Wagon.objects.filter(h_number=st.h_number)
     mi = Wagon.objects.filter(h_number=st.h_number).values_list('wname', flat=True).distinct()
     distinct_wnames = Wagon.objects.filter(h_number=st.h_number).values_list('wname', flat=True).distinct()
     z1=Wagon.objects.all()
     k2 = []
     for wname in distinct_wnames:
          wagon = Wagon.objects.filter(h_number=st.h_number).filter(wname=wname).first()
          if wagon:
              k2.append(wagon)
     l2={}
     for d1 in k2:
         for y in mi:
            li[y] = set(Wagon.objects.filter(h_number=st.h_number).filter(wname=y))
     kl=User.objects.get(val=1)
     l=kl.tme.strftime("%d/%m/%Y %H:%M:%S")
     ms=Mseg.objects.all().order_by('-t')
     lpu=st.platform;       
     return render(request,'cdy/admin.html',{'f':f,'k':studi,'x':x,'li':li,'k2':k2,'z1':z1,'kl':kl,'ms':ms,'k12':l,'lpu':lpu})
def content(request):
     f=Rake.objects.all()
     return render(request,"cdy/rake.html",{"f":f})
def fil(request,id):
     f=Rake.objects.all()
     st=Rake.objects.get(pk=id)
     x=st.ino 
     studi=Wagn.objects.filter(ino=x)
     mi = Wagn.objects.filter(ino=x).values_list('wname', flat=True).distinct()
     distinct_wnames = Wagn.objects.filter(ino=x).values_list('wname', flat=True).distinct()
     z1=Wagn.objects.all()
     k2 = []
     for wname in distinct_wnames:
          wagon = Wagn.objects.filter(ino=x).filter(wname=wname).first()
          if wagon:
              k2.append(wagon)
     l2={}
     l3={}
     for d1 in k2:
         for y in mi:
            l2[y] = set(Wagn.objects.filter(ino=x).filter(wname=y))
            l3[y]=set(Wagn.objects.filter(ino=x).filter(wname=y).values_list('dcode',flat='True'))


     kjm=st.asgn
     return render(request,'cdy/rake.html',{'f':f,'k':studi,'x':x,'l2':l2,'l3':l3,'k2':k2,'kjm':kjm})
def rei(request,id):
     
     return render(request,"cdy/result.html",{"l":5})
# no elements are inserted in chronology order so for loop fails try to use join or manytomany fields
#for accessing multiple values base don single values
def rel(request):
   q=Hero.objects.all()
   r=Heo.objects.all()
   


   return render(request,'cdy/duplicate.html',{'q':q,'r':r}) 


'''
nam-->hero-->gabbar,rubber
__--->director-->jalsa,rabasa

and avoid duplicates
def your_view_function(request): current date filter 
    # Get the current date
    current_date = date.today()

    # Filter records based on the current date
    filtered_records = YourModel.objects.filter(date_field=current_date)

    # Pass the filtered records to a template for rendering
    return render(request, 'your_template.html', {'records': filtered_records})


'''
def fr(request):
    items = YourModel.objects.all()
    return render(request, 'cdy/objdelete.html', {'items': items})
def delete_objects(request,id):
    item = YourModel.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect(reverse('fr'))
def test(request,id):
      # work orders are filters based on order 
     q=Wagon.objects.filter(od=id)
     
     l=id 
     m=Inb.objects.filter(od=id)
     l1={}
     x="INBOUND VIA HOOK"
     l1[l]=Bund.objects.filter(od=l).values_list('bno')
     k4=Loc.objects.filter(lid=l)
     kr=Loc.objects.filter(lid=l)
     kn=request.META.get('HTTP_REFERER', None)
     lk={}
     prev_obj = None
     for current_obj in k4:
        lk[current_obj] = prev_obj
        prev_obj = current_obj 
         
     return render(request,"cdy/test.html",{'y':m,'l':l,'id':id,'l1':l1,'x':x,'k4':k4,'kn':kn,'kr':kr,'lk':lk})
def up(request,id):
   
     l=Wagon.objects.get(pk=id)
     q=l.h_number
     f=l.wname
     k=Wagon.objects.filter(h_number=q).values('wname')  # extraction of values based on certain values
     return render(request,"cdy/tst.html",{'k':k,'f':f,'q':q})
def mat(request):
     k=Mt.objects.all()
     return render(request,'cdy/material.html',{'k':k})
def veh(request):
     f=Vehicle.objects.all()
     return render(request,"cdy/vehicle.html",{"f":f})
def dev(request):
     f=Device.objects.all()
     return render(request,"cdy/device.html",{"f":f})
def gp(request):
     f=Gps.objects.all()
     return render(request,"cdy/gps.html",{"f":f})
def sy(request):
     k=Mt.objects.all()
     return render(request,'cdy/sync.html',{'k':k})
     
def kilo(request):
     k=Workoder.objects.all().order_by('-dt').values() # ascending order based on time     
     return render(request,'cdy/time.html',{'k':k})    
def delte(request,id):
     k=Hook.objects.get(pk=id)
     k.delete()
     return HttpResponseRedirect(reverse('home'))
def dellte(request,id):
     k1=Inb.objects.get(pk=id)
     k1.delete()
     return HttpResponseRedirect(reverse('inbwork'))
def gal(request):
     k=Hook.objects.all()

def mp(request):
    k=Mp.objects.all()
    return render(request,'cdy/mprocess.html',{'k':k})
def dash(request):
     t=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
     ti=datetime.date.today().strftime("%d-%m-%Y")
     return render(request,'cdy/dashboard.html',{'t':t,'ti':ti})
def scr(request):
     w=Mtu.objects.all()
     return render(request,'cdy/scriptwork.html',{'w':w})
def sde(request):
     return render(request,'cdy/sidemenu.html')
def sma(request):
      return render(request,'cdy/print.html')
# views.py
def bin(request):
     return render(request,'cdy/bin.html')
def hok(request):
     k=Hook.objects.all().values_list('platform').distinct().exclude(platform='N/A')
     l1={}
     l2={}
   

     distinct_wnames = Hook.objects.values_list('platform', flat=True).distinct()
   
     mi = Hook.objects.values_list('platform', flat=True).distinct()
  
     k12 = []
     for plat in distinct_wnames:
          platf = Hook.objects.filter(platform=plat).first()
          if platf:
              k12.append(platf)
   
     for d1 in k12:
         for y in mi:
            l1[y] = set(Hook.objects.filter(platform=y).values_list('h_number'))
     mii = Wagon.objects.values_list('h_number', flat=True).distinct()
  
     
     k121 = []
     distinct_hnames = Wagon.objects.values_list('wname', flat=True).distinct()
 
     l12={}
     for plat in distinct_hnames:
          platf = Wagon.objects.filter(wname=plat).first()
          if platf:
              k121.append(platf)
   
     
          for y in mii:
              for z in mii:
                  l12[y] = set(Wagon.objects.filter(h_number=y).values_list('wname'))     

     return render(request,'cdy/hookdisplay.html',{'l1':l1,'l2':l12})



def inb(request):
     k=Inboundtruck.objects.all()
     return render(request,'cdy/inboundtruck.html',{'f':k})
def dis(request):
     l=Dispatch.objects.all()
     return render(request,'cdy/dispatch.html',{'f':l})
def extract_last_word(text):
    tokens = text.split('-')
    last_word = tokens[-1]
    return last_word

def generate_pdf(request, object_id):
    # Retrieve the object from the database
    obj = get_object_or_404(Inb, pk=object_id)
    
    # Render the template with the object data
    context = {'k': obj}
    html = render_to_string('cdy/rakecertificate.html', context)
    
    # Generate the PDF
    pdf = render_to_pdf(html)
    
    # Prepare the HTTP response with the PDF content
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = f"PDF_{obj.id}.pdf"  # Use object ID in the filename
        content = f"inline; filename={filename}"
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Page Not Found")
def inbwork(request):
    current_date = datetime.date.today()
    k=Inb.objects.filter(dt__date=current_date).order_by('-dt').values()
    d=Inb.objects.filter(ct="INBOUND VIA HOOK")
    m={}
    for x in d:
        m[x]=Hook.objects.filter(h_number=extract_last_word(x.bns)).values_list('platform')
    return render(request,'cdy/inboundworkorder.html',{'k':k,'d':m})
def materialp(request):
     return render(request,'cdy/materialp.html')   
def srch(request):
    return render(request,'cdy/dispatchtruckhistorysearch.html')
def prematerial(request):
    return render(request,'cdy/prerakeoutmaterialsearch.html');  


def upload_file(request):
    if request.method == 'POST' and request.FILES.get('myfile'):
        myfile = request.FILES['myfile']
        
        # Process the uploaded Excel file
        process_excel_file(myfile)
        
        return HttpResponseRedirect('/')

    return render(request, 'cdy/upload.html')

def process_excel_file(file):
    df = pd.read_excel(file)
    for index, row in df.iterrows():
        Hero.objects.create(
            nam=row['name'],
            
        )
def prerake(request):
     k=Rake.objects.exclude(pt='N/A')
     return render(request,'cdy/prerake.html',{'k':k})

def hooksearch(request):
    return render(request,'cdy/hookorderssearch.html')        

def hooksearchresults(request):
    if request.method == 'POST':
        l= request.POST.get('hook_no_operator')
        k=request.POST.get('hook_no_value')
        if k:
          return render(request,'cdy/hookorders.html',{'k':k})
        else:
          return render(request,'cdy/admin.html')
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        passw = request.POST['password']
        f= User.objects.filter(nam=username)
        user=f.filter(password=passw)
        t=datetime.datetime.now()
        l=t.strftime("%d-%m-%Y %H:%M:%S")
        if user:
            f.update(val=1)
            f.update(tme=t)
            return redirect('/home')  # Redirect to a dashboard or home page
        else:
            # Handle invalid login
            return render(request, 'cdy/login.html', {'error': 'NOT VALID'})

    return render(request, 'cdy/login.html')       
def logout(request):
    k=User.objects.filter(val=1)
    k.update(val=0)
    return redirect('/') 
def usr(request):
    k=User.objects.all()
    return render(request,'cdy/user.html',{'f':k})
def map(request):
    t=request.GET.get('source')
    q=request.GET.get('destination')
    m=Map.objects.filter(strt=t,ed=q) or Map.objects.filter(strt=q,ed=t)  
    
    return render(request,'cdy/ymsmap.html',{'t':t,'q':q,'m':m})
def wagontype(request):
    return render(request,'cdy/wagontype.html')
def export_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    # Retrieve data from the database (e.g., YourModel queryset)
    queryset = Hook.objects.all()

    # Create a CSV writer object
    writer = csv.writer(response)

    # Write header row
    header_row = [field.name for field in Hook._meta.fields]
    writer.writerow(header_row)

    # Write data rows
    for obj in queryset:
        row = [getattr(obj, field) for field in header_row]
        writer.writerow(row)

    return response
def export_page(request):
    return render(request, 'cdy/export.html')
def dispatchtruck(request):
    return render(request,'cdy/dispatchtruckhistorysearch.html')
def rakechallan(request):
    return render(request,'cdy/rakechallangrosssearch.html')
def captive(request):
    return render(request,'cdy/captivetruck.html')
def fnote(request):
    return render(request,'cdy/fnotesearch.html')
def binsearch(request):
    return render(request,'cdy/binlocationhistorysearch.html')
def mps(request):
    return render(request,'cdy/mpreportsearch.html')
def findetail(request):
    return render(request,'cdy/finishdetailsearch.html')
def hold(request):
    return render(request,'cdy/holdwagonsearch.html')
def cancelsearch(request):
    return render(request,'cdy/cancelledsearch.html')
def indent(request):
    return render(request,'cdy/indentdispatchymssearch.html')
def holdmaster(request):
    return render(request,'cdy/hold.html')
def prerakeoutsearch(request):
    return render(request,'cdy/prerakeoutsearch.html')
def prerakeverificationsearch(request):
    return render(request,'cdy/prerakeoutverificationsearch.html')
def locationhistory(request):
    return render(request,'cdy/locationhistorysearch.html')
def rakesearch(request):
    return render(request,'cdy/rakeorderssearch.html')
def layersearch(request):
    return render(request,'cdy/layerreportsearch.html')
def changepassword(request):
  if request.method == 'POST':
    t=request.POST.get('new_password')
    kl=User.objects.filter(val=1)
    kl.update(password=t)
  return HttpResponseRedirect(reverse('home'))  
def inboundorder(request):
    return render(request,'cdy/inboundhookorder.html')
def ord(request):
    return render(request,'cdy/order.html')
def drop(request,id):
    f=Loc.objects.get(pk=id)
    f.stat=2
    f.save()

    redirect_url = reverse('test', args=[f.lid])
    return HttpResponseRedirect(redirect_url)
def finished(request,id):
    f=Loc.objects.get(pk=id)
    f.stat=3
    f.save()

    redirect_url = reverse('test', args=[f.lid])
    return HttpResponseRedirect(redirect_url)

def finordersearch(request):
    return render(request,'cdy/finishorderssearch.html')
def maploc(request):
     if request.method == 'POST':
       t=request.POST.get('source')
       q=request.POST.get('destination')
       
     return HttpResponseRedirect(reverse('map') + f'?source={t}&destination={q}')
def rok(request):
     k=Rake.objects.all().values_list('pt').distinct().exclude(pt='N/A')
     l1={}
     l2={}
   

     distinct_wnames = Rake.objects.values_list('pt', flat=True).distinct().exclude(pt='N/A')
     z1=Rake.objects.all()
     mi = Rake.objects.values_list('pt', flat=True).distinct().exclude(pt='N/A')
     k12 = []
     for plat in distinct_wnames:
          platf = Rake.objects.filter(pt=plat).first()
          if platf:
              k12.append(platf)
   
     for d1 in k12:
         for y in mi:
            l1[y] = set(Rake.objects.filter(pt=y).values_list('ino'))
     mii = Wagn.objects.values_list('ino', flat=True).distinct()
     
     k121 = []
     distinct_hnames = Wagn.objects.values_list('wname', flat=True).distinct()
     l12={}
     for plat in distinct_hnames:
          platf = Wagn.objects.filter(wname=plat).first()
          if platf:
              k121.append(platf)
   
     
          for y in mii:
              for z in mii:
                  l12[y] = set(Wagn.objects.filter(ino=y).values_list('wname'))     

     return render(request,'cdy/rakemonitor.html',{'l1':l1,'l2':l12})
def plat(request, id):
    print(f"Request method: {request.method}")
    if request.method == 'POST':
        k = Hook.objects.get(pk=id)
        m = request.POST.get('namq'+str(k))
        if m:
            k.platform = m
            k.Status = "RAKE_ARRIVED"
            k.save()
            return redirect('home')
    return redirect('home') 
             # Redirect to the 'home' URL
def rat(request, id):
    print(f"Request method: {request.method}")
    if request.method == 'POST':
        k = Rake.objects.get(pk=id)
        m = request.POST.get('namq'+str(k))
        if m:
            k.pt = m
            k.desti = "PLAN_CONFIRMED"
            k.save()
            return HttpResponseRedirect(reverse('rake')) 
    return HttpResponseRedirect(reverse('rake'))           

    # Handle GET request or invalid POST request
def memo(request,id):
    ba=Rake.objects.get(pk=id)
    ba.desti="PLAN"
    ba.save()
    return HttpResponseRedirect(reverse('rake')) 
 
def ordie(request,id):
    bu=Rake.objects.get(pk=id)
    bu.asgn=1 
    bu.desti="WO_CREATED"
    bu.save()
    return HttpResponseRedirect(reverse('rake')) 
def info(request):
    k=3
    l="green"
    return render(request,'cdy/hookdisplay.html',{'kpl':k,'lpl':l})    
def updi(request):
     if request.method == 'POST':
        selected_group = request.POST.get('vsp')
        # Process the selected_group here, such as saving it to the database
        kn=request.META.get('HTTP_REFERER', None)
        f=User.objects.get(val=1)
        f.gr=selected_group 
        f.save()
        return redirect(request.META.get('HTTP_REFERER', 'cdy/home.html'))
     else:
         return render(request, 'cdy/home.html')
def truk(request,id):
    m=Inboundtruck.objects.get(pk=id)
    k=Inb.objects.get(truck=m.tname)
    if k:
        m.ono=k.od 
        m.save()
        return HttpResponseRedirect(reverse('inb'))
    else:
        return HttpResponseRedirect(reverse('inb'))