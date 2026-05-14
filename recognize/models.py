from django.db import models


class RecognitionHistory(models.Model):
    user_id = models.BigIntegerField()
    mineral_name = models.CharField(max_length=255)
    confidence = models.FloatField()
    image = models.ImageField(upload_to="recognitions/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mineral_name} ({self.confidence}%)"


class FavoriteMineral(models.Model):
    user_id = models.BigIntegerField()
    mineral_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user_id", "mineral_name")
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.user_id} — {self.mineral_name}"