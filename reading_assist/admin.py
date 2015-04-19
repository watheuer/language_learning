from django.contrib import admin
from reading_assist.models import Document, VocabList, Word

# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Document, DocumentAdmin)
admin.site.register(VocabList)
admin.site.register(Word)