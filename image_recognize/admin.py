from django.contrib import admin
from .models import ImageRecognition, RecognitionResult

class RecognitionResultInline(admin.TabularInline):
    model = RecognitionResult
    extra = 0

@admin.register(ImageRecognition)
class ImageRecognitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'uploaded_at', 'processed')
    list_filter = ('processed', 'uploaded_at')
    inlines = [RecognitionResultInline]

@admin.register(RecognitionResult)
class RecognitionResultAdmin(admin.ModelAdmin):
    list_display = ('image', 'label', 'confidence')
    list_filter = ('label',)