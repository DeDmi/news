from django.contrib import admin
from .models import Article, Comment
# Register your models here.



#1 вид отображенияполей для комментов
#class CommentInline(admin.StackedInline):
    #model = Comment
    #extra = 0


# 2 вид отображенияполей для комментов
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)

