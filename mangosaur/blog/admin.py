from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django_summernote.admin import SummernoteModelAdmin
from .models import Tag, Category, Post, Comment, User

class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = ('body',)

    fieldsets = [
        (None, {'fields': ['author', 'title', 'thumbnail', 'body']}),
        ('Details', {'fields': ['category', 'tags', 'date_created', 'date_edited']}),
        ('Votes', {'fields': ['vote_score', 'num_vote_up', 'num_vote_down']})
    ]

    list_display=('title', 'date_created', 'recent')
    list_filter = ['date_created']
    search_fields = ['title']

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']

class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']

class CommentAdmin(admin.ModelAdmin):
    list_filter = ['date_created']
    search_fields = ['author']
    
admin.site.register(User, UserAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)