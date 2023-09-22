from django.db import models

# Create your models here.

# class Role(models.Model):
#     name = models.CharField(max_length = 200)

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         db_table = 'role'



class Employee(models.Model):
    name = models.CharField(max_length = 255)
    place = models.CharField(max_length = 255)        
    user_id = models.CharField(max_length = 255, unique = True)
    password = models.CharField(max_length = 255)
    # role = models.ForeignKey(Role, on_delete=models.CASCADE)
    role = models.CharField(max_length = 255)

    class Meta:
        db_table = 'employee'

class Leave(models.Model):
    name = models.CharField(max_length = 200)
    reason = models.CharField(max_length = 500)
    from_date = models.DateField()
    to_date = models.DateField()
    status = models.CharField(max_length = 200, default = "Pending")
    e_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'leave'

