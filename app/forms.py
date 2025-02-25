from django import forms
from .models import Investor, Transaction

class InvestorForm(forms.ModelForm):
  class Meta:
    model = Investor
    fields = ['first_name', 'last_name', 'phone']

class TransactionForm(forms.ModelForm):
  TRANSACTION_TYPE_CHOICES = (
    ('deposit', 'Deposit'),
    ('withdrawal', 'Withdrawal')
  )

  transaction_type = forms.ChoiceField(
    choices=TRANSACTION_TYPE_CHOICES,
    widget=forms.Select,
    label="Transaction Type"
  )

  class Meta:
    model = Transaction
    fields = ['investor','transaction_type','amount', 'notes']
    widgets = {
      'amount': forms.NumberInput(attrs={'min': '0'}),
      'notes': forms.Textarea()
    }

  def clean(self):
    cleaned = super().clean()
    amount = cleaned.get('amount')
    trans_type = cleaned.get('transaction_type')

    if amount is not None:
      if trans_type == 'withdrawal':
        cleaned['amount'] = -abs(amount)

    return cleaned
