from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class My_profile_nav(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    short_intro = models.CharField(max_length=200,blank=True, null=True)
    side_profile_pic = models.ImageField(blank=True, null=True) 
     
    facebook_link = models.URLField(("facebook_link"), 
        max_length=128, 
        db_index=True, 
        unique=True, 
        blank=True
    )
    linkedin_link = models.URLField(("linkedin_link"), 
        max_length=128, 
        db_index=True, 
        unique=True, 
        blank=True
    )
    github_link = models.URLField(("github_link"), 
        max_length=128, 
        db_index=True, 
        unique=True, 
        blank=True
    )
    
    researchgate_link = models.URLField(("researchgate_link"), 
        max_length=128, 
        db_index=True, 
        unique=True, 
        blank=True
    )

    google_sch_link= models.URLField(("google_sch_link"), 
        max_length=128, 
        db_index=True, 
        unique=True, 
        blank=True
    )

    my_website_link = models.URLField(("my_website_link"), max_length=128, 
        db_index=True, 
        unique=True, 
        blank=True
    )

    
    

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    
   
    def __str__(self):
        return self.name