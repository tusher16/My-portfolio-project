from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
    (0,"not_featured"),
    (1,"Featured")
)

class My_profile_nav(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    short_intro = models.CharField(max_length=200,blank=True, null=True)
    side_profile_pic = models.ImageField(blank=True, null=True) 
     
    facebook_link = models.URLField(("facebook_link"), 
        max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    linkedin_link = models.URLField(("linkedin_link"), 
        max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    github_link = models.URLField(("github_link"), 
        max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    
    researchgate_link = models.URLField(("researchgate_link"), 
        max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )

    google_sch_link= models.URLField(("google_sch_link"), 
        max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )

    my_website_link = models.URLField(("my_website_link"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    my_kaggle_link = models.URLField(("my_kaggle_link"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    my_email = models.EmailField(("my_email"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    my_twitter = models.URLField(("my_twitter_link"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    my_ig = models.URLField(("my_ig_link"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    my_stack_overflow = models.URLField(("my_stack_overflow"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    my_medium_link = models.URLField(("my_medium_link"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    my_facebook = models.URLField(("my_facebook"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    

    date_created = models.DateTimeField(auto_now_add=True, null=True)

   
    def __str__(self):
        return self.name


class My_profile_home(models.Model):
    full_name = models.CharField(max_length=100,blank=True, null=True)
    my_job_status = models.CharField(max_length=100,blank=True, null=True)
    mid_intro = models.TextField(max_length=600,blank=True, null=True)
    side_profile_pic = models.ImageField(blank=True, null=True) 
    what_i_do = models.TextField(max_length=600,blank=True, null=True)

    def __str__(self):
        return self.full_name


class testiomonial(models.Model):
    
    test_details = models.TextField(max_length=800,blank=True, null=True)
    test_name = models.CharField(max_length=100,blank=True, null=True)
    test_job_status = models.CharField(max_length=200,blank=True, null=True)
    test_profile_pic = models.ImageField(blank=True, null=True)   

    def __str__(self):
        return self.test_name


class My_researche(models.Model):

    research_title = models.CharField(max_length=300,blank=True, null=True)
    research_short_dis = models.TextField(max_length=600,blank=True, null=True)
    research_image = models.ImageField(blank=True, null=True)
    research_published_by = models.CharField(max_length=300,blank=True, null=True)
    research_publish_time = models.CharField(max_length=100,blank=True, null=True)
    research_readmore_link = models.URLField(("research_readmore_link"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    research_publication_link = models.URLField(("research_publication_link"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )

    Featured = models.IntegerField(choices=STATUS, default=0)
    
    def __str__(self):
        return self.research_title


class My_portfolio(models.Model):

    portfolio_title = models.CharField(max_length=300,blank=True, null=True)
    portfolio_short_dis = models.TextField(max_length=600,blank=True, null=True)
    portfolio_image = models.ImageField(blank=True, null=True)
    portfolio_readtime = models.CharField(max_length=100,blank=True, null=True)
    portfolio_publish_time = models.CharField(max_length=100,blank=True, null=True)
    portfolio_medium_link = models.URLField(("portfolio_medium_link"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    portfolio_git_link = models.URLField(("portfolio_git_link"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )

    portfolio_live_link = models.URLField(("portfolio_live_link"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )

    Featured = models.IntegerField(choices=STATUS, default=0)
    

    def __str__(self):
        return self.portfolio_title

class My_blog(models.Model):

    blog_title = models.CharField(max_length=300,blank=True, null=True)
    blog_short_dis = models.TextField(max_length=600,blank=True, null=True)
    blog_image = models.ImageField(blank=True, null=True)
    blog_readtime = models.CharField(max_length=100,blank=True, null=True)
    blog_publish_time = models.CharField(max_length=100,blank=True, null=True)
    blog_medium_link = models.URLField(("blog_medium_link"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )

    Featured = models.IntegerField(choices=STATUS, default=0)
    

    def __str__(self):
        return self.blog_title

class Contact(models.Model):
    con_name = models.CharField(max_length=100,blank=True, null=True)
    con_email = models.EmailField(("my_email"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    con_message = models.TextField(max_length=600,blank=True, null=True)

    def __str__(self):
        return self.con_name
