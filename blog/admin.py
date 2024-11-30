from django.contrib import admin
from blog.models import MyPost, Category , Comment
from django_summernote.admin import SummernoteModelAdmin

# Register models and use them.
#@admin.register(Category)
#@admin.register(MyPost)
class MyPostAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date" # Show date time above database.
    empty_value_display = "-" # Show - if value of parameters are null.
    # fields = () # Only shows title or list of parameters we write there
    # and we only can change them
    list_display = ( "title", "author", "status", "login_required","counted_view", "created_date", "published_date")
    list_filter = ("status",)
    #ordering = ("title",)
    search_fields = ("title", "content")
    summernote_fields = ("content",)
    
    
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date" # Show date time above database.
    empty_value_display = "-" # Show - if value of parameters are null.
    # fields = () # Only shows title or list of parameters we write there
    # and we only can change them
    list_display = ( "name", "applied", "subject", "created_date", "updated_date")
    list_filter = ("applied",)
    #ordering = ("title",)
    search_fields = ("name", "post")
    summernote_fields = ("content",)

admin.site.register(MyPost, MyPostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)

