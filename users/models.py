
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email,password=password,)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255,verbose_name='email_address')
    is_student = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects=CustomUserManager()


    USERNAME_FIELD='email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class CustomUserProfile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(default='', blank=True)
    preferred_name = models.CharField(max_length=100, null=True)
    avatar_url = models.CharField(max_length=255, null=True)
    discord_name = models.CharField(max_length=100, null=True)
    github_username = models.CharField(max_length=100)
    codepen_username = models.CharField(max_length=100, null=True)
    fcc_profile_url = models.CharField(max_length=255, null=True)
    customuser = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    LEVELS = (
        (1, 'Level One'),
        (2, 'Level Two'),
    )
    current_level = models.IntegerField(choices=LEVELS, default=1)

    phone = models.CharField(max_length=50, null=True)
    timezone = models.CharField(max_length=50, null=True)
    # objects=CustomUserManager()


    def __str__(self):
        return f'{self.name}'