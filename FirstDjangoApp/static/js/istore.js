/*----Esconde/muestra el nav----*/
function hideNav() {
    var width_nav = parseInt($("#nav").width());
    if ($(window).width() < 450) {

    } else if (width_nav > 70) { //si el nav esta ampliado
        $("#nav").css({"width": 60 + 'px'});
        $("#opcionInicio").html("<i class=\"fas fa-at  \"></i>");
        $("#opcionVender").html("<i class=\"fas fa-dollar-sign \"></i>");
        $("#opcionVentas").html("<i class=\"fas fa-chart-line \"></i>");
        $("#opcionHerramientas").html("<i class=\"fas fa-database \"></i>");
        $("#opcionGastos").html("<i class=\"fas fa-money-bill-alt \"></i>");
        $("#opcionPIB").html("<i class=\"fas fa-chart-pie \"></i>");
        $("#salir").html("<i class=\"fas fa-power-off \"></i>");
        document.getElementById("fecha").innerHTML = "";
        newContainerPrincipalSize();

    } else if (width_nav < 70) { //Si el nav esta reducido
        $("#nav").css({"width": 200 + 'px'});
        $("#opcionInicio").html("<i class=\"fas fa-at  \"></i>&nbspInicio");
        $("#opcionVender").html("<i class=\"fas fa-dollar-sign \"></i>&nbspTienda");
        $("#opcionVentas").html("<i class=\"fas fa-chart-line \"></i>&nbspVentas");
        $("#opcionHerramientas").html("<i class=\"fas fa-database \"></i>&nbspTools");
        $("#opcionGastos").html("<i class=\"fas fa-money-bill-alt \"></i>&nbspGastos");
        $("#opcionPIB").html("<i class=\"fas fa-chart-pie \"></i>&nbspPIB");
        $("#salir").html("<i class=\"fas fa-power-off \"></i>&nbspSalir");
        newContainerPrincipalSize();

    }


}

/*----Verifica si es un celular----*/
function celularNav() {
    if ($(window).width() < 450) { //Ancho de pantalla menor a 645px

        $("#nav").css({"width": 50 + 'px'});

        //$("#data-usuario").hide();
        $("#opcionInicio").html("<i class=\"fas fa-at  \"></i>");
        $("#opcionVender").html("<i class=\"fas fa-dollar-sign \"></i>");
        $("#opcionVentas").html("<i class=\"fas fa-chart-line \"></i>");
        $("#opcionHerramientas").html("<i class=\"fas fa-database \"></i>");
        $("#opcionGastos").html("<i class=\"fas fa-money-bill-alt \"></i>");
        $("#opcionPIB").html("<i class=\"fas fa-chart-pie \"></i>");
        $("#salir").html("<i class=\"fas fa-power-off \"></i>");
        document.getElementById("fecha").innerHTML = "";

    }
    newContainerPrincipalSize();
}

/*----Crea el contenedor principal----*/
function newContainerPrincipalSize() {
    var $containerPrincipal = $(".container-principal");
    var width_nav = parseInt($("#nav").width());
    var widthContainerPrincipal = parseInt($(window).width()) - width_nav - 20;
    $containerPrincipal.css({"max-width": widthContainerPrincipal + "px"});
    $containerPrincipal.css({"width": widthContainerPrincipal + "px"});
    $containerPrincipal.css({"margin-left": width_nav + 10 + "px"});

    var heightContainerPrincipal = parseInt($(window).height()) - 80; //-60 de fixed menubar y 10 de paddings de cada lado
    $containerPrincipal.css({"height": heightContainerPrincipal + "px"});
    $containerPrincipal.css({"max-height": heightContainerPrincipal + "px"});
}

/*----Cambia el contenido segun la opcion seleccionada---*/
function showActiveContainer(active_container, no1, no2, no3, no4, no5) {
    $(active_container).show();
    $(no1).hide();
    $(no2).hide();
    $(no3).hide();
    $(no4).hide();
    $(no5).hide();
}

