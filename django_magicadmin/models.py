import uuid

from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model

User = get_user_model()

class MagicLinkError(Exception):
    pass

class MagicLink(models.Model):
    secret_identifier = models.CharField(max_length=512, default=uuid.uuid4())
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True)
    used_at = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    already_used = models.BooleanField(default=False)

    def get_login_url(self, request=None, complete = True):
        if not all((self.pk, self.created_at)):
            raise ("Unsaved Job models have no close URL")

        kwargs = {"magiclink": self.secret_identifier}

        if not complete or not request:
            return reverse("magic_login_validate", kwargs=kwargs)
        
        return request.build_absolute_uri(reverse("magic_login_validate", kwargs=kwargs))

    class Meta:
        get_latest_by = ['-created_at']
        indexes = [
            models.Index(fields=['secret_identifier'], name='magic_link_idx'),
        ]
        verbose_name = 'Magic Link'
        verbose_name_plural = 'Magic Links'
    
    def __repr__(self) -> str:
        return f"<MagicLink(user={self.user.username}, already_used={self.already_used})>"
    
    def __str__(self) -> str:
        return f"MagicLink: {self.user.username} - Already Used? {self.already_used}"