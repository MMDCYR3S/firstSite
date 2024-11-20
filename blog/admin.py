from django.contrib import admin
from blog.models import MyPost, Category

# Register models and use them.
#@admin.register(Category)
#@admin.register(MyPost)
class MyPostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date" # Show date time above database.
    empty_value_display = "-" # Show - if value of parameters are null.
    # fields = () # Only shows title or list of parameters we write there
    # and we only can change them
    list_display = ( "title", "author", "status", "counted_view", "created_date", "published_date")
    list_filter = ("status",)
    #ordering = ("title",)
    search_fields = ("title", "content")
    
admin.site.register(MyPost, MyPostAdmin)
admin.site.register(Category)

