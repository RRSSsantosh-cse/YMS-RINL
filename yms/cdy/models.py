from django.db import models
from django.utils import timezone

class Hook(models.Model):
    uid=models.IntegerField()
    platform=models.CharField(max_length=100,default='N/A') 
    h_number=models.CharField(max_length=150)
    Status=models.CharField(max_length=150,default='PLAN')
   
    count=models.CharField(max_length=150)
    class Meta:
        db_table="hook"
 
class Bund(models.Model):
    od=models.IntegerField()
    bno=models.CharField(max_length=20)

    class Meta :
        db_table="bund"

class Wagon(models.Model):
     uid=models.IntegerField()
     h_number=models.CharField(max_length=100)
     wname=models.CharField(max_length=100)
     cod=models.CharField(max_length=120)
     de=models.CharField(max_length=100)
     wt=models.CharField(max_length=100)
     
     stat=models.CharField(max_length=100)
     st=models.CharField(max_length=100)
     od=models.IntegerField()
     class Meta :
         db_table="wagon"   
class Rake(models.Model):
    pt=models.CharField(max_length=10) 
    ino=models.IntegerField()
    desti=models.CharField(max_length=30)
    stat=models.CharField(max_length=10)
    rcont=models.IntegerField()
    asgn=models.IntegerField()
    class Meta:
        db_table="rake"
class Wagn(models.Model):
     ino=models.IntegerField()
     dcode=models.CharField(max_length=5)
     wname=models.CharField(max_length=20)
     wtype=models.CharField(max_length=10)
     mcode=models.CharField(max_length=20)
     sto=models.CharField(max_length=10)
     stat=models.CharField(max_length=10)
     whealth=models.CharField(max_length=10)
     od=models.IntegerField()
     uid=models.IntegerField()
     class Meta:
         db_table="wagn"                

class Inb(models.Model):
    od=models.IntegerField(unique=True)  #workorder id
    dt=models.DateTimeField()            # generated time
        #inbound via hook,material preprocessing dispatch by rake
    ct=models.CharField(max_length=40)
    zone=models.CharField(max_length=50)    # drop zone
    sour=models.CharField(max_length=40)   # source
    bi=models.CharField(max_length=30)     # drop bin or ...
    truck=models.CharField(max_length=30)   # assigned truck
    asign=models.CharField(max_length=10)   # assigned by
    weight=models.CharField(max_length=20)  
    bns=models.CharField(max_length=40)
    tp=models.CharField(max_length=20)
    mcode=models.CharField(max_length=30)
    # we have bins(FOR inbound via hook) which is described as {wagon-name}-{hook no} like VSPCDY-034-2300003199
    # for rae dispatch  we have {wagonname}-{sqeuence}-{indentno}
    class Meta:
        db_table="inb"

class Rke(models.Model):
    od=models.IntegerField(unique=True)   #workorder id
    dt=models.DateTimeField()            # generated time
      #inbound via hook,material preprocessing dispatch by rake
    sour=models.CharField(max_length=40)   # source
    wname=models.CharField(max_length=20)
    zone=models.CharField(max_length=50)    # drop zone
    truck=models.CharField(max_length=30)   # assigned truck
    asign=models.CharField(max_length=10)   # assigned by
    weight=models.CharField(max_length=20)    #caluclated weight
    bn=models.CharField(max_length=10)
    # we have bins(FOR inbound via hook) which is described as {wagon-name}-{hook no} like VSPCDY-034-2300003199
    # for rae dispatch  we have {wagonname}-{sqeuence}-{indentno}
    class Meta:
        db_table="rke"

class Mp(models.Model):
    od=models.IntegerField()   #workorder id
    dt=models.DateTimeField()            # generated time
       #inbound via hook,material preprocessing dispatch by rake
    mcode=models.CharField(max_length=20)
    sour=models.CharField(max_length=40)   # source
    bi=models.CharField(max_length=30)     # drop bin or ...
    zone=models.CharField(max_length=50)    # drop zone
    truck=models.CharField(max_length=30)   # assigned truck
    asign=models.CharField(max_length=10)   # assigned by
    weight=models.CharField(max_length=20)    #caluclated weight
    bn=models.CharField(max_length=10)
    # we have bins(FOR inbound via hook) which is described as {wagon-name}-{hook no} like VSPCDY-034-2300003199
    # for rae dispatch  we have {wagonname}-{sqeuence}-{indentno}
    class Meta:
        db_table="mp" 




