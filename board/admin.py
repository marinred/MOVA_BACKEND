from django.contrib import admin
from .models import Board
from .models import BoardComment
from .models import BoardCategory
from .models import User

class CommentInline(admin.TabularInline):
    model = BoardComment
    
class BoardAdmin(admin.ModelAdmin):
    inlines = (
        CommentInline,
    )
    

# Register your models here.
admin.site.register(Board, BoardAdmin)
admin.site.register(BoardComment)
admin.site.register(BoardCategory)
