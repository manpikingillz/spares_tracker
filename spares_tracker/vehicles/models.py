from django.db import models
from spares_tracker.common.models import BaseModel
from datetime import date
from django.db.models import Q
from spares_tracker.setup.models import Country
from spares_tracker.files.models import File

class VehicleMake(models.Model):
    vehicle_make_name = models.CharField(max_length=255)

    def __str__(self):
        return self.vehicle_make_name

class VehicleModel(models.Model):
    vehicle_model_name = models.CharField(max_length=255)
    vehicle_make = models.ForeignKey(VehicleMake, related_name='vehicle_models', on_delete=models.CASCADE)

    def __str__(self):
        return self.vehicle_model_name


class Vehicle(BaseModel):
    class BodyType(models.TextChoices):
        SEDAN = 'SEDAN', 'Sedan'
        HATCHBACK = 'HATCHBACK', 'Hatchback'
        SUV = 'SUV', 'SUV'
        MINI_VAN = 'MINI_VAN', 'Mini Van'
        VAN = 'VAN', 'Van'
        TRUCK = 'TRUCK', 'Truck'
        WAGON = 'WAGON', 'Wagon'
        COUPE = 'COUPE', 'Coupe'
        MINI_VEHICLE = 'MINI_VEHICLE', 'Mini Vehicle'
        BUS = 'BUS', 'Bus'
        MINI_BUS = 'MINI_BUS', 'Mini Bus'
        PICKUP = 'PICKUP', 'Pick up'
        CONVERTIBLE = 'CONVERTIBLE', 'Convertible'
        MOTORCYCLE = 'MOTORCYCLE', 'Motorcycle'
        TRACTOR = 'TRACTOR', 'Tractor'
        MACHINERY = 'MACHINERY', 'Machinery'
        UNSPECIFIED = 'UNSPECIFIED', 'Unspecified'

    class Transmission(models.TextChoices):
        AUTOMATIC = 'AUTOMATIC', 'Automatic'
        CVT = 'CVT', 'CVT'
        DCT = 'DCT', 'DCT'
        MANUAL = 'MANUAL', 'Manual'
        SEMI_AUTOMATIC = 'SEMI_AUTOMATIC', 'Semi Automatic'
        SPORT_AT = 'SPORT_AT', 'Sport AT'
        UNSPECIFIED = 'UNSPECIFIED', 'Unspecified'

    class Fuel(models.TextChoices):
        PETROL='PETROL', 'Petrol'
        DIESEL = 'DIESEL', 'Diesel'
        ELECTRIC = 'ELECTRIC', 'Electric'
        HYBRID_DIESEL = 'HYBRID_DIESEL', 'Hybrid (Diesel)'
        HYBRID_PETROL = 'HYBRID_PETROL', 'Hybrid (Petrol)'
        CNG = 'CNG', 'CNG'
        PLG = 'PLG', 'PLG'
        UNSPECIFIED = 'UNSPECIFIED', 'Unspecified'

    class Color(models.TextChoices):
        BEIGE = 'BEIGE', 'Beige'
        BLACK = 'BLACK', 'Black'
        BLUE = 'BLUE', 'Blue'
        BRONZE = 'BRONZE', 'Bronze'
        BROWN = 'BROWN', 'Brown'
        GOLD = 'GOLD', 'Gold'
        GRAY = 'GRAY', 'Gray'
        GREEN = 'GREEN', 'Green'
        MAROON = 'MAROON', 'Maroon'
        ORANGE = 'ORANGE', 'Orange'
        PEARL = 'PEARL', 'Pearl'
        PINK = 'PINK', 'Pink'
        PURPLE = 'PURPLE', 'Purple'
        RED = 'RED', 'Red'
        SILVER = 'SILVER', 'Silver'
        WHITE = 'WHITE', 'White'
        YELLOW = 'YELLOW', 'Yellow'
        UNSPECIFIED = 'UNSPECIFIED', 'Unspecified'

    class DriveTrain(models.TextChoices):
        TWO_WHEEL_DRIVE = 'TWO_WHEEL_DRIVE', '2 Wheel Drive'
        FOUR_WHEEL_DRIVE = 'FOUR_WHEEL_DRIVE', '4 Wheel Drive'
        ALL_WHEEL_DRIVE = 'ALL_WHEEL_DRIVE', 'All Wheel Drive'
        UNSPECIFIED = 'UNSPECIFIED', 'Unspecified'

    class Steering(models.TextChoices):
        LEFT = 'LEFT', 'Left'
        RIGHT = 'RIGHT', 'Right'
        UNSPECIFIED = 'UNSPECIFIED', 'Unspecified'


    JANUARY = 1
    FEBUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

    MONTH_CHOICES = (
        (JANUARY, 'January'),
        (FEBUARY, 'February'),
        (MARCH, 'March'),
        (APRIL, 'April'),
        (MAY, 'May'),
        (JUNE, 'June'),
        (JULY, 'July'),
        (AUGUST, 'August'),
        (SEPTEMBER, 'September'),
        (OCTOBER, 'October'),
        (NOVEMBER, 'November'),
        (DECEMBER, 'December')
    )

    number_plate = models.CharField(max_length=20, unique=True)
    country_of_registration = models.ForeignKey(Country, related_name='vehicles', on_delete=models.CASCADE)
    chasis_number = models.CharField(max_length=255)
    registration_year = models.PositiveSmallIntegerField()
    registration_month = models.PositiveSmallIntegerField(
        choices=MONTH_CHOICES,
    )
    manufacture_year = models.PositiveSmallIntegerField()
    manufacture_month = models.PositiveSmallIntegerField(
        choices=MONTH_CHOICES,
    )
    vehicle_model = models.ForeignKey(VehicleModel, related_name='vehicles', on_delete=models.CASCADE)
    vehicle_model_code = models.CharField(max_length=255)
    engine_size = models.PositiveSmallIntegerField()

    exterior_color = models.CharField(
        choices=Color.choices,
        max_length=50,
        default=Color.UNSPECIFIED)

    fuel = models.CharField(
        choices=Fuel.choices,
        max_length=50,
        default=Fuel.UNSPECIFIED
    )

    transmission = models.CharField(
        choices=Transmission.choices,
        max_length=50,
        default=Transmission.UNSPECIFIED
    )

    body_type = models.CharField(
        choices=BodyType.choices,
        max_length=50,
        default=BodyType.UNSPECIFIED
    )

    drive_train = models.CharField(
        choices=DriveTrain.choices,
        max_length=50,
        default=DriveTrain.UNSPECIFIED
    )

    steering = models.CharField(
        choices=Steering.choices,
        max_length=50,
        default=Steering.UNSPECIFIED
    )

    vehicle_image = models.ForeignKey(
        File,
        related_name='vehicle_images',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'''{self.manufacture_year}
                    {self.vehicle_model.vehicle_make.vehicle_make_name}
                    {self.vehicle_model.vehicle_model_name}
                    {self.vehicle_model_code}
                    '''
    class Meta:
        constraints = [
            models.CheckConstraint(
                name='registration_year_between_1950_and_current_year',
                check=Q(registration_year__gte=1950) & Q(registration_year__lte=date.today().year)
            ),
            models.CheckConstraint(
                name='registration_month_between_1_and_12',
                check=Q(registration_month__gte=1) & Q(registration_month__lte=12)
            ),
            models.CheckConstraint(
                name='manufacture_year_between_1950_and_current_year',
                check=Q(manufacture_year__gte=1950) & Q(manufacture_year__lte=date.today().year)
            ),
            models.CheckConstraint(
                name='manufacture_month_between_1_and_12',
                check=Q(manufacture_month__gte=1) & Q(manufacture_month__lte=12)
            ),
        ]