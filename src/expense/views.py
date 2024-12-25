from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .forms import AddExpense
from .models import Expense
# from django.contrib.auth.mixins import UserPassesTestMixin


# def is_admin(user):
#     return user.is_authenticated and hasattr(user, "is_admin") and user.is_admin


class ExpenseView(View):
    def get(self, request):
        expenses = Expense.objects.order_by("name")
        
        context = {
            "expenses": expenses,
        }
        
        return render(
            request,
            "expense/index.html",
            context,
        )
        
class NewExpense(View):
    def get(self, request):
        form = AddExpense()
        title="Ajouter une dépense"
        submit_text = "Ajouter"
        
        context = {
            "form": form,
            "title": title,
            "submit_text": submit_text,
        }
        
        return render(
            request,
            "expense/new.html",
            context,
        )
    
    def post(self, request):
        form = AddExpense(request.POST)
        
        if form.is_valid():
            form.save()
            
            context={
                "form": form,
                "success": "Dépense ajoutée avec succès.",
            }
            
            return redirect("expense")
        else:
            print(form.errors)
            
            context={
                "form": form,
                "errors": form.errors,
            }
            
            return render(
                request,
                "expense/new.html",
                context
            )
            
            
        
class ExpenseUpdate(View):
    def get(self, request, pk):
        expense = Expense.objects.get(pk=pk)
        title=f"Mise à jour de la dépense"
        submit_text="Enregistrer"
        
        form = AddExpense(
            initial={
                "name": expense.name,
                "place": expense.place,
                "category": expense.category,
                "price": expense.price,
                "note": expense.note,
            }
        )
        
        context = {
            "form": form,
            "title": title,
            "submit_text": submit_text,
        }
        
        return render(
            request,
            "expense/new.html",
            context,
        )
        
    def post(self, request, pk):
        form = AddExpense(request.POST)
        
        if form.is_valid():
            form.save()
            
            context={
                "form": form,
                "success": "Dépense modifiée avec succès.",
            }
            
            return redirect("expense")
        else:
            print(form.errors)
            
            context={
                "form": form,
                "errors": form.errors,
            }
            
            return render(
                request,
                "expense/new.html",
                context
            )
            
class ExpenseDelete(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        expense = get_object_or_404(Expense, pk=pk)
        expense.delete()
        
        return redirect("expense")