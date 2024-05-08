from flask import Flask, jsonify

app = Flask(__name__)

# Datos de ejemplo de las carreras de la universidad
carreras = {
    1: {"nombre": "Ingeniería Industrial","especialidades":{"Ingeniería en Manufactura y Calidad":
                                                            ["QUIMICA","TALLER DE ETICA","CALCULO DIFERENCIAL","TALLER DE HERRAMIENTAS INTELECTUALES","FUNDAMENTOS DE INVESTIGACIÓN","DIBUJO INDUSTRIAL","ACTIVIDADES COMPLEMENTARIAS",
                                                             "METODOLOGIA Y NORMALIZACION","ELECTRICIDAD Y ELECTRONICA INDUSTRIAL","CALCULO INTEGRAL","FISICA","PROBABILIDAD Y ESTADISCTICA","ANALISIS DE LA REALIDAD NACIONAL","TALLER DE LIDERAZGO",
                                                             "PROPIEDAD DE LOS MATERIALES","ECONOMIA","CALCULO VECTORIAL","ALGEBRA LINEAL", "ESTADISTICA INFERENCIAL 1","ESTUDIO DEL TRABAJO 1","ADMINISTRACION DE PROYECTOS",
                                                             "PROCESOS DE FABRICACION","ALGORITMOS Y LENGUAJES DE PROGRAMACION","ADMINISTRACION DE OPERACIONES","INVESTIGACION DE OPERACIONES 1","ESTADISTICA INFERENCIAL 2","ESTUDIO DEL TRABAJO 2","HIGIENE Y SEGURIDAD INDUSTRIAL",
                                                             "GESTION DE COSTOS","MERCADOTECNIA","ADMINISTRACION DE OPERACIONES 2","CONTROL ESTADISTICO DE LA CALIDAD","ECONOMIA","DESARROLLO SUSTENTABLE",
                                                             "INGENIERIA ECONOMICA","TALLER DE INVESTIGACION 1","INGENIERIA DE SISTEMAS","SIMULACION","ADMINISTRACIÓN DEL MANTENIMIENTO","SISTEMAS NEUMATICOS E HIDRAULICOS","DISEÑO ASISTIDO POR COMPUTADORA",
                                                             "PLANEACION FINANCIERA","RELACIONES INDUSTRIALES","PLANEACIÓN Y DISEÑO DE INSTALACIONES","SISTEMA DE MANUFACTURA","LOGISTICA Y CADENA DE SUMINISTRO","GESTION DE LOS SISTEMAS","CONTROLADORES LOGICOS PROGRAMANLES",
                                                             "FORMULACION Y EVALUACION DE PROYECTOS","TEMAS SELECTOS DE MANUFACTURA","CORETOOL","MEDICIÓN Y MEJORAMIENTO DE LA PRODUCTIVIDAD","ROBOTICA INDUSTRIAL","SERVICIO SOCIAL",
                                                             "TALLER DE INVESTIGACION 2","RESIDENCIA PROFESIONAL","MANUFACURA FLEXIBLE"],
                                                            "Manufactura en Articulos de Piel":
                                                            ["QUIMICA","TALLER DE ETICA","CALCULO DIFERENCIAL","TALLER DE HERRAMIENTAS INTELECTUALES","FUNDAMENTOS DE INVESTIGACIÓN","DIBUJO INDUSTRIAL","ACTIVIDADES COMPLEMENTARIAS",
                                                             "METODOLOGIA Y NORMALIZACION","ELECTRICIDAD Y ELECTRONICA INDUSTRIAL","CALCULO INTEGRAL","FISICA","PROBABILIDAD Y ESTADISCTICA","ANALISIS DE LA REALIDAD NACIONAL","TALLER DE LIDERAZGO",
                                                             "PROPIEDAD DE LOS MATERIALES","ECONOMIA","CALCULO VECTORIAL","ALGEBRA LINEAL", "ESTADISTICA INFERENCIAL 1","ESTUDIO DEL TRABAJO 1","ADMINISTRACION DE PROYECTOS",
                                                             "PROCESOS DE FABRICACION","ALGORITMOS Y LENGUAJES DE PROGRAMACION","ADMINISTRACION DE OPERACIONES","INVESTIGACION DE OPERACIONES 1","ESTADISTICA INFERENCIAL 2","ESTUDIO DEL TRABAJO 2","HIGIENE Y SEGURIDAD INDUSTRIAL",
                                                             "GESTION DE COSTOS","MERCADOTECNIA","ADMINISTRACION DE OPERACIONES 2","CONTROL ESTADISTICO DE LA CALIDAD","ECONOMIA","DESARROLLO SUSTENTABLE",
                                                             "INGENIERIA ECONOMICA","TALLER DE INVESTIGACION 1","INGENIERIA DE SISTEMAS","SIMULACION","ADMINISTRACIÓN DEL MANTENIMIENTO","DISEÑO Y MODELADO","DISEÑO ASISTIDO POR COMPUTADORA",
                                                             "PLANEACION FINANCIERA","RELACIONES INDUSTRIALES","PLANEACIÓN Y DISEÑO DE INSTALACIONES","SISTEMA DE MANUFACTURA","LOGISTICA Y CADENA DE SUMINISTRO","GESTION DE LOS SISTEMAS DE CALIDAD","TECNOLOGÍA Y TALLER",
                                                             "FORMULACION Y EVALUACION DE PROYECTOS","TEMAS SELECTOS DE MANUFACTURA","CORETOOL","MEDICIÓN Y MEJORAMIENTO DE LA PRODUCTIVIDAD","TECNOLOGÍA Y TALLER 2","SERVICIO SOCIAL",
                                                             "TALLER DE INVESTIGACION 2","RESIDENCIA PROFESIONAL","ADMINISTRACION DE LOS SISTEMAS DE PRODUCCION DE CALZADO",

                                                            ]
                                                             }},
    2: {"nombre": "Ingeniería en Sistemas Computacionales","especialidades":{"Computo Empresarial":
                                                                             ["CALCULO DIFERENCIAL","MATEMATICAS DISCRETAS","FUNDAMENTOS DE PROGRAMACION","TALLER DE ADMINISTRACION","FUNDAMENTOS DE INVESTIGACION","TALLER DE ETICA",
                                                                              "CALCULO INTEGRAL","ALGEBRA LINEAL","PROGRAMACION ORIENTADA AOBJETOS","CONTABILIDAD FINANCIERA","QUIMICA","PROBABILIDAD Y ESTADISTICA",
                                                                              "CALCULO VECTORIAS","INVESTIGACION DE OPERACIONES","ESTRUCTURA DE DATOS","CULTURA EMPRESARIAL","DESARROLLO SUSTENTABLE","FISICA GENERAL",
                                                                              "ECUACIONES DIFERENCIALES","FUNDAMENTOS DE BASES DE DATOS","TOPICOS AVANZADOS DE PROGRAMACION","METODOS NUMERICOS","FUNDAMENTOS DE TELECOMUNICACIONES","PRINCIPIOS ELECTRICOS Y APLICACIONES DIGITALTES",
                                                                              "FUNDAMENTOS DE INGENIERIA DE SOFTWARE","TALLER DE BASES DE DATOS","INTELIGENCIA ARTIFICIAL","SISTEMAS OPERATIVOS","REDES DE COMPUTADORAS","ARQUITECTURA DE COMPUTADORAS","ACTIVIDADES COMPLEMENTARIOS",
                                                                              "INGENIERIA DE SOFTWARE","ADMINISTRACION DE BASES DE DATOS","LENGUAJES Y AUTOMATAS 1","TALLER DE SISTEMAS OPERATIVOS","CONMUTACION Y ENRUTAMIENTO DE REDES DE DATOS","LENGUAJES DE INTERFAZ",
                                                                              "GESTION DE PROYECTOS DE SOFTWARE","TOPICOS PARA EL DESPLIEGUE DE APLICACIONES","LENGUAJES Y AUTOMATAS 2","PROGRAMACION WEB","GRAFICACION","SISTEMAS PROGRAMABLES","SERVICIO SOCIAL",
                                                                              "INTELIGENCIA DE NEGOCIOS 1","SERVICIOS EN LA NUBE","DESARROLLO DE APLICACIONES MOVILES","TALLER DE INVESTIGACION 1","PROGRAMACION LOGICA Y FUNCIONAL","ADMINISTRACION DE REDES",
                                                                              "INTELIGENCIA DE NEGOCIOS 2","PROYECTO INTEGRADOR PARA APLICACIONES EMPRESARIALES","TALLER DE INVESTIGACION 2","SIMULACION","RESIDENCIA","",]}},
    3: {"nombre": "Ingeniería en Tecnologías de de la Información y comunicaciones","especialidades": {"Gestion de Servicios de TI en Ambientes Empresariales":
                                                                                                       ["CALCULO DIFERENCIAL", "FUNDAMENTOS DE PROGRAMACION", "MATEMATICAS DISCRETAS 1", "INTRODUCCION A LAS TIC'S","TALLER DE ETICA","FUNDAMENTOS DE INVESTIGACION",
                                                                                                        "CALCULO INTEGRAL","PROGRAMACION ORIENTADA A OBJETOS","MATEMATICAS DISCRETAS 2","PROBABILIDAD Y ESTADISTICA","CONTABILIDAD Y COSTOS","ADMINISTRACION GERENCIAL",
                                                                                                        "MATEMATICAS APLICADAS A COMUNICACIONES","ESTRUCTURA Y ORGANIZACION DE DATOS","ALGEBRA LINEAL","FUNDAMENTOS DE BASES DATOS","ELECTRICIDAD Y MAGNETISMO","DESARROLLO SUSTENTABLE",
                                                                                                        "ANALISIS DE SEÑALES Y SISTEMAS DE COMUNICACION","PROGRAMACION","MATEMATICAS PARA LA TOMA DE DECISIONES","TALLER DE BASE DE DATOS","CIRCUITOS ELECTRICOS Y ELECTRONICOS","INGENIERIA DE SOFTWARE",
                                                                                                        "FUNDAMENTOS DE REDES","TELECOMUNICACIONES","ADMINISTRACION DE PROYECTOS","BASE DE DATOS DISTRIBUIDAS","ARQUITECTURA DE COMPUTADORAS","TALLER DE INGENIERIA DE SOFTWARE",
                                                                                                        "REDES DE COMPUTADORA","TECNOLOGIAS INALAMBRICAS","DESARROLLO DE EMPRENDEDORES","TALLER DE INVESTIGACION 1","SISTEMAS OPERATIVOS 1","PROGRAMACION WEB","ACTIVIDADES COMPLEMENTARIAS",
                                                                                                        "REDES EMERGENTES","DESARROLLO DE APLICACIONES PARA DISPOSITIVOS MOVILES","INGENIERIA DEL CONOCIMIENTO","TALLER DE INVESTIGACION 2","SISTEMAS OPERATIVOS 2","NEGOCIOS ELECTRONICOS 1",
                                                                                                        "ADMINISTRACION Y SEGURIDAD DE REDES","SEGURIDAD INFORMATICA","ADMINISTRACION DE SERVIDORES","INTERACCION HUMANO COMPUTADORA","AUDITORIA EN TECNOLOGIAS DE LA INFORMACION","NEGOCIOS ELECTRONICOS 2","SERVICIO SOCIAL",
                                                                                                        "GESTION DE SISTEMAS vOip","ESTRATEGIAS DE GESTION DE SERV. DE TI ","VIRTUALIZACION & IoT","RESIDENCIAS"
                                                                                                        ]}},
    4: {"nombre": "Ingeniería en Gestión Empresarial","especialidades":{"Ingenieria En Gestion Empresarial":
                                                                        ["FUNDAMENTOS DE INVESTIGACION","CLACULO DIFERENCIAL","DESARROLLO HUMANO","FUNDAMENTOS DE GESTION EMPRESARIAL","DINAMICA SOCIAL","FUNDAMENTOS DE QUIMICA",
                                                                         "SOFTWARE DE APLICACION EJECUTIVO","CALCULO INTEGRAL","CONTABILIDAD ORIENTADA A NEGOCIOS","LEGISLACION LABORAL","TALLER DE ETICA","FUNDAMENTOS DE FISICA",
                                                                         "MARCO LEGAL DE LAS ORGANIZACIONES","PROBABILIDAD Y ESTADISTICA DESCRIPTIVA","COSTOS EMPRESARIALES","HABILIDADES DIRECTIVAS 1","ECONOMIA EMPRESARIAL","ALGEBRA LINEAL",
                                                                         "INSTRUMENTOS DE PRESUPUESTACION EMPRESARIAL","ESTADISTICA INFERENCIAL 1","INGENIERIA DE PROCESOS","HABILIDADES DIRECTIVAS 2","ENTORNO MACROECONOMICO","INVESTIGACION DE OPERACIONES",
                                                                         "FINANZAS EN LAS ORGANIZACIONES","ESTADISTICA INFERENCIAL 2","GESTION DE LA PRODUCCION 1","GESTION DEL CAPITAL HUMANO","DESARROLLO SUSTENTABLE","MERCADOTECNIA",
                                                                         "INGENIERIA ECONOMICA","EL EMPRENDEDOR Y LA INNOVACION","GESTION DE LA PRODUCCION 2","ADMINISTRACIÓN DE LA SALUD Y SEGURIDAD OCUPACIONAL","CALIDAD APLICADA A LA GESTION EMPRESARIAL","SISTEMAS DE INFORMACION DE MERCADOTECNIA","ACTIVIDADES COMPLEMENTARIAS",
                                                                         "PLAN DE NEGOCIOS","CALIDAD APLICADA A LA GESTION EMPRESARIAL 2","TALLER DE INVESTIGACION 1","DISEÑO ORGANIZACIONAL","MERCADOTECNIA ELECTRONICA","SERVICIO SOCIAL",
                                                                         "ESTRATEGIAS FIN Y COSTOS DE CALIDAD","INNOVACION DE PROCESOS","SEMINARIO DE CALIDAD","SEMINARIO DE CONSULTORIA ORG.","TALLER DE UNVESTIGACION 2","GESTION ESTRATEGICA",
                                                                         "CADENA DE SUMINISTROS","RESIDENCIA PROFESIONAL","GESTION DEL CONOCIMIENTO","SEMINARIO DE GESTION ESTRATEGICA","",""]}},
    5: {"nombre": "Ingeniería Electrónica","especialidades":{"Ingenieria Electronica":
                                                             ["CALCULO DIFERENCIAL","MECANICA CLASICA","QUIMICA","TALLER DE ETICA","FUNDAMENTOS DE INVESTIGACION","COMUNICACION HUMANA",
                                                              "CALCULO INTEGRAL","PROBABILIDAD Y ESTADISTICA","DESARROLLO SUSTENTABLE","MEDICIONES ELECTRICAS","TOPICOS SELECTOS DE FISICA","DESARROLLO HUMANO",
                                                              "CALCULO VECTORIAL","ELECTROMAGNETISMO","ALGEBRA LINEAL","FISICA DE SEMICONDUCTORES","PROGRAMACION ESTRUCTURADA",
                                                              "ECUACIONES DIFERENCIALES","CIRCUITOS ELECTRICOS 1","MARCO LEGAL DE LA EMPRESA","ANALISIS NUMERICO","DISEÑO DIGITAL","PROGRAMACION VISUAL",
                                                              "CIRCUITOS ELECTRICOS 2","DIODOS Y TRANSITORES","TEORIA ELECTROMAGNETICA","MAQUINAS ELECTRICAS","DISEÑO DIGITAL CON VHDL","DESARROLLO PROFESIONAL",
                                                              "CONTROL 1","DISEÑOS CON TRANSITORES","FUNDAMENTOS FINANCIEROS","MICROCONTROLADORES","TALLER DE INVESTIGACION 1","ACTIVIDADES COMPLEMENTARIAS",
                                                              "CONTROL 2","AMPLIFICADORES OPERACIONALES","INSTRUMENTACION","OPTOELECTRONICA","INTRODUCCION A LAS TELECOMUNICACIONES","TALLER DE INVESTIGACION 2",
                                                              "CONTROL DIGITAL","CONTROLADORES LOGICOS PROGRAMABLES","ELECTRONICA DE POTENCIA","ADMINISTRACION GENERAL",
                                                              "DESARROLLO DE EVALUACION DE PROYECTOS","RESIDENCIA PROFESIONAL","ESPECIALIDAD"]}},
    6: {"nombre": "Ingeniería Electromecánica","especialidades":{"Ingenieria Electromecanica":
                                                                 ["TALLER DE ETICA","CALCULO DIFERENCIAL","INTRODUCCION A LA PROGRAMACION","DESARROLLO SUSTENTABLE","QUIMICA","FUNDAMENTOS DE INVESTIGACION",
                                                                  "ESTATICA","CALCULO INTEGRAL","ALGEBRA LINEAL","METROLOGIA Y NORMALIZACION","TECNOLOGIA DE LOS MATERIALES","DIBUJO ELECTROMECANICO",
                                                                  "DINAMICA","CALCULO VECTORIAL","PROCESO DE MANUFACTURA","ELICTRICIDAD Y MAGNETISMO","MECANICA DE MATERIALES","PROBABILIDAD Y ESTADISTICA",
                                                                  "ANALISIS Y SINTESIS DE MECANISMOS","ECUACIONES DIFERENCIALES","TERMODINAMICA","ANALISIS DE CIRCUITOS ELECTRICOS DE CD","MECANICA DE FLUIDOS","ELECTRONICA ANALOGICA",
                                                                  "DISEÑO DE ELEMENTOS DE MAQUINAS","DISEÑO E INGENIERIA ASISTIDOS POR COMPUTADORA","TRANSFERENCIA DE CALOR","ANALISIS DE CIRCUITOS ELECTRICOS DE CA","SISTEMAS Y MAQUINARIAS DE FLUIDOS","ELECTRONICA DIGITAL",
                                                                  "MAQUIAS Y EQUIPOS TERMICOS 1","AHORRO DE ENERGIA","INSTALACIONES ELECTRICAS","MAQUINAS ELECTRICAS","ADMINISTRACIONY TECNICAS DE MANTENIMIENTO","TALLER DE INVESTIGACION 1","ACTIVIDADES COMPLEMENTARIAS,"
                                                                  "MAQUINAS Y EQUIPOS TERMICOS 2","SISTEMAS ELECTRICOS DE POTENCIA","CONTROLES ELECTRICOS","INGENIERIA DE CONTROL CLASICO","TALLER DE INVESTIGACION 2","SERVICIO SOCIAL",
                                                                  "REFRIGERACION Y AIRE ACONDICIONADO","SUBESTACIONES ELECTRICAS","SISTEMAS HIDRAULICOS Y NEUMATICOS DE POTENCIA","FORMULACION Y EVALUACION DE PROYECTOS",
                                                                  "RESIDENCIA PROFESIONAL","ESPECIALIDAD"]}},
    7: {"nombre": "Ingeniería Mecatronica","especialidades":{"Ingenieria Mecatronica":
                                                             ["QUIMICA","CALCULO DIFERENCIAL","TALLER DE ETICA","DIBUJO ASISTIDO POS COMPUTADORA","METROLOGIA Y NORMALIZACION","FUNDAMENTOS DE INVESTIGACION",
                                                              "CALCULO INTEGRAL","ALGEBRA LINEL","CIENCIAS E INGENIERIAS DE MATERIALES","PROGRAMACION BASICA","ESTADISTICA Y CONTROL DE CALIDAD","ADMINISTRACION Y CONTABILIDAD",
                                                              "CALCULO VECTORIAL","PROCESOS DE FABRICACION","ELECTROMAGNETISMO","ESTATICA","METODOS NUMERICOS","DESARROLLO SUSTENTABLE",
                                                              "ECUACIONES DIFERENCIALES","FUNDAMENTOS DE TERMODINAMICA","MECANICA DE MATERIALES","DINAMICA","ANALISIS DE CIRCUITOS ELECTRICOS",
                                                              "MAQUINAS ELECTRICAS","ELECTRONICA ANALOGICA","MECANICANISMOS","ANALISIS DE DLUIDOS","TALLER DE INVESTIGACION 1","ACTIVIDADES COMPLEMENTARIAS",
                                                              "ELECTRONICA DE POTENCIA APLICADA","INSTRUMENTACION","DISEÑO DE ELEMENTOS MECANICOS","ELECTRONICA DIIGITAL","VIBRACIONES MECANICAS","TALLER DE INVESTIGACION 2",
                                                              "DINAMICA DE SISTEMAS","MANUFACTURA AVANZADA","CIRCUITOS HIDRAULICOS Y NEUMATICOS","MANTENIMIENTO","MICROCONTROLADORES","PROGRAMMACION AVANZADA",
                                                              "CONTROL","FORMULACION Y EVALUACION DE PROYECTOS","CONTROLADORES LOGICOS PROGRAMABLES","SERVICIO SOCIAL",
                                                              "ROBOTICA","RESIDENCIA PROFESIONAL","ESPECIALIDAD"]}},
    8: {"nombre": "Ingeniería Logística","especialidades":{"Ingenieria en Logistica":
                                                           ["INTRODUCCION A LA INGENIERIA EN LOGISTICA","CALCULO DIFERENCIAL","QUIMICA","FUNDAMENTOS DE ADMINISTRACION","DIBUJO ASISTIDO POR COMPUTADORA","ECONOMIA",
                                                            "TALLER DE ETICA","CALCULO INTEGRAL","PROBABILIDAD Y ESTADISTICA","DESARROLLO HUMANO Y ORGANIZACIONAL","FUNDAMENTOS DE INVESTIGACION","CONTABILIDAD Y COSTOS",
                                                            "CADENA DE SUMINISTRO","ALGEBRA LINEAL","ESTADISTICA INFERENCIAL 1","FUNDAMENTOS DE DERECHO","MECANICA CLASICA","FINANZAS",
                                                            "COMPRAS","TIPOLOGIA DEL PRODUCTO","ESTADISTICA INFERENCIAÑ 2","ENTORNO ECONOMICO","TOPICOS DE INGENIERIA MECANICA","BASES DE DATOS",
                                                            "ALMACENES","INVENTARIOS","INVESTIGACION DE OPERACIONES 1","HIGIENE Y SEGURIDAS","PROCESOS DE FABRICACION Y MANEJO DE MATERIALES","MERCADOTECNIA",
                                                            "TRAFICO Y TRANSPORTE","CULTURA DE CALIDAD","INVESTIGACION DE OPERACIONES 2","DESARROLLO SUSTENTABLE","TALLER DE INVESTIGACION 1","EMPAQUE,ENVASE Y EMBALAJE","ACTIVIDADES EXTRAESCOLARES",
                                                            "SERVICIO AL CLIENTE","PROGRAMACION DE PROCESOS PRODUCTIVOS","MODELOS DE SIMULACION Y LOGISTICA","LEGISLACION ADUANERA","TALLER DE INVESTIGACION 2","INGENIERIA ECONOMICA",
                                                            "INNOVACION","COMERCIO INTERNACIONAL","FORMULACION Y EVALUACION DE PROYECTOS","GEOGRAFIA PARA EL TRANSPORTE","SERVICIO SOCIAL",
                                                            "RESIDENCIA PROFESIONAL","ESPECIALIDAD","GESTION DE PROYECTOS"]}},
   

    
    
     
}

