
import flet as ft
import os
from curriculum import CrearCurriculum, CurriculumData

def main(page: ft.Page):
    page.title = "Generador de Currículum"
    page.scroll = "auto"

    datos = CurriculumData()

    archivo_pdf = None


    # Campo para nombre del archivo PDF
    nombreArchivoPDF = ft.TextField(label="Nombre del archivo PDF (sin .pdf)")

    # Campos de entrada del CV
    nombre = ft.TextField(label="Nombre completo")
    titulo = ft.TextField(label="Título profesional")
    contacto = ft.TextField(label="Teléfono y correo")
    ubicacion = ft.TextField(label="Ubicación")
    linkedin = ft.TextField(label="LinkedIn URL")
    github = ft.TextField(label="GitHub URL")
    perfil = ft.TextField(label="Perfil Profesional", multiline=True)
    experiencia = ft.TextField(label="Experiencia Profesional", multiline=True)
    formacion = ft.TextField(label="Formación Académica", multiline=True)
    certificaciones = ft.TextField(label="Certificaciones", multiline=True)
    conocimientos = ft.TextField(label="Conocimientos Técnicos", multiline=True)
    idiomas = ft.TextField(label="Idiomas", multiline=True)
    logros = ft.TextField(label="Logros Destacados", multiline=True)

    mensaje = ft.Text(value="", color="green")

    # Área de preview
    preview = ft.TextField(
        label="Vista previa del CV",
        multiline=True,
        read_only=True,
        expand=True
    )

    # Función para actualizar preview
    def actualizarPreview(e=None):
        preview.value = (
            f"{nombre.value}\n{titulo.value}\n{contacto.value}\n{ubicacion.value}\n"
            f"LinkedIn: {linkedin.value}\nGitHub: {github.value}\n\n"
            f"Perfil Profesional:\n{perfil.value}\n\n"
            f"Experiencia Profesional:\n{experiencia.value}\n\n"
            f"Formación Académica:\n{formacion.value}\n\n"
            f"Certificaciones:\n{certificaciones.value}\n\n"
            f"Conocimientos Técnicos:\n{conocimientos.value}\n\n"
            f"Idiomas:\n{idiomas.value}\n\n"
            f"Logros Destacados:\n{logros.value}\n"
        )
        page.update()
    # Acción: limpiar todos los campos
    def limpiarCampos(e):
        for campo in [nombre, titulo, contacto, ubicacion, linkedin, github,
                  perfil, experiencia, formacion, certificaciones,
                  conocimientos, idiomas, logros, nombreArchivoPDF]:
            campo.value = ""
        preview.value = ""   # también limpiamos el preview
        mensaje.value = ""   # limpiamos el mensaje
        page.update()

    # Acción: generar PDF
    def generadorArchivoPDF(e):
        datos.nombre = nombre.value
        datos.titulo = titulo.value
        datos.contacto = contacto.value
        datos.ubicacion = ubicacion.value
        datos.linkedin = linkedin.value
        datos.github = github.value
        datos.perfil = perfil.value
        datos.experiencia = experiencia.value
        datos.formacion = formacion.value
        datos.certificaciones = certificaciones.value
        datos.conocimientos = conocimientos.value
        datos.idiomas = idiomas.value
        datos.logros = logros.value

        # Usar el nombre que el usuario escribió
        archivo = (nombreArchivoPDF.value.strip() or "curriculum_flet") + ".pdf"
        ruta = CrearCurriculum(datos, archivo)
        nonlocal archivo_pdf
        archivo_pdf = ruta
        mensaje.value = f"✅ PDF generado en: {ruta}"
        page.update()

    # Vincular actualización de preview a cada campo
    for campo in [nombre, titulo, contacto, ubicacion, linkedin, github,
                  perfil, experiencia, formacion, certificaciones,
                  conocimientos, idiomas, logros]:
        campo.on_change = actualizarPreview

    # Footer con derechos reservados y enlace
    footer = ft.Container(
        content=ft.Row(
            [
                ft.Text("© 2026 Todos los derechos reservados a David Salas"),
                ft.TextButton(
                "Repositorio en GitHub",
                url="https://github.com/12345star",  # aquí pones tu enlace
             ),
            ],
            alignment="spaceBetween",  # separa el texto y el botón
        ),
        padding=10,
        bgcolor=ft.Colors.BLACK12,  # color de fondo suave
    )

    # Layout: formulario a la izquierda, preview a la derecha
    page.add(
        ft.Row([
            ft.Column([
                nombreArchivoPDF,  # campo para nombre del archivo PDF
                nombre, titulo, contacto, ubicacion, linkedin, github,
                perfil, experiencia, formacion, certificaciones,
                conocimientos, idiomas, logros,
                ft.Row([
                    ft.ElevatedButton("Generar PDF", on_click=generadorArchivoPDF),
                    ft.ElevatedButton("Limpiar campos", on_click=limpiarCampos)  # nuevo botón

                ]),
                mensaje
            ], expand=1),
            preview
        ], expand=True),
        footer  # aquí se añade el footer
    )


ft.app(target=main)



