from django.contrib import admin
from blogs import models

@admin.register(models.BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_author_first_name', 'created_at']
    search_fields = ['title', 'short_description', 'long_description']
    list_filter = ['created_at', 'updated_at']
    ordering = ['-created_at']

    @admin.display(description='Muallif ismi')
    def get_author_first_name(self, obj):
        return obj.author.first_name if obj.author else None


@admin.register(models.BlogHashgtagModel)
class BlogHashtagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at', 'updated_at']
    ordering = ['-created_at']


@admin.register(models.BlogCategoryModel)
class BlogCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at', 'updated_at']  
    ordering = ['-created_at']


@admin.register(models.BlogCommentModel)
class BlogCommentModelAdmin(admin.ModelAdmin):
    list_display = ['get_blog_title', 'get_user_username', 'created_at']
    search_fields = ['blog__title']
    list_filter = ['created_at', 'updated_at']
    ordering = ['-created_at']

    @admin.display(description='Blog sarlavhasi')
    def get_blog_title(self, obj):
        return obj.blog.title if obj.blog else None

    @admin.display(description='Foydalanuvchi ismi')
    def get_user_username(self, obj):
        return obj.user.username if obj.user else None


@admin.register(models.BlogLikesModel)
class BlogLikeModelAdmin(admin.ModelAdmin):
    list_display = ['get_blog_title', 'get_user_username', 'created_at']
    search_fields = ['blog__title']
    list_filter = ['created_at', 'updated_at']
    ordering = ['-created_at']

    @admin.display(description='Blog sarlavhasi')
    def get_blog_title(self, obj):
        return obj.blog.title if obj.blog else None

    @admin.display(description='Foydalanuvchi ismi')
    def get_user_username(self, obj):
        return obj.user.username if obj.user else None
