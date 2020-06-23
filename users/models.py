from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

userchoices = (("Buyer","Buyer"), ("Seller","Seller"), ("Both","Both")) #choices of type of user

class UserManager(BaseUserManager):
    def create_user(self,email,first_name,last_name, is_active=True, is_staff=False, is_admin=False,password=None):
        if not email:
            raise ValueError("You need to have an email address")
        if not password:
            raise ValueError("Password required")
        userobj = self.model(
            email = self.normalize_email(email)  #makes email reusable
        )

        userobj.set_password(password) #change/add user password
        userobj.admin = is_admin
        userobj.active = is_active
        userobj.staff = is_staff
        userobj.save(using=self.db)
        return userobj
    def create_staff(self,email, password=None,is_seller=False):
        user= self.create_user(email,password=password,is_staff=True)
        return user
    def create_superuser(self,email,password=None): #name is important for this to create a superuse to acess django backend
        if not email:
            raise ValueError("You need to have an email address")
        if not password:
            raise ValueError("Password required")
        userobj = self.model(
            email=self.normalize_email(email)  # makes email reusable
        )

        userobj.set_password(password)  # change/add user password
        userobj.admin = True
        userobj.active = True
        userobj.staff = True
        userobj.save(using=self.db)
        return userobj

#create parent user class
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True)  #whether user can start to do stuff on website
    staff = models.BooleanField(default=False) #will user be able to manage some portions of the side?
    admin = models.BooleanField(default=False)
    seller = models.BooleanField(default=False)  #whether user will be making sales on the site
    first_name = models.CharField(max_length=70,blank=True)
    last_name = models.CharField(max_length=70,blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = UserManager()  #this makes it usable in the BaseUserManager based class
    def __str__(self):
        return self.email
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    #next two functions are critical to logging in the admin/superuser
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.admin
    @property
    def is_active(self):
        return self.active
    @property
    def is_seller(self):
        return self.seller
class GuestEmail(models.Model):
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email