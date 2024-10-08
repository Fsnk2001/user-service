from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email=None, is_active=True, is_admin=False, password=None, **kwargs):
        if not username:
            raise ValueError('Users must have username')

        user = self.model(
            username=username,
            email=self.normalize_email(email.lower()),
            is_active=is_active,
            is_admin=is_admin,
            **kwargs
        )
        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password, email=None):
        user = self.create_user(
            username=username,
            email=email,
            is_active=True,
            is_admin=True,
            password=password,
        )

        user.is_superuser = True
        user.save(using=self._db)

        return user
