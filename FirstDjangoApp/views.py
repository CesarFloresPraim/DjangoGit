from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from FirstDjangoApp.forms import RegistrationForm, VentaNuevaForm
from django.contrib.auth import hashers
from .models import Administrador, Ventas, Articulos, IncentivosDiarios, HoraSesion
from datetime import timedelta, date
from django.template import loader
from django.core import serializers
from django.core.exceptions import ValidationError
from django.db.models import Sum
import json
import datetime


# from django.views.decorators.csrf import csrf_exempt --> Avoids csrf verification

# Create your views here.

class Istore(TemplateView):
    template_name = 'FirstDjangoApp/verticalNav.html'

    def get(self, request, *args, **kwargs):

        if 'usuario' in request.session:
            usuario = request.session['usuario']
            usuarios = Administrador.objects.get(usuario__exact=usuario)
            hora_de_sesion = datetime.datetime.now().time()
            args = {
                'usuario': usuario,
            }
            if usuarios.tipo == 'Administrador':
                return render(request, self.template_name, args)
            elif usuarios.tipo == 'Tecnico':
                dia_num = datetime.datetime.today().weekday()
                dia = dia_to_text(dia_num)
                if hora_de_sesion < usuarios.hora_entrada:
                    incentivo = IncentivosDiarios.objects.get(dia=dia)
                    nueva_sesion = HoraSesion(usuario=usuario, hora_entrada=usuarios.hora_entrada, hora_sesion=hora_de_sesion, cantidad_incentivo=incentivo.bono_puntualidad)
                    nueva_sesion.save()
                return render(request, 'FirstDjangoApp/verticalNav2.html', args)

        return redirect('FirstDjangoApp:Usuarios')

    def post(self, request):

        if 'salir' in request.POST:
            try:
                if 'usuario' in request.session:
                    del request.session['usuario']
            except KeyError:
                pass
            return redirect('FirstDjangoApp:Usuarios')


def buscar_empleado(request):
    empleados = Administrador.objects.exclude(tipo='Administrador')
    suma_bonos_sesiones = 0
    html_codigo = ""
    for empleado in empleados:

        start_date = empleado.fecha_ultimo_pago
        end_date = datetime.date.today() + timedelta(days=1)
        suma_bonos_sesiones = 0
        suedo_base = empleado.salario
        dias_laborados = 0
        for single_date in daterange(start_date, end_date):
            bonos_sesiones = HoraSesion.objects.filter(fecha_sesion=single_date).filter(usuario=empleado.usuario)
            dias_laborados += 1
            for bono in bonos_sesiones:
                suma_bonos_sesiones += bono.cantidad_incentivo
        suedo_diario = suedo_base/6

        suma_bonos_sesiones += suedo_diario*dias_laborados

        html_codigo += """
        <div class="col-sm-3 p-card">
            <img src="../../static/img/card-{0}.jpg" alt="" class="img-thumbnail">
            <div class="down-card">
                <div class="row">
                    <div class="col-xs-12">
                        <p class="texto-centrado">{0}</p>
                        <p class="texto-centrado">{1}</p>
                        <p class="texto-centrado">{2}</p>
                    </div>
                    <div class="col-xs-12">
                        <button type="button" style="background-color: #2ecc71; width: 100%">Pagar</button>
                    </div>
                    <div class="col-xs-12">
                        <button type="button"  id="{0}" style="background-color: #2980b9; width: 100%"
                                onclick="mostrarDetallesEmpleado(true, this)">Detalles
                        </button>
                    </div>
                </div>
            </div>
        </div>
        """.format(empleado.usuario, suma_bonos_sesiones, dias_laborados)

    args = {
        'html_codigo':  html_codigo,
    }
    return JsonResponse(args)


def dia_to_text(dia_number):
    switcher = {
        0: 'Lunes',
        1: 'Martes',
        2: 'Miercoles',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sabado',
        6: 'Domingo',
    }
    return switcher.get(dia_number, 'Dia invalido')


