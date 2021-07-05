from django import forms
from .models import Modelspy, BranchMaster, DepartmentMaster, CompanyLedgerMaster, ArticleMaster, ColorMaster


class ModelspyForm(forms.ModelForm):
    class Meta:
        model = Modelspy
        fields = ['name']


class BranchMasterForm(forms.ModelForm):
    class Meta:
        model = BranchMaster
        fields = ['short_name', 'contact_person_name', 'gst_number', 'address1', 'pin_code', 'mobile']


class DepartmentMasterForm(forms.ModelForm):
    class Meta:
        model = DepartmentMaster
        fields = ['name']


class CompanyLedgerMasterForm(forms.ModelForm):
    class Meta:
        model = CompanyLedgerMaster
        fields = ['name', 'gst_number', 'supplier_status', 'address1', 'pin_code', 'mobile', 'remarks']


class ArticleMasterForm(forms.ModelForm):
    class Meta:
        model = ArticleMaster
        fields = ['name', 'short_name', 'blend_pct', 'twists', 'remarks']


class ColorMasterForm(forms.ModelForm):
    class Meta:
        model = ColorMaster
        fields = ['name', 'short_name', 'remarks', 'article']


