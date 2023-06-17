from graphene import (
    ObjectType,
    String,
    Boolean,
    # relay,
    Field,
    List,
    Int
)

# from .funko import Funko as FunkoModel
# from .objects import (
#     Funko,
#     User,
# )
from .objects import Gerente, Hotel, Habitacion
from .gerente import Gerente as GerenteModel
from .hotel import Hotel as HotelModel
from .habitacion import Habitacion as HabitacionModel

class Query(ObjectType):
    hoteles = List(lambda: Hotel, name=String(), id=Int(), min_estrellas=Int(), order_by_name=Boolean())
    gerentes = List(lambda: Gerente, name=String(), dni=Int(), last_name=String())
    habitaciones = List(lambda: Habitacion, id=Int(), numero=Int(), max_precio=Int(), disponible=Boolean(), hotel_id=Int())

    def resolve_hoteles(self, info, id=None, name=None, min_estrellas=None, order_by_name=None):
        query = Hotel.get_query(info=info)
        if id:
            query = query.filter(HotelModel.id==id)
        if name:
            query = query.filter(HotelModel.name==name)
        if min_estrellas:
            query.filter(HotelModel.estrellas >= min_estrellas)
        if order_by_name is not None:
            if order_by_name:
                query = query.order_by(HotelModel.name)
        return query.all()
    
    def resolve_gerentes(self, info, dni=None, name=None, last_name=None):
        query = Gerente.get_query(info=info)
        if dni:
            query = query.filter(GerenteModel.dni==dni)
        if name:
            query = query.filter(GerenteModel.name==name)
        if last_name:
            query = query.filter(GerenteModel.last_name==last_name)
        return query.all()
    
    def resolve_habitaciones(self, info, id=None, numero=None, max_precio=None, disponible=None, hotel_id=None):
        query = Habitacion.get_query(info=info)
        if id:
            query = query.filter(HabitacionModel.id==id)
        if numero:
            query = query.filter(HabitacionModel.numero==numero)
        if max_precio:
            query = query.filter(HabitacionModel.precio <= max_precio)
        if disponible is not None:
            query = query.filter(HabitacionModel.disponible == disponible)
        if hotel_id:
            query = query.filter(HabitacionModel.hotel_fk == hotel_id)
        return query.all()