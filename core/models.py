from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        if not phone:
            raise ValueError('User must have Phone')
               
        user = self.model(
            phone = phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, phone, password=None):
        """
        Creates and saves a superuser with the given phone, and password.
        """
        user = self.create_user(
            phone = phone,
            password = password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.profile_type = 'Admin'
        user.save(using = self._db)
        return user    


class User(AbstractBaseUser, PermissionsMixin):
    CHOICES = [
        ("Customer", 'Customer'),
        ("ServiceProvider", 'ServiceProvider'),
        ("Delivery Boy", 'Delivery Boy'),
        ("Admin", 'Admin'),
    ]
    DAYS=[
        ("Monday","Monday"),
        ("Tuesday","Tuesday"),
        ("Wednessday","Wednessday"),
        ("Thursday","Thursday"),
        ("Friday","Friday"),
        ("Saturday","Saturday"),
        ("Sunday","Sunday"),
    ]
    phone = models.CharField(max_length=15, unique=True, help_text="Phone Number With Country Code e.g. (+1123763989)")
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    profile_type = models.CharField(max_length=100, choices=CHOICES, default='Customer')
    location = models.CharField(max_length=100, null=True, blank=True)
    distance=models.FloatField(default=5,null=True)
    device_token = models.CharField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default=False)
    opening_timing=models.CharField(max_length=15,null=True,blank=True)
    closing_timing=models.CharField(max_length=15,null=True,blank=True)
    close_day=models.CharField(max_length=15,choices=DAYS,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ###### Measurement #####

    sleeve = models.FloatField(validators=[MinValueValidator(0)], default=0)
    waist = models.FloatField(validators=[MinValueValidator(0)], default=0)
    neck = models.FloatField(validators=[MinValueValidator(0)], default=0)
    shoulder = models.FloatField(validators=[MinValueValidator(0)], default=0)
    hip = models.FloatField(validators=[MinValueValidator(0)], default=0)
    waist_to_heap = models.FloatField(validators=[MinValueValidator(0)], default=0)
    waist_to_ankle = models.FloatField(validators=[MinValueValidator(0)], default=0)
    length_of_arm = models.FloatField(validators=[MinValueValidator(0)], default=0)
    round_arm = models.FloatField(validators=[MinValueValidator(0)], default=0)
    shoulder_to_waist = models.FloatField(validators=[MinValueValidator(0)], default=0)
    knee = models.FloatField(validators=[MinValueValidator(0)], default=0)
    back_width = models.FloatField(validators=[MinValueValidator(0)], default=0)
    thigh = models.FloatField(validators=[MinValueValidator(0)], default=0)
    calf = models.FloatField(validators=[MinValueValidator(0)], default=0)
    leg_length = models.FloatField(validators=[MinValueValidator(0)], default=0)
    ankle = models.FloatField(validators=[MinValueValidator(0)], null=True, default=0)
    waist_to_floor = models.FloatField(validators=[MinValueValidator(0)], default=0)
    crotch_depth = models.FloatField(validators=[MinValueValidator(0)], default=0)
    elbow_width = models.FloatField(validators=[MinValueValidator(0)], default=0)
    additional_information = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'







class BaseModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  class Meta:
    abstract = True

class Category(BaseModel):
    image=models.ImageField(upload_to='category_image',null=True,blank=True)
    name = models.CharField('Category Name', max_length=150,null=True,blank=True)


    
class Service(BaseModel):
    CHOICES = [
        ("Female", 'Female'),
        ("Male", 'Male'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100,null=True,blank=True)
    price = models.FloatField(validators=[MinValueValidator(0)])
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    gender = models.CharField(max_length=100, choices=CHOICES, default='Female')

    def __str__(self):
        return self.name
    
class UserCategory(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserServices(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    user_cat_id=models.ForeignKey(UserCategory,on_delete=models.CASCADE,null=True)
    service_id=models.ForeignKey(Service,on_delete=models.CASCADE,null=True)


class SelectedService(BaseModel):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='selected_service')
    quantity = models.PositiveIntegerField(null=True, blank=True)
    price = models.FloatField(validators=[MinValueValidator(0)], null=True, blank=True)

    ###### Measurement #####

    sleeve = models.FloatField(validators=[MinValueValidator(0)], default=0)
    waist = models.FloatField(validators=[MinValueValidator(0)], default=0)
    neck = models.FloatField(validators=[MinValueValidator(0)], default=0)
    shoulder = models.FloatField(validators=[MinValueValidator(0)], default=0)
    hip = models.FloatField(validators=[MinValueValidator(0)], default=0)
    waist_to_heap = models.FloatField(validators=[MinValueValidator(0)], default=0)
    waist_to_ankle = models.FloatField(validators=[MinValueValidator(0)], default=0)
    length_of_arm = models.FloatField(validators=[MinValueValidator(0)], default=0)
    round_arm = models.FloatField(validators=[MinValueValidator(0)], default=0)
    shoulder_to_waist = models.FloatField(validators=[MinValueValidator(0)], default=0)
    knee = models.FloatField(validators=[MinValueValidator(0)], default=0)
    back_width = models.FloatField(validators=[MinValueValidator(0)], default=0)
    thigh = models.FloatField(validators=[MinValueValidator(0)], default=0)
    calf = models.FloatField(validators=[MinValueValidator(0)], default=0)
    leg_length = models.FloatField(validators=[MinValueValidator(0)], default=0)
    ankle = models.FloatField(validators=[MinValueValidator(0)], null=True, default=0)
    waist_to_floor = models.FloatField(validators=[MinValueValidator(0)], default=0)
    crotch_depth = models.FloatField(validators=[MinValueValidator(0)], default=0)
    elbow_width = models.FloatField(validators=[MinValueValidator(0)], default=0)
    additional_information = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.service.name
    
    class Meta:
        verbose_name = 'Selected Service'
        verbose_name_plural = 'Selected Services'

    
class Order(BaseModel):
    CHOICES = [
        ("Pending", 'Pending'),
        ("Preparing To Pickup For Service", 'Preparing To Pickup For Service'),
        ("Picked For Service", 'Picked For Service'),
        ("Preparing To Pickup For Delivery", 'Preparing To Pickup For Delivery'),
        ("Picked For Delivery", 'Picked For Delivery'),
        ("Rejected By Delivery_Boy",'Rejected By Delivery_Boy'),
        ("Order In Progress",'Order In Progress'),
        ("Completed", 'Completed'),
        ("Delivered", 'Delivered'),
        ("Canceled", 'Canceled'),
        ("Accepted By Tailor", 'Accepted By Tailor'),
        ("Rejected By Tailor", 'Rejected By Tailor'),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_customer')
    tailor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_tailor')
    delivery_boy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='order_delivery_boy')
    service = models.ManyToManyField(SelectedService, related_name='order_selected_service')
    status = models.CharField(max_length=100, choices=CHOICES, default='Pending')
    customer_delivery_address = models.TextField(max_length=200)
    order_date = models.DateField(default=timezone.now)
    pickup_date = models.DateField(null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)
    completed_date = models.DateField(null=True, blank=True)
    canceled_date = models.DateField(null=True, blank=True)
    cancel_reason = models.TextField(max_length=200, null=True, blank=True)
    tailor_price=models.FloatField(null=True,blank=True)

    
class Alldeliveryboyadddata(models.Model):
    order_id=models.ForeignKey(Order,on_delete=models.CASCADE,null=True, blank=True)
    delivery_boy_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    price=models.CharField(max_length=100,null=True,blank=True)
    status=models.CharField(max_length=100,null=True,blank=True,default="Incomplete")

class Enquiry(BaseModel):
    phone = models.CharField(max_length=15, help_text="Phone Number With Country Code e.g. (+1123763989)")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=400)

    def __str__(self):
        return self.subject
    
    class Meta:
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'


class Earning(BaseModel):
    CHOICES = [
        ("Pending", 'Pending'),
        ("Paid", 'Paid'),
    ]
    order = models.ForeignKey(User, on_delete=models.CASCADE, related_name='earning_order')
    image = models.ImageField(upload_to='earning', null=True, blank=True)
    status = models.CharField(max_length=100, choices=CHOICES, default='Pending')
    request_date = models.DateTimeField(null=True, blank=True)
    paid_date = models.DateTimeField(auto_now=True,null=True)
    requested_amount=models.CharField(max_length=1000,default=0)
    profile_type = models.CharField(max_length=100,null=True, blank=True)



class Delivery_Boy_Earning(BaseModel):
    prize=models.CharField(max_length=100,null=True,blank=True)

    

class Notification(BaseModel):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='sender_notification')
    recipient = models.ForeignKey(User,on_delete=models.CASCADE, related_name='recipient_notification',null=True)
    title = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    is_seen = models.BooleanField(default=False)
    recieved_date = models.DateTimeField(auto_now_add=True)
    order_id=models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)

class TermsAndConditions(models.Model):
    img=models.ImageField(null=True,blank=True,upload_to='condition')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True,blank=True)



class PrivacyPolicy(models.Model):
    img=models.ImageField(null=True,blank=True,upload_to='condition')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True,blank=True)