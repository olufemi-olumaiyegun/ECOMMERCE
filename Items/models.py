from django.db import models
import os
import random





#tackling the path name for the image and how it will appear to the user as a URL
#this will make sure that we useful URLS instead of the default django object id URL
#Also useful in parsing and manipulating image names with spaces in them that would normally cause an error when browsing



def get_filename_path(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    print(instance.title)
    print(filename)
    randomintStr = str(random.randint(1,999999999999)) #could be a smaller range.
    new_filename =  instance.title + randomintStr  #item title + random numbers to serve as url component for image
    ext = get_filename_path(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    #return "products/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename=final_filename)
    return "products/{final_filename}".format(final_filename=final_filename)


####We gonna have to relate this object tyoe to the User->Seller class somehow so this will be edited later on
#probs a one to many or foreign key action. up to you buddy
class Item(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2,default=5000.50)
    delivery_time = models.IntegerField(default=14) #maximum time it will take to deliver item

    #whether they have paid to have their products featured on the front page or not.
    # We change it ourselves in admin whenever we need to or we create an app to do it automatically.
    featured = models.BooleanField(default=False)

    # we will have to mess around with this so that when there is a purchase of an item, the quantity reduces.
    # #This will probably be done in a different app called "billing??idk"
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title


##create separate image class to enable users upload multiple images for a product
class Images(models.Model):
    item = models.ForeignKey(Item,default=None,on_delete=models.CASCADE)
    pictures = models.ImageField(upload_to=upload_image_path,null=True,blank=True) #should not be null in deployment but i am to lazy to bother with a default valur
