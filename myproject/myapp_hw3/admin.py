from django.contrib import admin
from .models import User, Product, Order


@admin.action(description="Сбросить количество до нуля")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity_products', 'date_created', 'image')
    ordering = ('name', 'date_created')
    list_filter = ('name', 'price', 'date_created')
    search_fields = ['name', 'description']
    search_help_text = 'Поиск по полю "Название товара" и "Описание"'
    actions = [reset_quantity]
    actions = ['export_as_csv']

    readonly_fields = ['date_created']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Описание',
            {
                'classes': ['collapse'],
                'description': 'Описание товара',
                'fields': ['description'],
            },
        ),
        (
            None,
            {
                'fields': ['price', 'quantity_products', 'image', 'date_created'],
            },
        )
    ]


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'date_registered')
    ordering = ('name',)
    list_filter = ('name', 'address', 'date_registered')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'total_price', 'date_ordered')


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)



