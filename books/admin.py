from django.contrib import admin
from .models import Publisher, Author, Book

# ------------------- admin customization --------------------- 
# admin customization for model Author 
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

# admin customization for model Book 
class BookAdmin(admin.ModelAdmin):
    # custom list change
    list_display = ('title', 'publisher', 'pub_date')
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
    fields = ('title', 'publisher', 'authors')
    # custom edit/add form
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)

# ------------------- model registrations --------------------- 

# register Publisher model
admin.site.register(Publisher)

# register Author model with AuthorAdmin options
admin.site.register(Author, AuthorAdmin)

# register Book model with BookAdmin options
admin.site.register(Book, BookAdmin)


    