from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Content

@login_required
def content_list(request):
    """List available content"""
    content_type = request.GET.get('type', 'all')
    
    if content_type == 'all':
        contents = Content.objects.all()
    else:
        contents = Content.objects.filter(content_type=content_type)
    
    context = {
        'contents': contents,
        'content_type': content_type,
    }
    return render(request, 'pages/content_list.html', context)

@login_required
def content_detail(request, id):
    """Display single content item"""
    content = Content.objects.get(id=id)
    context = {
        'content': content,
    }
    return render(request, 'pages/content_detail.html', context)
