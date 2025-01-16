"""
URL configuration for yms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# IF WORKORDERS=N/A THEN WE HAVE TO FETHC FROM ERP AND VIEW MATERIALS HAS ZER0 MATERIALS
from django.contrib import admin
from django.urls import path
from cdy import views
from cdy.views import generate_pdf,upload_file
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_login, name='login'),
    path('home',views.Home,name="home"),
    path('rake',views.content,name="rake"),
    path('result<int:id>',views.rei,name="result"),
    path('value<int:id>',views.index,name="index"),
    path('test/<int:id>',views.test,name="test"),
    path('up/<int:id>',views.up,name="up"),
    path('fil<int:id>',views.fil,name="fil"),
    path('mat',views.mat,name="mat"),
    path('veh',views.veh,name="veh"),
    path('dev',views.dev,name="dev"),
    path('gp',views.gp,name="gp"),
    path('sy',views.sy,name="sy"),
    path('kilo',views.kilo,name='kilo'), 
    path('delte<int:id>',views.delte,name='delte'),
    path('mp',views.mp,name='mp'),
    path('rel',views.rel,name='rel'),
    path('dash',views.dash,name="dash"),
    path('scr',views.scr,name='scr'),
    path('sde',views.sde,name='sde'),
    path('fr',views.fr,name='fr'),
    path('delete/<int:id>/', views.delete_objects, name='delete_object'),
    path('generate-pdf/<int:object_id>/',generate_pdf,name='generate_pdf'),
    path('bin',views.bin,name='bin'),
    path('hok',views.hok,name='hok'),
    path('inb',views.inb,name='inb'),
    path('dis',views.dis,name='dis'),
    path('inbwork',views.inbwork,name='inbwork'),
    path('dellte/<int:id>/',views.dellte,name='dellte'), 
    path('materialp',views.materialp,name='materialp'), 
    path('srch',views.srch,name='srch'),
    path('prematerial',views.prematerial,name='prematerial'), 
    path('upload/', upload_file, name='upload_file'),
    path('prerake/',views.prerake,name='prerake'), 
   path('hooksearch',views.hooksearch,name='hooksearch'),
   path('hooksearchresults',views.hooksearchresults,name='hooksearchresults'),
path('logout',views.logout,name='logout'),
path('usr',views.usr,name='usr'),
path('map',views.map,name='map'),
path('wagontype',views.wagontype,name='wagontype'),
path('export/', views.export_page, name='export_page'),
    path('export/data/', views.export_to_csv, name='export_to_csv'), 
    path('dispatchtruck',views.dispatchtruck,name='dispatchtruck'),
    path('rakechallan',views.rakechallan,name='rakechallan'),
    path('captive',views.captive,name='captive'),
    path('fnote',views.fnote,name='fnote'),
    path('binsearch',views.binsearch,name='binsearch'),
    path('mps',views.mps,name='mps'),
    path('findetail',views.findetail,name='findetail'),
    path('hold',views.hold,name='hold'),
    path('cancelsearch',views.cancelsearch,name='cancelsearch'),
    path('indent',views.indent,name='indent'),
    path('holdmaster',views.holdmaster,name='holdmaster'),
     path('prerakeoutsearch',views.prerakeoutsearch,name='prerakeoutsearch'),
     path('prerakeverificationsearch',views.prerakeverificationsearch,name='prerakeverificationsearch'),
     path('locationhistory',views.locationhistory,name='locationhistory'),
     path('rakesearch',views.rakesearch,name='rakesearch'),
     path('layersearch',views.layersearch,name='layersearch'),
     path('changepassword',views.changepassword,name='changepassword'),
    path('inboundorder',views.inboundorder,name='inboundorder'),
    path('ord',views.ord,name='ord'),   
    path('test/drop/<int:id>',views.drop,name='drop'),
    path('test/finished/<int:id>',views.finished,name='finished'),
    path('finordersearch',views.finordersearch,name='finordersearch') ,
    path('maploc',views.maploc,name='maploc'),
    path('rok',views.rok,name='rok'),
    path('plat/<int:id>/',views.plat,name='plat'),
    path('generate-csv/', views.generate_csv, name='generate_csv'),
    path('generat-csv/', views.generat_csv, name='generat_csv'),
    path('memo/<int:id>',views.memo,name='memo'),
    path('rat/<int:id>',views.rat,name='rat'),
    path('ordie/<int:id>',views.ordie,name='ordie'),
    path('info',views.info,name='info'),
    path('updi',views.updi,name='updi'),
    path('truk/<int:id>',views.truk,name='truk'),
]
