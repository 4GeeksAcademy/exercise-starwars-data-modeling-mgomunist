import os
import sys
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    TIMESTAMP,
    create_engine,
)
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

# Definición base para las clases
BaseDeclarativa = declarative_base()

# Clase que representa a los Usuarios
class Usuario(BaseDeclarativa):
    __tablename__ = 'usuarios'
    id_usuario = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    contrasena = Column(String(60), nullable=False)
    nombre_usuario = Column(String(30), nullable=False)
    fecha_creacion = Column(TIMESTAMP, nullable=False)

    favoritos = relationship("Favorito", back_populates="usuario")

# Clase que representa a los Planetas
class Planeta(BaseDeclarativa):
    __tablename__ = 'planetas'
    id_planeta = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    clima = Column(String(100), nullable=True)
    terreno = Column(String(100), nullable=True)
    poblacion = Column(Integer, nullable=True)

# Clase que representa a los Personajes
class Personaje(BaseDeclarativa):
    __tablename__ = 'personajes'
    id_personaje = Column(Integer, primary_key=True)
    nombre = Column(String(150), nullable=False)
    especie = Column(String(100), nullable=True)
    planeta_origen = Column(String(100), nullable=True)
    genero = Column(String(20), nullable=True)

# Clase que representa a los Favoritos
class Favorito(BaseDeclarativa):
    __tablename__ = 'favoritos'
    id_favorito = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'), nullable=False)
    id_planeta = Column(Integer, ForeignKey('planetas.id_planeta'), nullable=True)
    id_personaje = Column(Integer, ForeignKey('personajes.id_personaje'), nullable=True)
    tipo_favorito = Column(String(50), nullable=False)

    usuario = relationship("Usuario", back_populates="favoritos")
    planeta = relationship("Planeta", backref="favoritos")
    personaje = relationship("Personaje", backref="favoritos")

# Generación del diagrama basado en el modelo
try:
    render_er(BaseDeclarativa, 'diagrama.png')
    print("¡Éxito! Revisa el archivo diagrama.png")
except Exception as e:
    print("Hubo un problema al generar el diagrama.")
    raise e