def operaciones(request):
    datos_a_modificar = request.POST['operaciones']
    if datos_a_modificar == 'incentivos':
        incentivos = IncentivosDiarios.objects.all()
        incentivos = [incentivos_serializer(incentivo) for incentivo in incentivos]
        html_codigo = """
                <table class="table table-hover">
                    <tr>
                        <th class='thincentivo'>Dia</th>
                        <th class='thincentivo'>Incentivo</th>
                        <th class='thincentivo'>Modificar<th>
                    </tr>
            """
        for i in incentivos:
            html_codigo += """
                    <tr>
                        <td>{0}</td>
                        <td>{1}</td>
                        <td><button type="button" onclick="alterarDiaSelect('{0}')">Seleccionar</button></td>
                    </tr>      
                """.format(i['dia'], i['bono_puntualidad'])
        html_codigo += """
                </table>
            """
        args = {
            'html_codigo': html_codigo,
            'operacion': datos_a_modificar,
        }
        return JsonResponse(args)
    elif datos_a_modificar == 'hora_llegada':
        tecnicos = Administrador.objects.exclude(tipo="Administrador")
        html_codigo = """
        <table class="table table-hover">
                    <tr>
                        <th class='thhora-entrada'>Tecnico</th>
                        <th class='thhora-entrada'>Hora de Entrada</th>
                        <th class='thhora-entrada'>Modificar<th>
                    </tr>
        """
        for i in tecnicos:
            html_codigo += """
                <tr>
                        <td>{0}</td>
                        <td>{1}</td>
                        <td><button type="button" onclick="alterarTecnicoSelect('{0}')">Seleccionar</button></td>
                    </tr>
            """.format(i.usuario, i.hora_entrada)

        html_codigo += """
            </table>
        """
        args = {
            'html_codigo': html_codigo,
            'operacion': datos_a_modificar,
        }
        return JsonResponse(args)

    elif datos_a_modificar == 'comisiones':
        articulos = Articulos.objects.all()
        html_codigo = """
        <table class="table" id="tablee-mostrar-articulos">
        <thead>
                    <tr>
                        <th class='tharticulos'>Articulo</th>
                        <th class='tharticulos'>Precio</th>
                        <th class='tharticulos'>Costo</th>
                        <th class='tharticulos'>Comision</th>
                        <th class='tharticulos'>Objetivo</th>
                        <th class='tharticulos'>Modificar</th>
                    </tr>
                </thead>
            <tbody>
        """

        for i in articulos:
            html_codigo += """
            <tr id="modificar-{5}">
                <td style="min-width: 200px">{0}</td>
                <td>{1}</td>
                <td>{2}</td>
                <td>{3}</td>
                <td>{4}</td>
                <td><button type="button" onclick="seleccionarFilaArticulo('{5}')">Seleccionar</button></td>
            </tr>
            """.format(i.descripcion, i.precio, i.costo, i.comision_empleado, i.objetivo_venta,
                       i.descripcion.replace(" ", ""))

        html_codigo += """
        </tbody>
        </table>
        """
        args = {
            'html_codigo': html_codigo,
            'operacion': datos_a_modificar,
        }
        return JsonResponse(args)
    return HttpResponse("hola", content_type='text/html')


def incentivos(request):
    dia = request.POST['diaIncentivo']
    cantidad = request.POST['cantidadIncentivo']

    incentivo_modificar = IncentivosDiarios.objects.get(dia=dia)
    incentivo_modificar.bono_puntualidad = cantidad
    try:
        incentivo_modificar.save()
    except ValidationError as e:
        return HttpResponse(e.messages, content_type='text/html')
        # Do something based on the errors contained in e.message_dict.
        # Display them to a user, or handle them programmatically.
    except ValueError as e:
        return HttpResponse(e, content_type='text/html')

    incentivo_modificar.save()
    return HttpResponse("Success", content_type="text/html")


def hora(request):
    tecnico = request.POST['nombre-tecnico']
    hora_entrada = request.POST['hora-entrada']

    tecnico_modificar = Administrador.objects.get(usuario=tecnico)
    tecnico_modificar.hora_entrada = hora_entrada

    try:
        tecnico_modificar.save()
    except ValidationError as e:
        return HttpResponse(e.messages, content_type='text/html')
        # Do something based on the errors contained in e.message_dict.
        # Display them to a user, or handle them programmatically.
        pass
    tecnico_modificar.save()

    return HttpResponse("Success")