class Inboundtruck(models.Model):
   tname=models.CharField(max_length=30)
   cno=models.BigIntegerField()
   awt=models.DecimalField(max_digits=20,decimal_places=10)  
   mcode=models.BigIntegerField()
   mdesc=models.CharField(max_length=30)
   nm=models.IntegerField()
   dt=models.DateTimeField()
   ono=models.IntegerField()
    # for this bins will be same as the truck name
   class Meta:
        db_table="inboundtruck"  
class Truckdispatch(models.Model):
    od=models.IntegerField(unique=True)   #workorder id
    dt=models.DateTimeField()            # generated time
    val=models.CharField(max_length=40)    #inbound via hook,material preprocessing dispatch by rake
    zone=models.CharField(max_length=50)    # drop zone
    sour=models.CharField(max_length=40)   # source
    bi=models.CharField(max_length=30)     # drop bin or ...
    truck=models.CharField(max_length=30)   # assigned truck
    asign=models.CharField(max_length=10)   # assigned by
    #weight=models.CharField(max_length=20)    caluclated weight
    # we have bins(FOR inbound via hook) which is described as {wagon-name}-{hook no} like VSPCDY-034-2300003199
    # for rae dispatch  we have {wagonname}-{sqeuence}-{indentno}
    class Meta:
        db_table="truckdispatch"                

        
'''
class Gn(models.Model):
     ge=models.CharField(max_length=20)
     class Meta:
         db_table="gn"  

class Gen(models.Model):
    nam=models.CharField(max_length=20)
    gen=models.ManyToManyField(Gn)
    class Meta:
        db_table="gen"             
'''
class Hero(models.Model):
    nam=models.CharField(max_length=10)
    class Meta:
        db_table="hero"

class Heo(models.Model):
    nam=models.CharField(max_length=10)
    ct=models.CharField(max_length=10)
    mve=models.CharField(max_length=10)
    class Meta:
        db_table="heo"        


class Workoder(models.Model):
    od=models.IntegerField(unique=True)
    dt=models.DateTimeField()  
    stat=models.CharField(max_length=10)  # status
    class Meta:
        db_table="Od"
         
class Loc(models.Model):
   lid=models.CharField(max_length=10)  
   lstart=models.CharField(max_length=30)
   lend=models.CharField(max_length=30)
   c1=models.CharField(max_length=20)
   c2=models.CharField(max_length=10)
   stat=models.IntegerField()
   class Meta:
       db_table="loc"
# in workorder pick location is the starting value of lstart      

class User(models.Model):
    nam=models.CharField(max_length=200)
    gr=models.CharField(max_length=100)
    eid=models.CharField(max_length=100)
    password=models.CharField(max_length=100)  
    val=models.IntegerField()
    ac=models.IntegerField()    
    tme=models.DateTimeField(default=timezone.now)
    class Meta:
        db_table="user"
class Vehicle(models.Model):
    vid=models.CharField(max_length=10)
    vname=models.CharField(max_length=20)
    class Meta :
        db_table="vehicle"
        '''
class Cat(models.Model):
    oid=models.CharField(max_length=10)
    truck=models.CharField(max_length=10)
    ploc=models.CharField(max_length=20)
    assign=models.CharField(max_length=20)
    cate=models.CharField(max_length=30)
    class Meta:
        db_table="cat"
                        '''        
class Material(models.Model):
    mid=models.IntegerField()
    mcode=models.CharField(max_length=30)
    mdesc=models.CharField(max_length=30)
    aweight=models.CharField(max_length=30)
    cweight=models.CharField(max_length=30)
    cstock=models.CharField(max_length=30)
    ptype=models.CharField(max_length=30)
    crt=models.CharField(max_length=30) 
    dte=models.DateField()
    tm=models.TimeField()
    class Meta :
        db_table="material"
class Mt(models.Model):
    mid=models.IntegerField()
    mcode=models.CharField(max_length=30)
    mdesc=models.CharField(max_length=30)
    aweight=models.CharField(max_length=30)
    cweight=models.CharField(max_length=30)
    cstock=models.CharField(max_length=30)
    ptype=models.CharField(max_length=30)
    crt=models.CharField(max_length=30) 
    dte=models.DateField()
    tm=models.TimeField()
    mtype=models.CharField(max_length=30)
    secodedes=models.CharField(max_length=30)
    seccode=models.CharField(max_length=30)
    grcode=models.CharField(max_length=30)
    lcode=models.CharField(max_length=30)
    lcodedes=models.CharField(max_length=30)
    grcodedes=models.CharField(max_length=30)
    scodedes=models.CharField(max_length=30)
    class Meta :
        db_table="mt"        
      

