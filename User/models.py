from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone


class auth_user(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='e-mail address',
        max_length=255,
        unique=True,
        db_index=True, )
    username = models.CharField(max_length=60, unique=True)
    nombres = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=120, blank=True, null=True)
    dni = models.CharField(max_length=8, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    activation_key = models.CharField(max_length=50, blank=True, default='')
    key_expires = models.DateField(null=True, blank=True, default=timezone.now())
    date_joined = models.DateField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username',]

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.nombres

    def __str__(self):
        return str(self.email)

    class Meta:
        db_table = 'auth_user'
