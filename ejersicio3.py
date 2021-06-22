from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

lista_Integrantes = [{'item_id': 1, 'matricula': 918765432, 'nombre': 'Juan', 'edad': 21, 'APaterno': 'López','AMaterno': 'Girón', 'correo': 'juan@utselva.edu', 'telefono': 9191778245, 'carrera': 'Redes'},
                    {'item_id': 2, 'matricula': 918765423, 'nombre': 'Pedro', 'edad': 22, 'APaterno': 'Santiz','AMaterno': 'Luna', 'correo': 'pedro@utselva.edu', 'telefono': 9191778457, 'carrera': 'Intligencia'},
                    {'item_id': 3, 'matricula': 918765445, 'nombre': 'Lupe', 'edad': 23, 'APaterno': 'Trujillo','AMaterno': 'Girón', 'correo': 'lupe@utselva.edu', 'telefono': 9191771457, 'carrera': 'Seguridad privada'},
                    {'item_id': 4, 'matricula': 918765457, 'nombre': 'Jose', 'edad': 30, 'APaterno': 'Sanchez','AMaterno': 'Guttierrez', 'correo': 'jose@utselva.edu', 'telefono': 919177457, 'carrera': 'Inginiero'},
                    {'item_id': 5, 'matricula': 918761456, 'nombre': 'Andres', 'edad': 28, 'APaterno': 'Carvajal','AMaterno': 'Vargas', 'correo': 'andres@utselva.edu', 'telefono': 919177789, 'carrera': 'Agronomia'},
                    {'item_id': 6, 'matricula': 918765456, 'nombre': 'Cristiano', 'edad': 26, 'APaterno': 'Acero','AMaterno': 'Monroy', 'correo': 'cristiano@utselva.edu', 'telefono': 919177478, 'carrera': 'contaduria'},
                    {'item_id': 7, 'matricula': 918765478, 'nombre': 'Gerard', 'edad': 35, 'APaterno': 'Villa','AMaterno': 'Garcia', 'correo': 'Gerard@utselva.edu', 'telefono': 919177546, 'carrera': 'Ad. Empresas'},
                    {'item_id': 8, 'matricula': 918764579, 'nombre': 'Leo', 'edad': 20, 'APaterno': 'Rocha','AMaterno': 'Martinez', 'correo': 'Leo@utselva.edu', 'telefono': 9191774457, 'carrera': 'Relaciones Exteriores'},
                    {'item_id': 9, 'matricula': 918765479, 'nombre': 'Ana', 'edad': 24, 'APaterno': 'Fernandez','AMaterno': 'Ruiz', 'correo': 'Ana@utselva.edu', 'telefono': 9191774564, 'carrera': 'ing. Computacion'},
                    {'item_id': 10, 'matricula': 918764794, 'nombre': 'Eva', 'edad': 25, 'APaterno': 'Rodriguez','AMaterno': 'Botero', 'correo': 'eva@utselva.edu', 'telefono': 9191774733, 'carrera': 'Inginiero'}]

@app.get('/integrantes')
async def read_integrntes(item_id: int):
    for diccionario in lista_Integrantes:
        if diccionario.get('item_id') == item_id:
            respuesta = f"""
            <html>
            <head>
                <title>{diccionario.get('nombre')}</title>
            </head>
            <body>
            <h3>Sitio personal {diccionario.get('nombre')}</h3>
            <ul>
                <li>Matricula: {diccionario.get('matricula')}</li>
                <li strong>APaterno: {diccionario.get('APaterno')}
                <li>AMaterno: {diccionario.get('AMaterno')}</li>
                <li>Nombre: {diccionario.get('nombre')}</li>
                <li>Edad: {diccionario.get('edad')} </li>
                <li>Correo: {diccionario.get('correo')}</li>
                <li>Telefono: {diccionario.get('telefono')}</li>
                <li>Carrera: {diccionario.get('carrera')}</li>
            </ul>
            </body>
            </html>
            """
            return HTMLResponse(content=respuesta, status_code=200)
    return "No se encontro el registro"