/*----Muestra la fecha en la pagina----*/
function showDate() {
    nuevaFecha = new Date();
    y = nuevaFecha.getFullYear();
    m = nuevaFecha.getMonth() + 1;
    d = nuevaFecha.getDate();
    document.getElementById("fecha").innerHTML = m + "/" + d + "/" + y;
}

/*----agrega animaciones al hacer click en los cuadros----*/
function animarCuadro(cuadro_id) {
    $(cuadro_id).animate({left: '400px'});
    $(cuadro_id).animate({left: '0px'});
}

/*----Ajusta la altura maximo de la tabla ventas dependiendo de la pantalla----*/
function ajustarAlturaVentas() {
    var altura_container = parseInt($("#container-2").height());
    var altura_calculos = parseInt($("#calculos").height());
    var altura_buscar_venta = parseInt($("#buscar-venta").height());
    var altura_maxima = altura_container - altura_buscar_venta - altura_calculos;

    var $ventas_actuales = $("#ventas_actuales");
    $ventas_actuales.css({"max-height": altura_maxima + "px"});
    $ventas_actuales.css({"height": altura_maxima + "px"});

}

/*----Ajusta la altura maximo del espacio para articulos dependiendo de la pantalla----*/
function ajustarAlturaArticulos() {
    var left_container_height = parseInt($("#left-container").height());
    var $articulos_encontrados = $("#articulos-encontrados");
    $articulos_encontrados.css({"max-height": left_container_height - 50 + "px"});
    $articulos_encontrados.css({"height": left_container_height - 50 + "px"});
}

/*----Ajusta la altura maximo del espacio graficas dependiendo de la pantalla----*/
function ajustarAlturaGraficas() {
    var altura_container = parseInt($("#container-6").height());
    var altura_form = parseInt($("#ver-graficas").height());

    var $espacio_graficas = $("#myChart");
    $espacio_graficas.css({"max-height": altura_maxima + "px"});
    $espacio_graficas.css({"height": altura_maxima + "px"});
}

/*----Submit de formulario buscar----*/
function buscarArticulos() {
    $("#buscar-articulos").submit();

}

/*----Agrega el articulo a la tabla----*/
function agregarATabla(articulo, agregar) {
    if (agregar === true) {
        var precio = $("#" + (articulo.id).replace(/\s/g, "") + "_precio").text();
        var table = document.getElementById("tablee-ventas");
        description_cell_number = 2; //2 el numero del input en cada row
        var found_repetido = false; //variable booleana para buscar un repetido
        for (var i = 1; i < table.rows.length; i++) { //loop a traves de cada row en la tabla
            var row = table.rows[i]; //variable de cada row
            var cell_descripcion = row.cells[description_cell_number]; //variable de la celda de descripcion
            if (cell_descripcion.getElementsByTagName("input")[0].value === articulo.id) { //comprobacion si ya existe un articulo igual en form
                found_repetido = true; //repetido encontrado
                break;
            }
        }
        if (found_repetido) { //si articulo esta repetio
            cell_cantidad = parseInt(row.cells[1].getElementsByTagName("input")[0].value) + 1; //valor cantidad actual + nuevo
            cell_precio = parseInt(row.cells[3].getElementsByTagName("input")[0].value) + parseInt(precio);//valor precio + nuevo
            row.cells[1].getElementsByTagName("input")[0].value = cell_cantidad; //cambair cantidad
            row.cells[3].getElementsByTagName("input")[0].value = cell_precio; //cambair precio
        } else { //si no existe un repetido, generar nueva row de venta
            var button_id = (articulo.id).replace(/\s/g, "") + "_eliminar";
            $('#tablee-ventas').append('<tr>\n' +
                '                    <td class="ajuste-ancho-columna10"><button id="' + button_id + '" type="button" class="button-ajuste input_ajuste" onclick="agregarATabla(this, false)"><i\n' +
                '                        class="fas fa-trash"></i></button>\n' +
                '                    <td class="ajuste-ancho-columna10"><input type="text" class="input_ajuste" value="1" readonly></td>\n' +
                '                    <td class="ajuste-ancho-columna60"><input type="text" class="input_ajuste" value="' + articulo.id + '" readonly></td>\n' +
                '                    <td><input type="text" class="input_ajuste" value="' + precio + '" readonly></td>\n' +
                '                </tr>')
        }
    }
    if (agregar === false) { //si no es agregar
        $("#" + articulo.id).closest('tr').remove(); // remueve el row donde se encuentra el id dado
    }

    modificarTotalVenta();
}

