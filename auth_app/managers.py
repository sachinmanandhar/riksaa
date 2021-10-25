from django.contrib.auth.models import AbstractUser, UserManager

class CustomUserManager(UserManager):

        def create_superuser(self, phone_number, password):
            user = self.create_user(
                username = phone_number,
                phone_number = phone_number,
                password=password
            )
            user.is_admin = True
            user.is_staff = True
            user.is_superuser = True
            user.save(using=self._db)
            return user
        
        def get_queryset(self):
            return( 
                super()
                    .get_queryset()
            )