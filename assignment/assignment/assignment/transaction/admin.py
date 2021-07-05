from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django import forms
from .models import Modelspy, BranchMaster, DepartmentMaster, CompanyLedgerMaster, ArticleMaster, ColorMaster

class ModelspyAdminForm(forms.ModelForm):

    class Meta:
        model = Modelspy
        fields = '__all__'


class ModelspyAdmin(admin.ModelAdmin):
    form = ModelspyAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(Modelspy, ModelspyAdmin)


class BranchMasterAdminForm(forms.ModelForm):

    class Meta:
        model = BranchMaster
        fields = '__all__'


class BranchMasterAdmin(admin.ModelAdmin):
    form = BranchMasterAdminForm
    list_display = ['short_name', 'contact_person_name', 'gst_number', 'address1', 'pin_code', 'mobile']
    readonly_fields = ['short_name', 'contact_person_name', 'gst_number', 'address1', 'pin_code', 'mobile']

admin.site.register(BranchMaster, BranchMasterAdmin)


class DepartmentMasterAdminForm(forms.ModelForm):

    class Meta:
        model = DepartmentMaster
        fields = '__all__'


class DepartmentMasterAdmin(admin.ModelAdmin):
    form = DepartmentMasterAdminForm
    list_display = ['name']
    readonly_fields = ['name']

admin.site.register(DepartmentMaster, DepartmentMasterAdmin)


class CompanyLedgerMasterAdminForm(forms.ModelForm):

    class Meta:
        model = CompanyLedgerMaster
        fields = '__all__'


class CompanyLedgerMasterAdmin(admin.ModelAdmin):
    form = CompanyLedgerMasterAdminForm
    list_display = ['name', 'gst_number', 'supplier_status', 'address1', 'pin_code', 'mobile', 'remarks']
    readonly_fields = ['name', 'gst_number', 'supplier_status', 'address1', 'pin_code', 'mobile', 'remarks']

admin.site.register(CompanyLedgerMaster, CompanyLedgerMasterAdmin)


class ArticleMasterAdminForm(forms.ModelForm):

    class Meta:
        model = ArticleMaster
        fields = '__all__'


class ArticleMasterAdmin(admin.ModelAdmin):
    form = ArticleMasterAdminForm
    list_display = ['name', 'short_name', 'blend_pct', 'twists', 'remarks']
    readonly_fields = ['name', 'short_name', 'blend_pct', 'twists', 'remarks']

admin.site.register(ArticleMaster, ArticleMasterAdmin)


class ColorMasterAdminForm(forms.ModelForm):

    class Meta:
        model = ColorMaster
        fields = '__all__'


class ColorMasterAdmin(admin.ModelAdmin):
    form = ColorMasterAdminForm
    list_display = ['name', 'short_name', 'remarks']
    readonly_fields = ['name', 'short_name', 'remarks']

admin.site.register(ColorMaster, ColorMasterAdmin)


