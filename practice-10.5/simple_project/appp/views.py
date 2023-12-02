from django.shortcuts import render

# Create your views here.
def about(request):
    d={'lst':[1,2,3], 'age':2, 't':"jAil",'t2':"blah blah blah", 'dt':'datetime.datetime.now()', 'lst2':[
    {'name': 'zed', 'age': 19},
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
    ], 'val':123456789, 'name':'Naveen','line':["cat",
"dog",
"horse"],'textt':"asdlf ha shdg ljk shag la ;shdg flsah ;dg flsajkd hljhgf  j khdsafasdl hljkahgksfda hgjkdsah gjlshad fghdsjkg hjsfdjkhg sdfffffffffffffff fffffffffff fffffffffffffffffffffffffffffffffffg" }
 
    return render(request, 'about.html',d)