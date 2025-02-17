from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from utils.models import BaseModel


class UserManager(BaseUserManager):
    """ユーザーのマネージャーモデル"""

    use_in_migrations = True

    def create_user(self, email: str, name: str, password: str, **extra_fields):
        """新しいユーザー作成し､保存する"""
        if not email:
            raise ValueError("メールアドレスが必要です｡")
        user = self.model(name, email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, name: str, password: str, **extra_fields):
        user = self.create_user(name, self.normalize_email(email), password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    """ユーザーモデル"""

    name = models.CharField(max_length=255, blank=False, verbose_name="ユーザーネーム")
    email = models.EmailField(
        max_length=255, unique=True, verbose_name="メールアドレス"
    )
    is_active = models.BooleanField(default=True, verbose_name="ユーザーの有効状態")
    is_staff = models.BooleanField(default=False, verbose_name="スタッフ権限")

    objects = UserManager()

    EMAIL_FIELD = "email"  # メールアドレスとして扱うフィールドの指定
    USERNAME_FIELD = "email"  # ユーザーを一意に識別するフィールドの指定
    REQUIRED_FIELDS = [
        "name"
    ]  # createsuperuser コマンド実行時に入力受付を行うフィールドの指定

    class Meta:
        db_table = "User"
        verbose_name = "ユーザー"

    def __srt__(self):
        return self.name
