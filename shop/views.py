from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Quote
from .forms import QuoteForm

# Create your views here.
def main_page(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('main_page')
    else:
        form = QuoteForm()
    return render(request, 'shop/main_page.html', {'form': form})