from django.db import models 
import uuid  
from account.models import User

# Create your models here.   

class Tasks(models.Model): 
    id     = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4) 
    
    pass 

class TasksList(models.Model): 
    id              = models.UUIDField(primary_key=True,editable=True,default=uuid.uuid4)  
    tasks           = models.ManyToManyField(Tasks,null=True,blank=True) 
    taskslist_title = models.CharField(max_length=255,null=True,blank=True) 
    
     
     
    

class Project(models.Model): 
    id          = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4) 
    title       = models.CharField(max_length=255)  
    description = models.TextField(null=True,blank=True) 
    taskslist   = models.ManyToManyField(TasksList,null=True,blank=True) 
    assign_to   = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    created_at  = models.DateTimeField(auto_now_add=True) 
    updated_at  = models.DateTimeField(auto_now=True) 
  
    
    def __str__(self) -> str:
        return self.title 
    

    
     
