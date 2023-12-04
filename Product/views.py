from django.shortcuts import render
from OrderAPI.models import Logger

# Create your views here.
# views.py

def see(request):
    query = request.GET.get('q')  # Retrieve the search query from the URL parameter 'q'
    results = []
    
    if query:
        # Perform the search based on the query using Django's ORM (assumes a case-insensitive search on the 'name' field)
        results = Logger.objects.filter(name__icontains=query)
    
    return render(request, 'search.html', {'results': results, 'query': query})

