from graphene import(
    ObjectType,
    Mutation,
    String,
    Field,
    Int,
    Boolean
)

from api_config import (
    db
)

from .objects import (
    Gerente,
    Hotel,
    Habitacion
)

from .gerente import Gerente as GerenteModel
from .hotel import Hotel as HotelModel
from .habitacion import Habitacion as HabitacionModel


# Gerente Mutation

class createGerente(Mutation):
    class Arguments:
        dni = Int(required=True)
        name = String(required=True)
        last_name = String(required=True)
        telefono = Int(required=True)
    
    gerente = Field(lambda: Gerente)

    def mutate(self, info, dni, name, last_name, telefono):
        gerente = GerenteModel(dni=dni, name=name, last_name=last_name, telefono=telefono)

        db.session.add(gerente)
        db.session.commit()
        
        return createGerente(gerente=gerente)

class updateGerente(Mutation):
    class Arguments:
        gerente_dni = Int(required=True)
        name = String()
        last_name = String()
        telefono = Int()

    gerente = Field(lambda: Gerente)

    def mutate(self, info, gerente_dni, telefono=None, name=None, last_name=None):
        gerente = GerenteModel.query.get(gerente_dni)
        if gerente:
            if(telefono):
                gerente.telefono = telefono
            if(name):
                gerente.name = name
            if(last_name):
                gerente.last_name = last_name
            db.session.add(gerente)
            db.session.commit()

        return updateGerente(gerente=gerente)

class deleteGerente(Mutation):
    class Arguments:
        gerente_dni = Int(required=True)

    gerente = Field(lambda: Gerente)

    def mutate(self, info, gerente_dni):
        gerente = GerenteModel.query.get(gerente_dni)
        if gerente:
            db.session.delete(gerente)
            db.session.commit()

        return deleteGerente(gerente=gerente)

# Hotel Mutation

class createHotel(Mutation):
    class Arguments:
        name = String(required=True)
        direccion = String(required=True)
        estrellas = Int(required=True)
        gerente_fk = Int(required=True)
    
    hotel = Field(lambda: Hotel)

    def mutate(self, info, name, direccion, estrellas, gerente_fk):
        hotel = HotelModel(name=name, direccion=direccion, estrellas=estrellas, gerente_fk=gerente_fk)

        db.session.add(hotel)
        db.session.commit()
        
        return createHotel(hotel=hotel)

class updateHotel(Mutation):
    class Arguments:
        hotel_id = Int(required=True)
        name = String()
        direccion = String()
        estrellas = Int()
        gerente_fk = Int()

    hotel = Field(lambda: Hotel)

    def mutate(self, info, hotel_id, direccion=None, name=None, estrellas=None, gerente_fk=None):
        hotel = HotelModel.query.get(hotel_id)
        if hotel:
            if(direccion):
                hotel.direccion = direccion
            if(name):
                hotel.name = name
            if(estrellas):
                hotel.estrellas = estrellas
            if(gerente_fk):
                hotel.gerente_fk = gerente_fk
            db.session.add(hotel)
            db.session.commit()

        return updateHotel(hotel=hotel)

class deleteHotel(Mutation):
    class Arguments:
        hotel_id = Int(required=True)

    hotel = Field(lambda: Hotel)

    def mutate(self, info, hotel_id):
        hotel = HotelModel.query.get(hotel_id)
        if hotel:
            db.session.delete(hotel)
            db.session.commit()

        return deleteHotel(hotel=hotel)

# Habitacion Mutation

class createHabitacion(Mutation):
    class Arguments:
        numero = Int(required=True)
        precio = Int(required=True)
        disponible = Boolean(required=True)
        hotel_fk = Int(required=True)
    
    habitacion = Field(lambda: Habitacion)

    def mutate(self, info, numero, precio, disponible, hotel_fk):
        habitacion = HabitacionModel(numero=numero, precio=precio, disponible=disponible, hotel_fk=hotel_fk)

        db.session.add(habitacion)
        db.session.commit()
        
        return createHabitacion(habitacion=habitacion)

class updateHabitacion(Mutation):
    class Arguments:
        habitacion_id = Int(required=True)
        numero = Int()
        precio = Int()
        disponible = Boolean()
        hotel_fk = Int()

    habitacion = Field(lambda: Habitacion)

    def mutate(self, info, habitacion_id, numero=None, precio=None, disponible=None, hotel_fk=None):
        habitacion = HabitacionModel.query.get(habitacion_id)
        if habitacion:
            if(numero):
                habitacion.numero = numero
            if(precio):
                habitacion.precio = precio
            if(disponible):
                habitacion.disponible = disponible
            if(hotel_fk):
                habitacion.hotel_fk = hotel_fk
            db.session.add(habitacion)
            db.session.commit()

        return updateHabitacion(habitacion=habitacion)

class deleteHabitacion(Mutation):
    class Arguments:
        habitacion_id = Int(required=True)

    habitacion = Field(lambda: Habitacion)

    def mutate(self, info, habitacion_id):
        habitacion = HabitacionModel.query.get(habitacion_id)
        if habitacion:
            db.session.delete(habitacion)
            db.session.commit()

        return deleteHabitacion(habitacion=habitacion)

class Mutation(ObjectType):
    create_gerente = createGerente.Field()
    update_gerente = updateGerente.Field()
    delete_gerente = deleteGerente.Field()

    create_hotel = createHotel.Field()
    update_hotel = updateHotel.Field()
    delete_hotel = deleteHotel.Field()

    create_habitacion = createHabitacion.Field()
    update_habitacion = updateHabitacion.Field()
    delete_habitacion = deleteHabitacion.Field()