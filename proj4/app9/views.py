from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.http import urlencode
from .forms import FigureForm
from num2words import num2words

def converter(amount):
    return num2words(amount, lang='en_IN').title()  # Convert to words and capitalize each word

def converted(request):
    if request.method == 'POST':
        form = FigureForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            words = converter(amount)
            query_string = urlencode({'amount': amount, 'words': words})
            return redirect(f'{reverse("cheque_print")}?{query_string}')
    else:
        form = FigureForm()
    return render(request, 'index.html', {'form': form})

def cheque_print(request):
    amount = request.GET.get('amount')
    words = request.GET.get('words')
    context = {'amount': amount, 'words': words}
    return render(request, 'cheque.html', context)