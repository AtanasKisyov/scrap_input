from django.shortcuts import render, redirect
from scrap_input.scrap_app.forms import ScrapTableForm
from scrap_input.scrap_app.helpers import get_scrapped_today


def home_page(request):
    return render(request, 'home.html')


def input_page(request):
    if request.method == 'POST':
        form = ScrapTableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('input')
    else:
        form = ScrapTableForm()
    scrapped_today = get_scrapped_today()
    context = {
        'form': form,
        'scrapped_today': scrapped_today,
    }
    return render(request, 'input.html', context)


def overview_page(request):
    return render(request, 'overview.html')
