from django.db import models 
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin,PermissionManager
import uuid
# Create your models here. 

class CustomUserManager(BaseUserManager): 
    def _create_user(self,email,username,password,**extra_fields): 
        if not email: 
            raise ValueError("User must have email") 
        if not username: 
            raise ValueError("User must have user name ") 
        email = self.normalize_email(email)  
        user = self.model(email=email,username=username,**extra_fields)
        user.set_password(password) 
        user.save(using=self._db) 
        return user 
    
    def create_user(self,email=None,username=None,password=None,**extra_fields): 
        extra_fields.setdefault('is_staff',False) 
        extra_fields.setdefault('is_superuser',False) 
        
        return self._create_user(email=email,password=password,**extra_fields) 
    
    def create_superuser(self,email=None,username=None,password=None,**extra_fields): 
        extra_fields.setdefault('is_staff',True) 
        extra_fields.setdefault('is_superuser',True) 
        return self._create_user(email=email,username=username,password=password,**extra_fields) 
    
    
#create User model 
class User(AbstractBaseUser,PermissionsMixin): 
    id              = models.UUIDField(primary_key=True,editable=False,unique=True,default=uuid.uuid4) 
    email           = models.EmailField(max_length=255,unique=True) 
    username        = models.CharField(max_length=255) 
    
    is_active       = models.BooleanField(default=True) 
    is_superuser    = models.BooleanField(default=False)  
    is_staff        = models.BooleanField(default=False) 
    
    objects         = CustomUserManager() 
    
    USERNAME_FIELD  = 'email'  
    EMAIL_FIELD     = 'email'
    REQUIRED_FIELDS = ['username',] 
    
    date_joined     = models.DateTimeField(auto_now_add=True) 
    last_login      = models.DateTimeField(auto_now=True) 
    
    def __str__(self) -> str:
        return self.email 
    
    
               
