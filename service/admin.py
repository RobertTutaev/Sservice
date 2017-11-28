from django.contrib import admin

from .models import SUserDb, SUserService, SDb, SLog, SQuery, SService, SType, SPage

class SDbAdmin(admin.ModelAdmin):
    list_display = ('name', 'p_host', 'p_name', 'checked')
    search_fields = ('name', 'p_host', 'p_name', 'checked')

class SLogAdmin(admin.ModelAdmin):
    list_display = ('info', 'dt')
    search_fields = ('info', 'dt')
    readonly_fields = ('info', 'dt')   

    def get_actions(self, request):
        actions = super(SLogAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_add_permission(self, request):
        return False

    #def has_change_permission(self, request, obj=None):
    #    return False

    def has_delete_permission(self, request, obj=None):
        return False

class SPageAdmin(admin.ModelAdmin):
    fields = ('name', 'content', 'user')
    list_display = ('name', 'user')
    search_fields = ('name',)
    readonly_fields = ('name', 'user')

    def save_model(self, request, obj, form, change):
        #if not change:
        obj.user = request.user
        obj.save()

    def get_actions(self, request):
        actions = super(SPageAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class SQueryAdmin(admin.ModelAdmin):
    list_display = ('name', 's_service', 'priority')
    search_fields = ('name', 's_service__name')

class SUserServiceAdmin(admin.ModelAdmin):
    list_display = ('user', 's_service')
    search_fields = ('user__username', 's_service__name')

class SUserDbAdmin(admin.ModelAdmin):
    list_display = ('user', 's_db')
    search_fields = ('user__username', 's_db__name')

class SServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'checked')
    search_fields = ('name', )

admin.site.register(SUserDb, SUserDbAdmin)
admin.site.register(SUserService, SUserServiceAdmin)
admin.site.register(SDb, SDbAdmin)
admin.site.register(SLog, SLogAdmin)
admin.site.register(SQuery, SQueryAdmin)
admin.site.register(SService, SServiceAdmin)
admin.site.register(SPage, SPageAdmin)
admin.site.register(SType)