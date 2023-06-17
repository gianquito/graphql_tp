from graphene_sqlalchemy import (
    SQLAlchemyObjectType,
)
# from graphene import (
#     # Int
# )
# from models.funko import Funko as FunkoModel
# from models.user import User as UserModel
from models.gerente import Gerente as GerenteModel
from models.hotel import Hotel as HotelModel
from models.habitacion import Habitacion as HabitacionModel



class Gerente(SQLAlchemyObjectType):
    class Meta:
        model = GerenteModel

class Hotel(SQLAlchemyObjectType):
    class Meta:
        model = HotelModel

class Habitacion(SQLAlchemyObjectType):
    class Meta:
        model = HabitacionModel