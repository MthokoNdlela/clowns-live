from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm


def troupe(request):
	order = Order.objects.all()
	customers = Client.objects.all()

	total_customers = customers.count()

	total_orders = order.count()
	delivered = order.filter(status='Delivered').count()
	pending = order.filter(status='Pending').count()

	context = {'orders':order, 'Client':customers,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending }

	return render(request, 'users/dashboard.html', context)

def clowns(request):
	products = Clown.objects.all()

	return render(request, 'users/clown.html', {'products':products})

def clients(request, pk_test):
	customer = Client.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()

	context = {'customer':customer, 'orders':orders, 'order_count':order_count}
	return render(request, 'users/clients.html',context)

def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'users/order_form.html', context)

def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'users/order_form.html', context)

def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'users/delete.html', context)