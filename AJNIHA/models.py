from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.dispatch import receiver
# Create your models here.
from django.db.models.signals import post_save
from django.contrib.auth.models import User
''''''
@receiver(post_save, sender=User)
def create_auto_sheleves(sender, instance, created, **kwargs):
    if created:
        ReaderAccount.objects.create(fName=instance.first_name, sName=instance.last_name,
                                            username=instance, email=instance.email, Gender="",
                                            country="", password=instance.password, birthday=None)
        print('user account created!')

class Book(models.Model):
    author= models.CharField(max_length=40)
    pageNo = models.IntegerField()
    bookTitle = models.CharField(max_length=40)
    isbn=models.CharField(max_length=40,default=1)
    description =models.TextField(null=True,blank=True)
    image = models.ImageField(default='/book.png',blank=True,null=True,auto_created=True,upload_to='')
    def __str__(self):
        return self.bookTitle

GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)

class ReaderAccount(models.Model):
    fName= models.CharField(max_length=40)
    sName = models.CharField(max_length=40)
    username= models.ForeignKey(User,on_delete=models.CASCADE)
    email= models.EmailField()
    Gender= models.CharField(choices=GENDER_CHOICES,null=True, max_length=10)
    country = models.CharField(max_length=40,blank=True, null=True)
    password = models.CharField(max_length=40)
    birthday = models.DateField(blank=True, null=True)
    prof_pic= models.ImageField(default='/default.png',blank=True,null=True,upload_to='')
    #Basically blank allows you to pass it a null value, but null tells the database to accept null values.
    def __str__(self):
        return str(self.username)


class Shelves(models.Model):
    shelfName = models.CharField(max_length=40)
    Reader= models.ForeignKey(ReaderAccount,on_delete=models.CASCADE)
    shelfType = models.CharField(max_length=1)
    class Meta:
        unique_together = ('shelfName', 'Reader','shelfType')
    def __str__(self):
        return str(self.shelfName) + ", " + str(self.Reader)

@receiver(post_save, sender=ReaderAccount)
def create_auto_sheleves(sender, instance, created, **kwargs):
    if created:
        Shelves.objects.create(shelfName="???????? ????????????",Reader=instance,shelfType=1)
        Shelves.objects.create(shelfName="?????? ????????????", Reader=instance, shelfType=2)
        Shelves.objects.create(shelfName="?????? ????????????", Reader=instance, shelfType=4)
        Shelves.objects.create(shelfName="??????????", Reader=instance, shelfType=5)
        print('Profile created!')




class shelves_Readers_Books(models.Model):
    reader= models.ForeignKey(ReaderAccount,unique=False, on_delete=models.CASCADE)
    book= models.ForeignKey(Book,unique=False, on_delete=models.CASCADE)
    shelf= models.ForeignKey(Shelves,unique=False, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('reader', 'book','shelf')
    def __str__(self):
        return str(self.book)+" ,"+str(self.shelf)

class ReadingRecords(models.Model):
    book_shelf_user= models.ForeignKey(shelves_Readers_Books,on_delete=models.CASCADE)
    note_title = models.CharField(max_length=40)
    date = models.DateTimeField()
    fromPage = models.IntegerField()
    toPage = models.IntegerField()
    note = models.TextField()
    private = models.BooleanField(default=False)
    bookcompleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.note_title)+ " ,"+ str(self.book_shelf_user)


class booksuggest(models.Model):
    accountUser = models.ForeignKey(ReaderAccount, on_delete=models.CASCADE)
    book_Title = models.CharField(max_length=40)
    book_description = models.TextField()
    def __str__(self):
            return str(self.accountUser)

class contacts(models.Model):
    title = models.CharField(max_length=40)
    name= models.CharField(max_length=40)
    message = models.TextField()
    def __str__(self):
        return self.name

class liked_post(models.Model):
    note_id= models.ForeignKey(ReadingRecords,on_delete=models.CASCADE)
    liked_by = models.ForeignKey(ReaderAccount,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.liked_by)


class follow (models.Model):
    follower_account= models.ForeignKey(ReaderAccount,on_delete=models.CASCADE,null=True, related_name='follower')
    followed_account = models.ForeignKey(ReaderAccount,on_delete=models.CASCADE,null=True, related_name='followed')
    class Meta:
        unique_together = ('follower_account', 'followed_account')
    def __str__(self):
        return str(self.follower_account)


