import string as st
import random as rn


class VehicleInfo:
    brand: str
    electric: bool
    catalogue_price: int

    def __init__(self, brand, electric, catalogue_price):
        self.brand = brand
        self.electric = electric
        self.catalogue_price = catalogue_price

    def compute_tax(self):
        tax_percentage = 0.1
        if self.electric:
            tax_percentage = 0.04

        return tax_percentage * self.catalogue_price

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Payable tax: {self.compute_tax()}")


class Vehicle:
    id: str
    licence_place: str
    info: VehicleInfo

    def __init__(self, id, licence_plate, info):
        self.id = id
        self.licence_plate = licence_plate
        self.info = info

    def print(self):
        print(f"ID: {self.id}")
        print(f"Licence Plate: {self.licence_plate}")
        self.info.print()


class VehicleRegister:

    vehicle_info = {}

    def __init__(self):
        self.add_vehicle_info("Test Model 3", True, 60000)
        self.add_vehicle_info("VW ID3", True, 35000)
        self.add_vehicle_info("BME e90", False, 27000)
        self.add_vehicle_info("Mercedes E220", False, 49800)

    def add_vehicle_info(self, brand, electric, catalogue_price):
        self.vehicle_info[brand] = VehicleInfo(brand, electric, catalogue_price)

    def generate_vehicle_id(self, length):
        return "".join(rn.choices(st.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        random_digits = "".join(rn.choices(st.digits, k=2))
        random_chars = "".join(rn.choices(st.ascii_uppercase, k=2))

        return f"{id[:2]}-{random_digits}-{random_chars}"

    def create_vehicle(self, brand):
        vehicle_id = self.generate_vehicle_id(12)
        vehicle_license_plate = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, vehicle_license_plate, self.vehicle_info[brand])


class Application:
    def regiser_vehicle(self, brand: str):
        # create a registry instance
        register = VehicleRegister()

        # create a vehicle
        vehicle = register.create_vehicle(brand)

        # print vehicle info
        vehicle.print()


app = Application()
app.regiser_vehicle("Test Model 3")
