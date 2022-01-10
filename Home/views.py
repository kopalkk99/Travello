from django.shortcuts import render
from .models import Destination
# Create your views here.



dest1 = Destination('Bali','BALI description',789,'destination_1.jpg',True)
dest2 = Destination('Indonesia','Indonesia description',456,'destination_2.jpg',False)
dest3 = Destination('London','London description',445,'destination_3.jpg',False)
dest4 = Destination('New York','New York description',1234,'destination_4.jpg',True)

dest = [dest1,dest2,dest3,dest4]

def index(req):
    print(dest1.destName)
    dest = Destination.objects.all()
    return render(req,'index.html',{'dest':dest})
