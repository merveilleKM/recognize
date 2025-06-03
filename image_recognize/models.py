from django.db import models
import os

class ImageRecognition(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Image {self.id} - {self.uploaded_at}"
    
    def delete(self, *args, **kwargs):
        # Supprimer l'image du système de fichiers lors de la suppression de l'entrée
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

class RecognitionResult(models.Model):
    image = models.ForeignKey(ImageRecognition, on_delete=models.CASCADE, related_name='results')
    label = models.CharField(max_length=100)
    confidence = models.FloatField()
    category = models.CharField(
        max_length=20,
        choices=[
            ('object', 'Objet'),
            ('scene',  'Scène'),
            ('color',  'Couleur'),
            ('concept','Concept'),
            ('general','Général'),
        ],
        default='general',
    )
    
    def __str__(self):
        return f"{self.label} ({self.confidence:.2f})"