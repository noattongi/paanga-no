from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import InvestorForm, TransactionForm
from .models import Investor

def index(request):
  return render(request, "index.html")

def loans(request):
  return render(request, "loans/index.html")

def investors(request):
  investors = Investor.objects.all()
  return render(request, "investors/index.html", {'investors': investors})

def new_investor(request):
  if request.method == 'POST':
    form = InvestorForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/investors')
    else:
      print(form.errors)
  else:
    form = InvestorForm()
  return render(request, "investors/new.html", {'form': form})

def show_investor(request, pk):
  investor = get_object_or_404(Investor, pk=pk)
  return render(request, "investors/show.html", {'investor': investor})

def new_transaction(request) :
  if request.method == 'POST':
    form = TransactionForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/transactions')
    else:
      print(form.errors)
  else:
    investor_id = request.GET.get('investor_id')

    if investor_id:
        try:
            investor_id = int(investor_id)
        except ValueError:
            investor_id = None

    form = TransactionForm(initial={"investor": investor_id})
  return render(request, "transactions/new.html", {'form': form})

def admin(request):
  return HttpResponse("Admin Page")

def login(request):
  return render(request, "login.html")