def comision(request):
    articulo = request.POST['articulo']
    articulo = json.loads(articulo)

    articulo_a_modificar = Articulos.objects.get(descripcion=articulo['descripcion'])
    articulo_a_modificar.precio = articulo['precio']
    articulo_a_modificar.costo = articulo['costo']
    articulo_a_modificar.comision_empleado = articulo['comision']
    articulo_a_modificar.objetivo_venta = articulo['objetivo']

    try:
        articulo_a_modificar.save()
    except ValidationError as e:
        return HttpResponse(e.messages, content_type='text/html')
        # Do something based on the errors contained in e.message_dict.
        # Display them to a user, or handle them programmatically.
    except ValueError as e:
        return  HttpResponse(e)

    articulo_a_modificar.save()
    return  HttpResponse("Success")


def incentivos_serializer(incentivo):
    return {'dia': incentivo.dia, 'bono_puntualidad': incentivo.bono_puntualidad}


def get_chart_data(request):
    tipo_grafica = request.GET['tipo_grafica']
    datos_a_graficar = request.GET['datos_a_graficar']
    start_date = request.GET['fecha_inicio']
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date = request.GET['fecha_fin']
    end_date_1 = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
    end_date = end_date_1 + datetime.timedelta(days=1)
    data = []
    labels = []

    if datos_a_graficar == 'ganancias':
        for single_date in daterange(start_date, end_date):
            ganancias_por_fecha = Ventas.objects.filter(fecha__startswith=single_date).aggregate(total=Sum('precio'))
            data.append(ganancias_por_fecha['total'])
            labels.append(single_date)
    else:
        for single_date in daterange(start_date, end_date):
            ventas_por_fecha = Ventas.objects.filter(fecha__startswith=single_date)
            data.append(ventas_por_fecha.count())
            labels.append(single_date)

    """
    elif datos_a_graficar == 'ventas_tecnico':
        tecnicos = Administrador.objects.all()
        for tecnico in tecnicos:
            ventas_tecnico_suma = 0
            for single_date in daterange(start_date, end_date):
                ventas_tecnico = Ventas.objects.filter(fecha__startswith=single_date, realizada_por=tecnico['nombre'])
                ventas_tecnico_suma += ventas_tecnico.count()
            data.append(ventas_tecnico_suma)
            labels.append(tecnico['nombre'])
    """
    args = {
        'labels': labels,
        'data': data,
        'tipo_grafica': tipo_grafica,
    }
    return JsonResponse(args)  # igual que return HttpResponse(argss, content_type='application/json')


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)-1):
        yield (start_date + timedelta(days=1)) + timedelta(n)


def buscar_articulos(request):
    articulo_buscar = request.GET['buscar-articulos']
    articulos = Articulos.objects.filter(descripcion__icontains=articulo_buscar)
    articulos = [articulo_serializer(articulo) for articulo in
                 articulos]  # Crea una lista de diccinarios y no de objetos
    html_codigo = ""
    for i in articulos:
        html_codigo += """
        <div class="agregarArticuloATabla" style="display: inline-block">
            <img src="../../static/img/{0}.jpg" class="tamanio-imagen" onclick='agregarATabla(this, true)' id='{0}' >
            <div class="polar-abajo" style="height: 60px; width: 180px">
                <p class='sin-margin-bot'> {0} </p>
                <p class='sin-margin-bot' id='{2}_precio'>{1} </p>
            </div>
        </div>
        """.format(i['descripcion'], i['precio'], i['descripcion'].replace(" ", ""))

    return HttpResponse(html_codigo, content_type='text/html')


def articulo_serializer(articulo):
    return {'descripcion': articulo.descripcion, 'precio': articulo.precio, 'costo': articulo.costo}


def registrar_venta(request):
    ventas = request.POST['ventas']
    metodo_de_pago = request.POST['metodo_de_pago']
    if "usuario" in request.session:
        usuario = request.session["usuario"]
    else:
        usuario = "None"

    ventas = json.loads(ventas)
    for venta in ventas:

        articulo = Articulos.objects.filter(descripcion=venta['descripcion'])
        venta = Ventas(cantidad=venta['cantidad'], descripcion=venta['descripcion'], precio=venta['precio'],
                       costo=articulo[0].costo, metodo_de_pago=metodo_de_pago, realizada_por=usuario)
        try:
            venta.full_clean()
        except ValidationError as e:
            return HttpResponse(e.messages, content_type='text/html')
            # Do something based on the errors contained in e.message_dict.
            # Display them to a user, or handle them programmatically.
        venta.save()
    return HttpResponse("Success", content_type='text/html')


