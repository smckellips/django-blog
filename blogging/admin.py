from django.contrib import admin

# Register your models here.
from blogging.models import Post, Category

# admin.site.register(Post)
# admin.site.register(Category)

class CategoryInline(admin.StackedInline):
    model = Category.posts.through

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline,]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ['posts',]
