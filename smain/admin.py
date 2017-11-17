from django.contrib import admin

from .models import SAuthUserDb, SAuthUserService, SDb, SLog, SQuery, SService, SType

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


class SQueryAdmin(admin.ModelAdmin):
    list_display = ('name', 's_service', 'priority')
    search_fields = ('name', 's_service__name')

class SAuthUserServiceAdmin(admin.ModelAdmin):
    list_display = ('auth_user', 's_service')
    search_fields = ('auth_user__username', 's_service__name')

class SAuthUserDbAdmin(admin.ModelAdmin):
    list_display = ('auth_user', 's_db')
    search_fields = ('auth_user__username', 's_db__name')

class SServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'checked')
    search_fields = ('name', )

admin.site.register(SAuthUserDb, SAuthUserDbAdmin)
admin.site.register(SAuthUserService, SAuthUserServiceAdmin)
admin.site.register(SDb, SDbAdmin)
admin.site.register(SLog, SLogAdmin)
admin.site.register(SQuery, SQueryAdmin)
admin.site.register(SService, SServiceAdmin)
admin.site.register(SType)