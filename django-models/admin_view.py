# relationship_app/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import admin_required

@login_required
@admin_required
def admin_view(request):
    # Your view logic here
    return render(request, 'relationship_app/admin_view.html')



