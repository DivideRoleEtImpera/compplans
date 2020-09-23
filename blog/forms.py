from django import forms
from django.forms import ModelForm, Textarea,TextInput
from django.utils.translation import gettext_lazy as _

from .models import Plan

class PlanForm(forms.ModelForm):

    class Meta:
        model = Plan
        fields = ('code', 'program_name','program_sub_name','program_leader','year','description',)
        labels = {
            'code': _('Код плана'),
            'program_name': _('Направление'),
            'program_sub_name': _('Направленность'),
            'program_leader':_('Руководитель'),
            'year':_('Год'),
            'description':_('Описание'),
        }
        
        widgets = {
            'code': TextInput(attrs={'size': '20'}),
            'year':TextInput(attrs={'size': '4'}),
         	'program_name': TextInput(attrs={'size': '100'}),
            'program_sub_name': TextInput(attrs={'size': '100'}),
            'program_leader':TextInput(attrs={'size': '100'}),
            'description':Textarea(attrs={'cols': 80, 'rows': 10})
        }
        error_messages = {
            'code': {
                'max_length': _("Слишком длинный код. Длина кода не более 20 знаков"),
            },
        }