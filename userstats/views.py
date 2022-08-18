from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
import datetime
from expenses.models import Expense

class ExpensesSummaryStats(APIView):
    def get_category(self,expense):
        return expense.category


    def get(self,request):
        todays_date = datetime.date.today()
        ayear_ago = todays_date - datetime.timedelta(days=365)
        expenses = Expense.objects.filter(owner = request.user, date__gte = ayear_ago,date_lte = todays_date)

        final = {}
        categories = list(set(map(self.get_category,expenses)))

        for expense in expenses:
            for category  in :
                final[expense.category] = expense.amount
            else:
                final[expense.category] += expense.amount

