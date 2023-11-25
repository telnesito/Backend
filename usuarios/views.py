from rest_framework import viewsets
from .serializer import UsuariosSerializer, PerfilEstudianteSerializer, PerfilProfesorSerializer, PerfilCoordinadorSerializer
from .models import Usuarios,PerfilEstudiante, PerfilProfesor, PerfilCoordinador
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

"""
    Metodos de usuarios
"""

@api_view(['GET', 'POST'])
def get_usuarios(request):
    if request.method == 'GET':
        user = Usuarios.objects.all()
        user_serializer=UsuariosSerializer(user, many = True)
        return Response(user_serializer.data)
    
    elif request.method == 'POST':
        user_serializer = UsuariosSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)
    
@api_view(['GET', 'PUT', 'DELETE'])
def get_usuario_especifico(request, pk):

    if request.method == 'GET':
        user = Usuarios.objects.filter(cedula = pk).first()
        user_serializer = UsuariosSerializer(user)
        return Response(user_serializer.data)
    elif request.method == 'PUT':
        user = Usuarios.objects.filter(cedula = pk).first()
        user_serializer = UsuariosSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)
    elif request.method == 'DELETE':
        user = Usuarios.objects.filter(cedula = pk).first()
        user = user.delete() 
        return Response('Eliminado')
        
        
        
    
"""
    Metodos de perfil estudiante
"""
@api_view(['GET', 'POST'])
def get_usuarios_estudiantes(request):
    if request.method == 'GET':
        perfil_estudiante = PerfilEstudiante.objects.all()
        perfil_estudiante_serializer = PerfilEstudianteSerializer(perfil_estudiante, many=True)
        return Response(perfil_estudiante_serializer.data)
    
    elif request.method == 'POST':
        perfil_estudiante_serializer =PerfilEstudianteSerializer(data = request.data)
        if perfil_estudiante_serializer.is_valid():
            perfil_estudiante_serializer.save()
            return Response(perfil_estudiante_serializer.data)
        return Response(perfil_estudiante_serializer.errors)

     
    # elif request.method == 'POST':
    #     user_serializer = UsuariosSerializer(data=request.data)
    #     if user_serializer.is_valid():
    #         user_serializer.save()
    #         return Response(user_serializer.data)
    #     return Response(user_serializer.errors)
    
@api_view(['GET', 'PUT', 'DELETE'])
def estudianteEspecifico(request, pk):

    if request.method == 'GET':
        estudiante = PerfilEstudiante.objects.filter(cedula = pk).first()
        estudiante_serializer = PerfilEstudianteSerializer(estudiante)
        return Response(estudiante_serializer.data)
    
    if request.method == 'PUT':
        estudiante = PerfilEstudiante.objects.filter(cedula = pk).first()
        estudiante_serializer = PerfilEstudianteSerializer(estudiante, data = request.data)
        if estudiante_serializer.is_valid():
            estudiante_serializer.save()
            return Response(estudiante_serializer.data)
        return Response(estudiante_serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def get_usuario_especifico(request, pk):

#     if request.method == 'GET':
#         user = Usuarios.objects.filter(cedula = pk).first()
#         user_serializer = UsuariosSerializer(user)
#         return Response(user_serializer.data)
#     elif request.method == 'PUT':
#         user = Usuarios.objects.filter(cedula = pk).first()
#         user_serializer = UsuariosSerializer(user, data=request.data)
#         if user_serializer.is_valid():
#             user_serializer.save()
#             return Response(user_serializer.data)
#         return Response(user_serializer.errors)
#     elif request.method == 'DELETE':
#         user = Usuarios.objects.filter(cedula = pk).first()
#         user = user.delete() 
#         return Response('Eliminado')

    
"""
    Metodos de perfil profesor
"""
@api_view(['GET'])
def get_usuarios_profesores(request):
    if request.method == 'GET':
        perfil_profesor = PerfilProfesor.objects.all()
        perfil_profesor_serializer = PerfilProfesorSerializer(perfil_profesor, many=True)
        return Response(perfil_profesor_serializer.data)
            
"""
    Metodos de perfil coordinador
"""

@api_view(['GET'])
def get_usuarios_coordinador(request):
    if request.method == 'GET':
        perfil_coordinador = PerfilCoordinador.objects.all()
        perfil_coordinador = PerfilCoordinadorSerializer(perfil_coordinador, many=True)
        return Response(PerfilCoordinadorSerializer.data)

