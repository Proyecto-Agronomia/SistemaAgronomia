from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required


app_name='proyeccionsocial'

urlpatterns=[
	#URL para el menu de inicio
	#path('', index),
	path('proyeccionsocial/index/<username>/',login_required(index), name='index'),


	#URL para Ciclo
	path('proyeccionsocial/consultaCiclo/',login_required(consultaCiclo), name="consulta_ciclo"),
	path('proyeccionsocial/crearCiclo/',login_required(crearCiclo.as_view()), name="crear_ciclo"),
	path('proyeccionsocial/editarCiclo/<pk>/',login_required(editarCiclo.as_view()), name="editar_ciclo"),
	path('proyeccionsocial/eliminarCiclo/<pk>/',login_required(eliminarCiclo.as_view()), name="eliminar_ciclo"),


	#URL para Estudiante
	path('proyeccionsocial/consultaEstudiante/<username>/',login_required(consultaEstudiante), name="consulta_estudiante"),
	#path('proyeccionsocial/crearEstudiante/<username>/',login_required(crearEstudiante.as_view()), name="crear_estudiante"),
	path('proyeccionsocial/crearEstudiante/<username>/',login_required(crearEstudiante), name="crear_estudiante"),
	path('proyeccionsocial/editarEstudiante/<pk>/',login_required(editarEstudiante.as_view()), name="editar_estudiante"),
	path('proyeccionsocial/eliminarEstudiante/<pk>/',login_required(eliminarEstudiante.as_view()), name="eliminar_estudiante"),
	#Buscar Estudiante
	path('proyeccionsocial/consultaEstudianteBuscar/',login_required(consultaEstudianteBuscar), name="consulta_estudiante_buscar"),


	#URL para Crear Entidad Externa
	path('proyeccionsocial/crearEntidadExterna/<username>/',login_required(crearEntidadExterna.as_view()), name="crear_entidad_externa"),


	#URL para Estudio Universitario
	path('proyeccionsocial/consultaEstudioUniversitario/<username>/',login_required(consultaEstudioUniversitario), name="consulta_estudio_universitario"),
	#path('proyeccionsocial/crearEstudioUniversitario/<username>/',login_required(crearEstudioUniversitario.as_view()), name="crear_estudio_universitario"),
	path('proyeccionsocial/crearEstudioUniversitario/<username>/',login_required(crearEstudioUniversitario), name="crear_estudio_universitario"),
	path('proyeccionsocial/editarEstudioUniversitario/<pk>/',login_required(editarEstudioUniversitario.as_view()), name="editar_estudio_universitario"),
	path('proyeccionsocial/eliminarEstudioUniversitario/<pk>/',login_required(eliminarEstudioUniversitario.as_view()), name="eliminar_estudio_universitario"),
	#Buscar Estudio Universitario
	path('proyeccionsocial/consultaEstudioUniversitarioBuscar/',login_required(consultaEstudioUniversitarioBuscar), name="consulta_estudio_universitario_buscar"),


	#URL para la Solicitud de Servicio Social
	path('proyeccionsocial/consultaSolicitudServicioSocial/<username>/',login_required(consultaSolicitudServicioSocial), name="consulta_solicitud_servicio_social"),
	#path('proyeccionsocial/crearSolicitudServicioSocial/<username>/',login_required(crearSolicitudServicioSocial.as_view()), name="crear_solicitud_servicio_social"),
	path('proyeccionsocial/crearSolicitudServicioSocial/<username>/',login_required(crearSolicitudServicioSocial), name="crear_solicitud_servicio_social"),
	path('proyeccionsocial/editarSolicitudServicioSocial/<pk>/',login_required(editarSolicitudServicioSocial.as_view()), name="editar_solicitud_servicio_social"),
	path('proyeccionsocial/eliminarSolicitudServicioSocial/<pk>/',login_required(eliminarSolicitudServicioSocial.as_view()), name="eliminar_solicitud_servicio_social"),
	#Buscar Solicitud Servicio Social
	path('proyeccionsocial/consultaSolicitudServicioSocialBuscar/',login_required(consultaSolicitudServicioSocialBuscar), name="consulta_solicitud_servicio_social_buscar"),
	# Para el boton Solicitudes del Base para Administrador
	path('proyeccionsocial/editarSolicitudServicioSocial2/<pk>/',login_required(editarSolicitudServicioSocial2.as_view()), name="editar_solicitud_servicio_social2"),
	path('proyeccionsocial/eliminarSolicitudServicioSocial2/<pk>/',login_required(eliminarSolicitudServicioSocial2.as_view()), name="eliminar_solicitud_servicio_social2"),


	#URL para el Estado de la Solicitud de Servicio Social
	path('proyeccionsocial/consultaEstadoSolicitudServicioSocial/<username>/',login_required(consultaEstadoSolicitudServicioSocial), name="consulta_estado_solicitud_servicio_social"),
	path('proyeccionsocial/crearEstadoSolicitudServicioSocial/<username>/<pk>',login_required(crearEstadoSolicitudServicioSocial.as_view()), name="crear_estado_solicitud_servicio_social"),
	path('proyeccionsocial/editarEstadoSolicitudServicioSocial/<pk>/',login_required(editarEstadoSolicitudServicioSocial.as_view()), name="editar_estado_solicitud_servicio_social_consulta"),
	path('proyeccionsocial/eliminarEstadoSolicitudServicioSocial/<pk>/',login_required(eliminarEstadoSolicitudServicioSocial.as_view()), name="eliminar_estado_solicitud_servicio_social"),
	# Para el boton Solicitudes del Base para Administrador
	path('proyeccionsocial/consultaEstadoSolicitudServicioSocialConsulta/<username>/',login_required(consultaEstadoSolicitudServicioSocialConsulta), name="consulta_estado_solicitud_servicio_social_consulta"),
	path('proyeccionsocial/crearEstadoSolicitudServicioSocial2/<username>/<pk>',login_required(crearEstadoSolicitudServicioSocial2.as_view()), name="crear_estado_solicitud_servicio_social2"),
	path('proyeccionsocial/consultaEstadoSolicitudServicioSocialBuscar/',login_required(consultaEstadoSolicitudServicioSocialBuscar), name="consulta_estado_solicitud_servicio_social_buscar"),
	path('proyeccionsocial/consultaEstadoSolicitudServicioSocialBuscar2/',login_required(consultaEstadoSolicitudServicioSocialBuscar2), name="consulta_estado_solicitud_servicio_social_buscar2"),
	
	
	#URL para Carrera
	path('proyeccionsocial/consultaCarrera/',login_required(consultaCarrera), name="consulta_carrera"),
	path('proyeccionsocial/crearCarrera/',login_required(crearCarrera.as_view()), name="crear_carrera"),
	path('proyeccionsocial/editarCarrera/<pk>/',login_required(editarCarrera.as_view()), name="editar_carrera"),
	path('proyeccionsocial/eliminarCarrera/<pk>/',login_required(eliminarCarrera.as_view()), name="eliminar_carrera"),
	

	#URL para ServicioSocial
	path('proyeccionsocial/consultaServicioSocial/<username>/',login_required(consultaServicioSocial), name="consulta_servicio_social"),
	path('proyeccionsocial/crearServicioSocial/<username>/',login_required(crearServicioSocial.as_view()), name="crear_servicio_social"),
	path('proyeccionsocial/crearServicioSocialAdmin/<username>/',login_required(crearServicioSocialAdmin.as_view()), name="crear_servicio_social_admin"),
	path('proyeccionsocial/editarServicioSocial/<pk>/',login_required(editarServicioSocial.as_view()), name="editar_servicio_social"),
	path('proyeccionsocial/eliminarServicioSocial/<pk>/',login_required(eliminarServicioSocial.as_view()), name="eliminar_servicio_social"),
	path('proyeccionsocial/consultaServicioSocialBuscar/',login_required(consultaServicioSocialBuscar), name="consulta_servicio_social_buscar"),
    

    #URL para AsesorExterno
    path('proyeccionsocial/consultaAsesorExterno/',login_required(consultaAsesorExterno), name="consulta_asesor_externo"),
    path('proyeccionsocial/crearAsesorExterno/',login_required(crearAsesorExterno.as_view()), name="crear_asesor_externo"),
	path('proyeccionsocial/crearAsesorExternoEstd/<username>/',login_required(crearAsesorExternoEstudiante.as_view()), name="crear_asesor_externo_estudiante"),
    path('proyeccionsocial/editarAsesorExterno/<pk>/',login_required(editarAsesorExterno.as_view()), name="editar_asesor_externo"),
    path('proyeccionsocial/eliminarAsesorExterno/<pk>/',login_required(eliminarAsesorExterno.as_view()), name="eliminar_asesor_externo"),
    

    #URL para AsesorInterno
    path('proyeccionsocial/consultaAsesorInterno/',login_required(consultaAsesorInterno), name="consulta_asesor_interno"),
    path('proyeccionsocial/crearAsesorInterno/',login_required(crearAsesorInterno.as_view()), name="crear_asesor_interno"),
    path('proyeccionsocial/editarAsesorInterno/<pk>/',login_required(editarAsesorInterno.as_view()), name="editar_asesor_interno"),
    path('proyeccionsocial/eliminarAsesorInterno/<pk>/',login_required(eliminarAsesorInterno.as_view()), name="eliminar_asesor_interno"),


    #URL para Documentos
	path('proyeccionsocial/listarDocumentos/<pk>/', login_required(documentosEstudianteListView.as_view()), name="listar_documentos"),
	path('proyeccionsocial/agregarDocumentos/<pk>/', login_required(agregarDocumentos.as_view()), name="agregar_documentos"),
	path('proyeccionsocial/eliminarDocumento/<pk>/', login_required(eliminarDocumento.as_view()), name="eliminar_documento"),
	

	#URL para Horas Sociales
	path('proyeccionsocial/listarHorasSociales/<pk>/', login_required(horasSocialesListView.as_view()), name="listar_horas_sociales"),
	path('proyeccionsocial/agregarHorasSociales/<pk>/', login_required(agregarHorasSociales.as_view()), name="agregar_horas_sociales"),
	path('proyeccionsocial/editarHorasSociales/<pk>/', login_required(editarHorasSociales.as_view()), name="editar_horas_sociales"),	
	path('proyeccionsocial/eliminarHorasSociales/<pk>/', login_required(eliminarHorasSociales.as_view()), name="eliminar_horas_sociales"),
	

	#URL para Proyecto
	path('proyeccionsocial/consultaProyecto/',login_required(consultaProyecto), name="consulta_proyecto"),
	path('proyeccionsocial/crearProyecto/',login_required(crearProyecto.as_view()), name="crear_proyecto"),
	path('proyeccionsocial/editarProyecto/<pk>/',login_required(editarProyecto.as_view()), name="editar_proyecto"),
	path('proyeccionsocial/eliminarProyecto/<pk>/',login_required(eliminarProyecto.as_view()), name="eliminar_proyecto"),
	#Buscar Proyecto
	path('proyeccionsocial/consultaProyectoBuscar/',login_required(consultaProyectoBuscar), name="consulta_proyecto_buscar"),


	# URL para Actividad
	path('proyeccionsocial/consultaActividad/<username>/',login_required(consultaActividad), name="consulta_actividad"),
	path('proyeccionsocial/crearActividad/<username>',login_required(crearActividad.as_view()), name="crear_actividad"),
	path('proyeccionsocial/crearActividadAdmin/<username>',login_required(crearActividadAdmin.as_view()), name="crear_actividad_admin"),
	path('proyeccionsocial/editarActividad/<pk>/',login_required(editarActividad.as_view()), name="editar_actividad"),
	path('proyeccionsocial/eliminarActividad/<pk>/',login_required(eliminarActividad.as_view()), name="eliminar_actividad"),


	#URL para los Formularios
	path('proyeccionsocial/generarF1/<str:carnet_estudiante>/',login_required(generarF1.as_view()), name= "generar_F1"),
	path('proyeccionsocial/generarF2/<str:carnet_estudiante>/',login_required(generarF2.as_view()), name= "generar_F2"),
	path('proyeccionsocial/generarF3/<str:carnet_estudiante>/',login_required(generarF3.as_view()), name= "generar_F3"),
	path('proyeccionsocial/generarF4TI/<str:carnet_estudiante>/',login_required(generarF4TI.as_view()), name= "generar_F4TI"),
	path('proyeccionsocial/generarF4TE/<str:carnet_estudiante>/',login_required(generarF4TE.as_view()), name= "generar_F4TE"),
	path('proyeccionsocial/generarF6/<str:carnet_estudiante>/',login_required(generarF6.as_view()), name= "generar_F6"),
	path('proyeccionsocial/generarF7/<str:carnet_estudiante>/',login_required(generarF7.as_view()), name= "generar_F7"),
	path('proyeccionsocial/generarF8/<str:carnet_estudiante>/',login_required(generarF8.as_view()), name= "generar_F8"),
	path('proyeccionsocial/generarF9/<str:carnet_estudiante>/',login_required(generarF9.as_view()), name= "generar_F9"),
	path('proyeccionsocial/generarF11/<str:carnet_estudiante>/',login_required(generarF11.as_view()), name= "generar_F11"),
]