@app.route('/carreras')
def get_carreras():
    return jsonify(carreras)

@app.route('/carreras/<int:id>')
def get_carrera_nombre(id):
    carrera = carreras.get(id)
    if carrera:
        return jsonify({"nombre": carrera.get("nombre")})
    else:
        return jsonify({"error": "Carrera no encontrada"}), 404


@app.route('/carreras/<int:id>/especialidades')
#def get_carrera(id):
    #carrera = carreras.get(id)
   # if carrera:
  #      return jsonify({"especialidades": carrera.get("especialidades")})
 #   else:
#        return jsonify({"error": "Carrera no encontrada"}), 404

def get_especialidades(id):
    carrera = carreras.get(id)
    if carrera:
        return jsonify({"especialidades": list(carrera.get("especialidades").keys())})
    else:
        return jsonify({"error": "Carrera no encontrada"}), 404


@app.route('/carreras/<int:id>/especialidades/<especialidad>')
def get_materias(id, especialidad):
    carrera = carreras.get(id)
    if carrera:
        especialidades = carrera.get("especialidades")
        materias = especialidades.get(especialidad)
        if materias:
            return jsonify({"materias": materias})
        else:
            return jsonify({"error": "Especialidad no encontrada"}), 404
    else:
        return jsonify({"error": "Carrera no encontrada"}), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000,debug=True)
