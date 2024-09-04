from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save


 
JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

COUNTRIES = (
    ('US', 'United States'),
    ('GB', 'United Kingdom'),
    ('FR', 'France'),
    ('EG', 'Egypt'),
    ('DE', 'Germany'),
    ('IT', 'Italy'),
    ('ES', 'Spain'),
    ('CN', 'China'),
    ('JP', 'Japan'),
)

def image_upload(object, filename) :
    
    imagename, ext = filename.split(".")
    return "jobs/%s/%s.%s"%(object.id,object.id, ext)
   

class Job(models.Model): 
    owner = models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)  # column
    job_type = models.CharField(max_length=15 , choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    country = models.CharField(
        max_length=20,  
        choices=COUNTRIES,
        verbose_name="Select Country Job"
    )
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1) 
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField( upload_to=image_upload,blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    num_applyed = models.IntegerField(default=0)


    def save(self, *args, **kwargs):
       self.slug = slugify(self.title)
       super(Job, self).save(*args, **kwargs) # Call the real save() method

    
    def __str__(self):
      return self.title
    
   
       
    

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
      return self.name


class Apply(models.Model):
    # owner = models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE) # type: ignore
    job = models.ForeignKey(Job, related_name= 'apply_job', on_delete=models.CASCADE)
    name  = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    website = models.URLField()
    cv = models.FileField( upload_to='apply/', max_length=100)
    cover_letter = models.TextField(max_length=500)
    # apply_at = models.DateTimeField()
    def __str__(self):
       return  self.name


@receiver(post_save, sender=Apply)
def count_applayes(sender, instance,  **kwargs):
    job = instance.job 
    job.num_applyed +=1 
    job.save()

        
    
    
    
    
        

  

    
   
    












