from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from .utils import sendTransaction
import hashlib


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    hash = models.CharField(max_length=32, blank=True, editable=False)
    txId = models.CharField(max_length=66, blank=True, editable=False, unique=True)

    def writeOnChain(self):
        self.hash = hashlib.sha256(self.content.encode('utf-8')).hexdigest()
        self.txId = sendTransaction(self.hash)
        self.save()

