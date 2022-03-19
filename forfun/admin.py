from django.urls import path
from django.contrib import admin
from .models import Kid, Image
from django.core.mail import send_mail

class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('admin/', self.admin_view(self.index), name='index'),
        ]
        return custom_urls + urls
    
    def my_view(self, request):
        return HttpResponse('Hello from my view')

admin_site = CustomAdminSite()

@admin.action(description='Send email to parents')
def send_email(modeladmin, request, queryset):
    import pdb;
    pdb.set_trace()
    for obj in queryset:
        kid=obj.kid
        subject = 'Food for your child'
        message = f'Hi {user.username}, your kid\'s food was unrecognized.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [kid.email]
        send_mail( subject, message, email_from, recipient_list )



class AdminImages(admin.ModelAdmin):    
    fields = ( 'image_tag', )
    readonly_fields = ('image_tag',)

class AdminEmail(admin.ModelAdmin):
    list_display = ['image_url']
    ordering = ['image_url']
    actions = [send_email]
    fields=('kid', 'image_url', 'created_on', 'updated_on', 'is_approved', 'approved_by', 'food_group')
    readonly_fields = ['updated_on', ]

admin.site.register(Kid)
admin.site.register(Image,AdminEmail)