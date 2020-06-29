from .models import Images,Item
from django import forms
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

class RegisterProduct(forms.ModelForm):
    title = forms.CharField()
    description = forms.Textarea()
    price = forms.DecimalField()
    delivery_time = forms.IntegerField()  # maximum time it will take to deliver item

    # whether they have paid to have their products featured on the front page or not.
    # We change it ourselves in admin whenever we need to or we create an app to do it automatically.
    featured = forms.BooleanField()

    # we will have to mess around with this so that when there is a purchase of an item, the quantity reduces.
    # #This will probably be done in a different app called "billing??idk"
    quantity = forms.IntegerField()
    class Meta:
        model = Item
        fields = ['title', 'description', 'price', 'delivery_time', 'featured', 'quantity']


class ImageForm(forms.ModelForm):
    pictures = forms.ImageField()
    class Meta:
        model = Images
        fields = ['pictures']
