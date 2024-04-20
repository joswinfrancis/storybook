from django.shortcuts import render,get_object_or_404
from .models import Story,Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.
def story_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    story = Story.objects.all()
    paginator = Paginator(story,4)
    page = request.GET.get('page')
    try:
        story=paginator.page(page)
    except PageNotAnInteger:
        story=paginator.page(1)
    except EmptyPage:
        story=paginator.page(paginator.num_pages)
    if category_slug:
        story = Story.objects.all()
        category = get_object_or_404(Category,slug=category_slug)
        story = story.filter(category=category)
        paginator = Paginator(story,2)
        page = request.GET.get('page')
        try:
            story=paginator.page(page)
        except PageNotAnInteger:
            story=paginator.page(1)
        except EmptyPage:
            story=paginator.page(paginator.num_pages)
        
    return render(request,'story_list.html',{
        'categories':categories,
        'story':story,
        'category':category,
        'page':page
    })

def story_detail(request,id):
    story = get_object_or_404(Story,id=id)
    return render(request,'story_detail.html',{'story':story})

def search_story(request):
    query=None
    results = []
    if request.method=="GET":
        query=request.GET.get("search")
        if query is not None:
            results = Story.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    return render(request, 'search.html', {'query':query, 'results':results})