/*----Modifica el total de ventas----*/
function modificarTotalVenta() {
    var table = document.getElementById("tablee-ventas");
    var cell_precio = 3; //3 el numero del input en cada row
    var total = 0;
    for (var i = 1; i < table.rows.length; i++) {
        var row = table.rows[i]; //variable de cada row
        total += parseInt(row.cells[cell_precio].getElementsByTagName("input")[0].value); //suma los valores de precios de cada row
    }
    $("#total_venta").val(total); //cambia el input de total al valor de venta actual

}

/*----Obiene el csrf_token del formulario----*/
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

/*----Funcion que muestra las graficas con los datos obtenidos----*/
function mostrarGraficas(labels_array, data_array, tipo_grafica) {
    $chartSpace = $("#charts");
    $chartSpace.empty(); //Borra canvas anteriores
    $chartSpace.html("<canvas id=\"myChart\" class=\"canvas-fix\"></canvas>"); // Agrega canvas nuevo
    var canvas = document.getElementById("myChart");
    var ctx = canvas.getContext("2d");
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.clearRect(0, 0, ctx.width, ctx.height); //Borra la grafica anterior
    var myChart = new Chart(ctx, {
        type: tipo_grafica,
        data: {
            labels: labels_array,
            datasets: [{
                data: data_array,
                label: 'Ventas',
                backgroundColor: [
                    'rgba(128,0,0,0.2)',
                    'rgba(220,20,60, 0.2)',
                    'rgba(255,0,0, 0.2)',
                    'rgba(250,128,114, 0.2)',
                    'rgba(255,140,0, 0.2)',
                    'rgba(218,165,32, 0.2)',
                    'rgba(255,255,0, 0.2)',
                    'rgba(154,205,50, 0.2)',
                    'rgba(127,255,0, 0.2)',
                    'rgba(0,100,0, 0.2)',
                    'rgba(0,250,154, 0.2)',
                    'rgba(60,179,113, 0.2)',
                    'rgba(0,128,128, 0.2)',
                    'rgba(0,255,255, 0.2)',
                    'rgba(127,255,212, 0.2)',
                    'rgba(0,191,255, 0.2)',
                    'rgba(135,206,250, 0.2)',
                    'rgba(0,0,255, 0.2)',
                    'rgba(65,105,225, 0.2)',
                    'rgba(138,43,226, 0.2)',
                    'rgba(139,0,139, 0.2)',
                    'rgba(238,130,238, 0.2)',
                    'rgba(255,20,147, 0.2)',
                    'rgba(245,222,179, 0.2)',
                    'rgba(112,128,144, 0.2)',
                    'rgba(240,255,240, 0.2)',
                    'rgba(230,230,250, 0.2)'
                ],
                borderColor: [
                    'rgba(128,0,0,1)',
                    'rgba(220,20,60, 1)',
                    'rgba(255,0,0, 1)',
                    'rgba(250,128,114, 1)',
                    'rgba(255,140,0, 1)',
                    'rgba(218,165,32, 1)',
                    'rgba(255,255,0, 1)',
                    'rgba(154,205,50, 1)',
                    'rgba(127,255,0, 1)',
                    'rgba(0,100,0, 1)',
                    'rgba(0,250,154, 1)',
                    'rgba(60,179,113, 1)',
                    'rgba(0,128,128, 1)',
                    'rgba(0,255,255, 1)',
                    'rgba(127,255,212, 1)',
                    'rgba(0,191,255, 1)',
                    'rgba(135,206,250, 1)',
                    'rgba(0,0,255, 1)',
                    'rgba(65,105,225, 1)',
                    'rgba(138,43,226, 1)',
                    'rgba(139,0,139, 1)',
                    'rgba(238,130,238, 1)',
                    'rgba(255,20,147, 1)',
                    'rgba(245,222,179, 1)',
                    'rgba(112,128,144, 1)',
                    'rgba(240,255,240, 1)',
                    'rgba(230,230,250, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}

/*----Cambia el valor del select dia----*/
function alterarDiaSelect(dia) {
    $("#diaIncentivo").val(dia).change();
}

/*----Cambia el valor del select dia----*/
function alterarTecnicoSelect(tecnico) {
    $("#nombre-tecnico").val(tecnico).change();
}

/*----Selecciona la fila del articulo a modificar---*/
function seleccionarFilaArticulo(articulo) {

    $("#modificar-comisiones").show(); //Muestra el div para modificar articulo
    var table = document.getElementById("tablee-mostrar-articulos");
    for (var i = 1; i < table.rows.length; i++) {
        table.rows[i].style.backgroundColor = 'rgb(245,245,246)';
    }
    var $row = $("#modificar-" + articulo);
    $row.css({'background-color': '#c7ecee'}); //Cambia el color del row seleccionado
    //Agrega los valores al formulario de modificar
    $("#modificar-articulo").val($row.children('td:eq(0)').text());
    $("#modificar-precio").val($row.children('td:eq(1)').text());
    $("#modificar-costo").val($row.children('td:eq(2)').text());
    $("#modificar-comision").val($row.children('td:eq(3)').text());
    $("#modificar-objetivo").val($row.children('td:eq(4)').text());


}

/*----Mostrar los detalles de paga al empleado---*/
function mostrarDetallesEmpleado(mostrar, empleado) {
/*
    if (mostrar) {
        $.ajax({
            url: ,
            type: get,
            data: ,
            dataType: 'json',
            success: function (respuesta) {
                console.log(respuesta);
                $("#row-empleados").html(respuesta['html_codigo'])
            },
            error: function (error_respuesta) {
                console.log(error_respuesta)
            }
        });
        $("#detalles-empleado").show();
    } else {
        $("#detalles-empleado").hide();
    }
    */
}

function buscarEmpleado(){
    $("#buscar-empleados").submit();
}
/*----Crea al input como un datepicker----*/
$(document).ready(function () {
    $("#datepicker").datepicker();
    $("#datepicker1").datepicker();
    $("#datepicker2").datepicker();
    ajustarAlturaVentas();
    ajustarAlturaArticulos();
});

/*----Ajustes de DatePicker JQuery----*/
jQuery(function ($) {
    $.datepicker.regional['es'] = {
        closeText: 'Cerrar',
        prevText: '&#x3c;Ant',
        nextText: 'Sig&#x3e;',
        currentText: 'Hoy',
        monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        monthNamesShort: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun',
            'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
        dayNames: ['Domingo', 'Lunes', 'Martes', 'Mi&eacute;rcoles', 'Jueves', 'Viernes', 'S&aacute;bado'],
        dayNamesShort: ['Dom', 'Lun', 'Mar', 'Mi&eacute;', 'Juv', 'Vie', 'S&aacute;b'],
        dayNamesMin: ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'S&aacute;'],
        weekHeader: 'Sm',
        dateFormat: 'yy-mm-dd',
        firstDay: 1,
        isRTL: false,
        showMonthAfterYear: false,
        yearSuffix: ''
    };
    $.datepicker.setDefaults($.datepicker.regional['es']);
});

/*----Ejecucion de las funciones principales una vez cargado el documento----*/
$(document).ready(function () {
    showDate();
    celularNav();
    showActiveContainer("#container-3", "#container-1", "#container-5", "#container-6", "#container-2", "#container-4");
    newContainerPrincipalSize();
    ajustarAlturaVentas();

    /*----Oculta el div para modificar articulos----*/
    $("#modificar-comisiones").hide();
    $("#detalles-empleado").hide();

    /*----Ejecucion de funciones al hacer resize de pantalla---*/
    $(window).resize(function () {
        newContainerPrincipalSize();
        ajustarAlturaVentas();
        ajustarAlturaArticulos();

    });
});

/*----Peticiones con Ajax----*/
$(document).ready(function () {
    /*----Busqueda de ventas en la base de datos sin refresh----*/
    $("#buscar-venta").submit(function (e) {
        e.preventDefault();

        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),
            dataType: 'json',
            success: function (respuesta) {
                console.log(respuesta);
                $("#ventas_actuales").html(respuesta['html_codigo']);
                $("#precio_show").val(respuesta['suma_precio']);
                $("#costo_show").val(respuesta['suma_costo']);
                $("#total_show").val(respuesta['total']);
            },
            error: function (error_respuesta) {
                console.log(error_respuesta)
            }
        })
    });

    /*----Busqueda articulos en la base de datos sin refresh----*/
    $("#buscar-articulos").submit(function (e) {
        e.preventDefault();

        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),
            dataType: 'html',
            success: function (respuesta) {
                console.log(respuesta);
                $("#articulos-encontrados").html(respuesta)
            },
            error: function (error_respuesta) {
                console.log(error_respuesta)
            }
        })
    });

    /*----Registro en la base de datos sin refresh----*/
    $("#registrar-venta").submit(function (e) {
        e.preventDefault();
        var ventas = [];

        var table = document.getElementById("tablee-ventas");
        for (var i = 1; i < table.rows.length; i++) {
            var row = table.rows[i];
            //your code goes here, looping over every row.
            var renglon_venta = {
                'cantidad': row.cells[1].getElementsByTagName("input")[0].value,
                'descripcion': row.cells[2].getElementsByTagName("input")[0].value,
                'precio': row.cells[3].getElementsByTagName("input")[0].value
            };
            ventas.push(renglon_venta);
            //alert(renglon_venta.cantidad + " " + renglon_venta.descripcion + " a $" + renglon_venta.precio);

        }

        var csrftoken = getCookie('csrftoken');
        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: {
                'csrfmiddlewaretoken': csrftoken,
                'ventas': JSON.stringify(ventas),
                'metodo_de_pago': $("#metodo_de_pago").val()
            },
            dataType: 'html',
            success: function (respuesta) {
                console.log(respuesta);
                if (respuesta === "Success") {
                    alert("Venta registrada exitosamente!");
                    $tabla_ventas = $("#tablee-ventas");
                    $tabla_ventas.empty();
                    $tabla_ventas.append('<tr>' +
                        '<th style="background: rgba(217,0,9,0.2)">X</th>' +
                        '<th style="background: rgba(51,217,178,0.20)">#</th>' +
                        '<th style="background: rgba(51,217,178,0.20)">Descripcion</th>' +
                        '<th style="background: rgba(51,217,178,0.20)">Precio</th>' +
                        '</tr>');
                } else {
                    alert("Error al registrar venta por las siguientes razones: \n" + respuesta);
                }
            },
            error: function (error_respuesta) {
                console.log(error_respuesta)
            }
        })
    });

    /*----Muestra las graficas----*/
    $("#ver-graficas").submit(function (e) {
        e.preventDefault();

        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),
            dataType: 'json',
            success: function (respuesta) {
                console.log(respuesta);
                mostrarGraficas(respuesta['labels'], respuesta['data'], respuesta['tipo_grafica'])
            },
            error: function (error_respuesta) {
                console.log(error_respuesta)
            }
        })
    });

    /*----Obtiene los datos de la operacion a realizar----*/
    $("#operacion-realizar").submit(function (e) {
        e.preventDefault();

        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),
            dataType: 'json',
            success: function (respuesta) {
                console.log(respuesta);
                if (respuesta['operacion'] === "incentivos") { //Muestra los datos dependiendo del tipo de operacin
                    $("#modificar-valores-incentivos").show();
                    $("#modificar-valores-hora").hide();
                    $("#modificar-comisiones").hide();

                } else if (respuesta['operacion'] === "hora_llegada") {
                    $("#modificar-valores-hora").show();
                    $("#modificar-valores-incentivos").hide();
                    $("#modificar-comisiones").hide();

                } else if (respuesta['operacion'] === "comisiones") {
                    $("#modificar-valores-hora").hide();
                    $("#modificar-valores-incentivos").hide();
                    $("#modificar-comisiones").hide();

                }
                $("#datos_modificar").html(respuesta['html_codigo'])
            },
            error: function (error_respuesta) {
                console.log(error_respuesta)
            }
        })
    });

    /*----Actualiza los incentivos----*/
    $("#modificar-valores-incentivos").submit(function (e) {
        e.preventDefault();

        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),
            dataType: 'html',
            success: function (respuesta) {
                console.log(respuesta);
                if (respuesta === "Success") {
                    alert("Cambios registrados exitosamente!");

                } else {
                    alert("No ha sido posible registrar los cambios" + respuesta);
                }
            },
            error: function (error_respuesta) {
                console.log(error_respuesta)
            }
        })
    });

    /*----Actualiza las horas de entrada----*/
    $("#modificar-valores-hora").submit(function (e) {
        e.preventDefault();

        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),
            dataType: 'html',
            success: function (respuesta) {
                console.log(respuesta);
                if (respuesta === "Success") {
                    alert("Cambios registrados exitosamente!");
                } else {
                    alert("No ha sido posible registrar los cambios" + respuesta);
                }
            },
            error: function (error_respuesta) {
                console.log(error_respuesta);
            }
        })
    });

    /*----Actualiza los articulos----*/
    $("#modificar-comisiones").submit(function (e) {
        e.preventDefault();

        var $articulo = $("#modificar-articulo");
        var $precio = $("#modificar-precio");
        var $costo = $("#modificar-costo");
        var $comision = $("#modificar-comision");
        var $objetivo = $("#modificar-objetivo");
        var desc = $articulo.val().replace(/\s/g, "");
        var row = $("#modificar-" + desc);

        var table = document.getElementById("tablee-mostrar-articulos");
        for (var i = 1; i < table.rows.length; i++) {
            table.rows[i].style.backgroundColor = 'rgb(245,245,246)'; //Cambia el color del row seleccionado
        }

        var articulo = {
            'descripcion': $articulo.val(),
            'precio': $precio.val(),
            'costo': $costo.val(),
            'comision': $comision.val(),
            'objetivo': $objetivo.val()
        };
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: {
                'csrfmiddlewaretoken': csrftoken,
                'articulo': JSON.stringify(articulo)
            },
            dataType: 'html',
            success: function (respuesta) {
                console.log(respuesta);
                if (respuesta === "Success") {
                    alert("Cambios registrados exitosamente!");
                    //Limpia los inputs de modificar articulo
                    $articulo.val('');
                    $precio.val('');
                    $costo.val('');
                    $comision.val('');
                    $objetivo.val('');
                    $("#elemento-modificar").hide(); //Esconde el div para modificar articulo
                } else {
                    alert("No ha sido posible registrar los cambios" + respuesta);
                }
            },
            error: function (error_respuesta) {
                console.log(error_respuesta)
            }
        })

    });

    /*----Busca a los empleados----*/
    $("#buscar-empleados").submit(function (e) {
        e.preventDefault();

        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),
            dataType: 'json',
            success: function (respuesta) {
                console.log(respuesta);
                $("#row-empleados").html(respuesta['html_codigo'])
            },
            error: function (error_respuesta) {
                console.log(error_respuesta)
            }
        })
    });
});
