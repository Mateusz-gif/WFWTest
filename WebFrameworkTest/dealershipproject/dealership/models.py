from django.db import models


class Salesperson(models.Model):
    salesperson_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Mechanic(models.Model):
    mechanic_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    serial_number = models.CharField(max_length=100, unique=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    colour = models.CharField(max_length=50)
    year = models.IntegerField()
    car_for_sale = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"


class SalesInvoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    invoice_number = models.CharField(max_length=100, unique=True)
    date = models.DateField()
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)

    def __str__(self):
        return self.invoice_number


class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.service_name


class ServiceTicket(models.Model):
    service_ticket_id = models.AutoField(primary_key=True)
    service_ticket_number = models.CharField(max_length=100, unique=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_received = models.DateField()
    comments = models.TextField(blank=True, null=True)
    date_returned_to_customer = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.service_ticket_number


class ServiceMechanic(models.Model):
    servicemechanic_id = models.AutoField(primary_key=True)
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    hours = models.DecimalField(max_digits=6, decimal_places=2)
    comment = models.TextField(blank=True, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"ServiceMechanic #{self.servicemechanic_id}"


class Parts(models.Model):
    parts_id = models.AutoField(primary_key=True)
    part_number = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.part_number


class PartsUsed(models.Model):
    parts_used_id = models.AutoField(primary_key=True)
    part = models.ForeignKey(Parts, on_delete=models.CASCADE)
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    number_used = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"PartsUsed #{self.parts_used_id}"