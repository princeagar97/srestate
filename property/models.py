from django.db import models


class City(models.Model):
    #id =  models.IntegerField(primary_key=True)
    city_name = models.CharField(unique=True, max_length=128)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        managed = True
        #db_table = 'city'
    def __str__(self):
        return self.city_name



class Area(models.Model):
    #id =  models.IntegerField(primary_key=True)
    area_name = models.CharField(max_length=128)
    pincode = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        managed = True
        #db_table = 'area'
        unique_together = (('area_name', 'city'),)
    def __str__(self):
        return self.area_name + "," + self.city.city_name


class Apartment(models.Model):
    #id =  models.IntegerField(primary_key=True)
    apartment_name = models.CharField(max_length=128)
    area = models.ForeignKey(Area,on_delete=models.CASCADE,default=0)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        managed = True
        #db_table = 'area'








class Broker(models.Model):
    #id =  models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    mobile =  models.CharField(unique= True,max_length=10)
    class Meta:
        managed = True
        #db_table = 'broker'
        unique_together = (('first_name', 'mobile'),)





class Client(models.Model):
    #id =  models.IntegerField(primary_key=True)
    client_name = models.CharField(max_length=255)
    client_address = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    mobile = models.CharField(max_length=64, blank=True, null=True)
    mail = models.CharField(max_length=64, blank=True, null=True)
    client_details = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        #db_table = 'client'


class Contact(models.Model):
    #id =  models.IntegerField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Broker, on_delete=models.CASCADE, blank=True, null=True)
    estate = models.ForeignKey('Estate', on_delete=models.CASCADE, blank=True, null=True)
    contact_time = models.TextField()  # This field type is a guess.
    contact_details = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        #db_table = 'contact'


class Estate(models.Model):
    #id =  models.AutoField(primary_key = True)
    estate_name = models.CharField(max_length=255)
    city = models.ForeignKey(Area, on_delete=models.CASCADE)
    estate_type = models.ForeignKey('EstateType', on_delete=models.CASCADE)
    floor_space = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    number_of_balconies = models.IntegerField(blank=True, null=True)
    balconies_space = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    number_of_bedrooms = models.IntegerField(blank=True, null=True)
    number_of_bathrooms = models.IntegerField(blank=True, null=True)
    number_of_garages = models.IntegerField(blank=True, null=True)
    number_of_parking_spaces = models.IntegerField(blank=True, null=True)
    pets_allowed = models.IntegerField(blank=True, null=True)
    estate_description = models.TextField()  # This field type is a guess.
    estate_status = models.ForeignKey('EstateStatus', on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    society = models.ForeignKey(Apartment,on_delete=models.CASCADE,default=0)
    class Meta:
        managed = True



class EstateStatus(models.Model):
    #id =  models.AutoField(primary_key = True)
    estate_status_name = models.CharField(unique=True, max_length=64)
    is_deleted  = models.BooleanField(default=0)
    class Meta:
        managed = True
    def __str__(self):
        return  self.estate_status_name
        #db_table = 'estate_status'


class EstateType(models.Model):
    #id =  models.IntegerField(primary_key=True)
    type_name = models.CharField(max_length=128)
    is_deleted = models.BooleanField(default=0)

    class Meta:
        managed = True
    def __str__(self):
        return  self.type_name

class InCharge(models.Model):
    #id =  models.IntegerField(primary_key=True)
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = True


class SubestateType(models.Model):
    #id =  models.IntegerField(primary_key=True)
    subtype_name = models.CharField(max_length=128)
    estate_type = models.ForeignKey(EstateType, on_delete=models.CASCADE)

    class Meta:
        managed = True
