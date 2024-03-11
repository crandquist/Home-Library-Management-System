# views.py in the 'search' app
from django.shortcuts import render
from .search_client import make_microservice_request

def search_books(request):
    if request.method == 'POST':
        # Handle form submission
        author = request.POST.get('author', '')
        title = request.POST.get('title', '')
        results = make_microservice_request(author, title)
        return render(request, 'search_results.html', {'results': results})
    else:
        # Render the search form
        return render(request, 'search_form.html')
