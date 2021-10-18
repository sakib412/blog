from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField


def author_avatar_path(instance, filename):
    # https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.FileField.upload_to
    # file will be uploaded to MEDIA_ROOT/avatar/author_<id>-<filename>
    return 'avatar/author_{0}-{1}'.format(instance.user.id, filename)


GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')
)

ROLE = (
    ("member", "Member"),
    ("author", "Author"),
    ("editor","Editor"),
    ("admin", "Administrator")
)

STATUS = ((0, "Inactive"), (1, "Active"))


class Author(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=512, blank=True)
    avatar = models.ImageField(blank=True, upload_to=author_avatar_path)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=True)
    gender = models.CharField(choices=GENDER, default='other', max_length=255)
    interested_in = models.JSONField(default=list, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    role = MultiSelectField(choices=ROLE, default="member")
    social_link = models.JSONField(default=dict,blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self) -> str:
        return f"{self.user}"
    