def buscar(request):
    fecha_buscar = request.GET['fecha']
    ventas = Ventas.objects.filter(fecha__startswith=fecha_buscar)  # Regresa unal ista de objetos buscados
    ventas = [venta_serializer(venta) for venta in ventas]  # Crea una lista de diccinarios y no de objetos
    # array_ventas = json.dumps(ventas, default=myconverter)
    html_codigo = """
    <table id="ventas_actuales" class="table table-hover">
        <tr>
        <th class="thventas">Fecha/Hora</th>
        <th class="thventas">Cantidad</th>
        <th class="thventas">Descripcion</th>
        <th class="thventas verdePrecio">Precio</th>
        <th class="thventas rojoCosto">Costo</th>
        <th class="thventas">Metodo de Pago</th>
        <th class="thventas">Tecnico</th>
    </tr>"""
    suma_precio, suma_costo = 0, 0

    for i in ventas:
        # Calcular suma de precios y costos
        suma_precio += float(i['precio'])
        suma_costo += float(i['costo'])
        html_codigo += """
            <tr>
                <td> {0} </td>
                <td> {1} </td>
                <td> {2} </td>
                <td> {3} </td>
                <td> {4} </td>
                <td> {5} </td>
                <td> {6} </td>
            </tr>""".format(i['fecha'], i['cantidad'], i['descripcion'], i['precio'], i['costo'], i['metodo_de_pago'],
                            i['realizada_por'])
    html_codigo += "</table>"
    total = suma_precio - suma_costo
    args = {
        'html_codigo': html_codigo,
        'suma_precio': suma_precio,
        'suma_costo': suma_costo,
        'total': total
    }
    argss = json.dumps(args)

    # return HttpResponse(array_ventas,content_type='applications/json')
    return HttpResponse(argss, content_type='application/json')


def myconverter(o):  # Cambiar el tipo date para que puede ser serializable por json
    if isinstance(o, datetime.datetime):
        return o.__str__()


def venta_serializer(venta):
    return {'fecha': venta.fecha, 'cantidad': venta.cantidad, 'descripcion': venta.descripcion,
            'precio': venta.precio, 'costo': venta.costo, 'metodo_de_pago': venta.metodo_de_pago,
            'realizada_por': venta.realizada_por}


class Usuarios(TemplateView):
    template_name = 'FirstDjangoApp/index.html'

    def get(self, request, *args, **kwargs):
        if 'usuario' in request.session:
            return redirect('FirstDjangoApp:Istore')

        return render(request, self.template_name)

    def post(self, request):
        administrador = request.POST['usuario']
        contrasenia = request.POST['contrasenia']
        user = Administrador.objects.raw('SELECT * FROM FirstDjangoApp_administrador WHERE usuario=%s', [administrador])
        if hashers.check_password(contrasenia, user[0].contrasenia1) == False:
            return render(request, self.template_name)

        request.session['usuario'] = administrador
        return redirect('FirstDjangoApp:Istore')


class Registrar(TemplateView):
    template_name = 'FirstDjangoApp/Register.html'

    def get(self, request, *args, **kwargs):
        form = RegistrationForm
        args = {
            'form': form,
        }
        return render(request, self.template_name, args)

    def post(self, request):
        administrador = RegistrationForm(request.POST)
        if administrador.is_valid():  # Form sea valido
            contrasenia1 = administrador.cleaned_data['contrasenia1']  # Obtiene la contraseña 1 limpia
            contrasenia2 = request.POST['psw_repeat']  # Obtiene contraseña 2
            if contrasenia1 != contrasenia2:  # Compara las 2 contraseñas
                return HttpResponse("Error, las contraseñas no coinciden")  # Si no son iguales te regresa a la pagina

            # Si son iguales modifica la contraseña en texto plano a una encriptada
            hashed_administrador = administrador.save(commit=False)
            hashed_administrador.contrasenia1 = hashers.make_password(contrasenia1, salt=None, hasher='default')
            hashed_administrador.save()  # Guarda el administrador con los datos cambiados
            return redirect('FirstDjangoApp:Usuarios')  # Redirige a inicio de sesion

        return HttpResponse("Error al registrar usuario nuevo")  # Si el form no es valido te regresa a la pagina


# Function-Based view #
"""
def Registrar(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            contrasenia2 = form.cleaned_data.get('contrasenia2')
        return redirect('FirstDjangoApp:Usuarios')
    else:
        form = RegistrationForm()

    return render(request, 'FirstDjangoApp/Register.html', {'form':form})

"""