class Gps(models.Model):
    tid=models.CharField(max_length=10)
    tname=models.CharField(max_length=20)
    tmax=models.CharField(max_length=10)
    gid=models.CharField(max_length=20)
    class Meta:
        db_table="gps"
class Device(models.Model):
    fid=models.IntegerField()
    nam=models.CharField(max_length=10)
    dip=models.CharField(max_length=30)
    typ=models.CharField(max_length=20)
    madd=models.CharField(max_length=30)
    X=models.IntegerField()
    Y=models.IntegerField()
    upd=models.CharField(max_length=10)
    class Meta:
        db_table="device"
class Bin(models.Model):
    # we obtain material desc from sync
    bname=models.CharField(max_length=10)  # bin name
    zone=models.CharField(max_length=40)  # zone
    lup=models.DateTimeField() #last updated
    lact=models.CharField(max_length=60)
    mtype=models.CharField(max_length=20)  # material sub type
    mcode=models.CharField(max_length=30)    # material code
    mq=models.CharField(max_length=20)  # quality
    mdesc=models.CharField(max_length=50)  # maertia descriptio 
    mlayers=models.IntegerField()      # layer limit
    mweight=models.CharField(max_length=30)     # weight limit

    class Meta:
        db_table="bin"

#we obtain bin name mcode mdesc configured for(mtype) mcount(materials on bin),weight limit and layers limit        
# user defined vehile name has truck id and vehicle name same from  gps 

'''
for work order group 

drop location -->{Drop Bin}|{Drop Zone}


'''
class Dispatch(models.Model):
    ono=models.IntegerField()
    tname=models.CharField(max_length=20)   # truck name
    dno=models.BigIntegerField()   # DDGP no   
    din=models.CharField(max_length=30)  #  DDGP item no
    ino=models.CharField(max_length=30)   # item no
    mcap=models.DecimalField(max_digits=20,decimal_places=10)     # max capacity
    mdesc=models.CharField(max_length=30)  # material desc
    ano=models.IntegerField()              # adjustment number
    avp=models.CharField(max_length=20)       # actual vs plan weight 
    sno=models.BigIntegerField()        # so sto number
    dq=models.DecimalField(max_digits=20,decimal_places=10)   # ddgp quantity
    mcode=models.CharField(max_length=30)   #material code
    dstatus=models.CharField(max_length=30)   #ddgp status
    ttime=models.DateTimeField()    # tare weight time
    class Meta:
        db_table="dispatch"


    


'''
in dispatch truck we print 
truck name,ddgp info as  {DDGP No}-{DDGP item No}-{SO STO No}-{Item no}
like 5023087217-000010-4992318517-0050



'''


# work order databases differ based on the type 
'''
class Inb(models.Model):
    wid=models.IntegerField()
    wname=models.CharField(max_length=20)
    plat=models.CharField(max_length=10)
    ino=models.CharField(max_length=10)
    class Meta:
        db_table="inb"
        # below is same for msterial processing and dispatch
class TD(models.Model):
    wid=models.IntegerField()
    bin=models.CharField(max_length=30)
    class Meta:
        db_table="td"

class Inb(models.Model):
    wid=models.IntegerField()
    wname=models.CharField(max_length=20)
    class Meta:
        db_table="inb"
class TD(models.Model):
    wid=models.IntegerField()
    wname=models.CharField(max_length=20)
    class Meta:
        db_table="td"  
'''        
class Mcode(models.Model):
    wid=models.IntegerField()
    mcode=models.IntegerField()
    class Meta:
        db_table="mcode"        

class Mtu(models.Model):
    val=models.CharField(max_length=10)
    nam=models.CharField(max_length=20)
    class Meta:
        db_table="mtu"      
class YourModel(models.Model):
    nam=models.CharField(max_length=10)
    class Meta:
        db_table="yourmodel"   
class Map(models.Model):
    strt=models.CharField(max_length=20)
    x=models.IntegerField()
    y=models.IntegerField()
    ed=models.CharField(max_length=20)
    class Meta:
        db_table="map"               
class Mseg(models.Model):
    val=models.CharField(max_length=200)
    t=models.DateTimeField(default="0:0:00 12-2-2000")
    c=models.CharField(max_length=10)
    class Meta:
        db_table="mseg"        
class Ordstat(models.Model):
      worder=models.IntegerField()
      val=models.IntegerField()
      class Meta:
          db_table="ordstat"     