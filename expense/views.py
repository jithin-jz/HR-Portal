from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Expense

@login_required(login_url='/login/')
def manage_expenses(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        name = request.POST.get('name', '').strip()
        category = request.POST.get('category', 'Other')
        price = request.POST.get('price', '0').strip()

        try:
            price = float(price)
        except ValueError:
            price = 0

        if action == 'add' and name and price > 0:
            Expense.objects.create(user=request.user, name=name, category=category, price=price)
            messages.success(request, "Expense added successfully!")
        elif action == 'delete':
            expense_id = request.POST.get('expense_id')
            expense = get_object_or_404(Expense, id=expense_id, user=request.user)
            expense.delete()
            messages.success(request, "Expense deleted successfully!")
        else:
            messages.error(request, "Invalid action or missing data.")

    # Fetch user's expenses and calculate the total
    expenses = Expense.objects.filter(user=request.user).order_by('-date_added')
    total_expenses = sum(expense.price for expense in expenses)

    context = {
        'expenses': expenses,
        'total_expenses': total_expenses,
        'categories': Expense.CATEGORY_CHOICES,
    }
    return render(request, 'expense.html', context)
