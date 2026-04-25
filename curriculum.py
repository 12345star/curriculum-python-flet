from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

class CurriculumData:
    def __init__(self,
                 nombre="", titulo="", contacto="", ubicacion="",
                 linkedin="", github="", perfil="", experiencia="",
                 formacion="", certificaciones="", conocimientos="",
                 idiomas="", logros=""):
        self.nombre = nombre
        self.titulo = titulo
        self.contacto = contacto
        self.ubicacion = ubicacion
        self.linkedin = linkedin
        self.github = github
        self.perfil = perfil
        self.experiencia = experiencia
        self.formacion = formacion
        self.certificaciones = certificaciones
        self.conocimientos = conocimientos
        self.idiomas = idiomas
        self.logros = logros


def CrearCurriculum(datos: CurriculumData, nombre_archivo="curriculum.pdf"):
    ruta_salida = os.path.join(os.getcwd(), nombre_archivo)
    c = canvas.Canvas(ruta_salida, pagesize=LETTER)
    ancho, alto = LETTER

    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]

    # Función para dibujar encabezado en cada página
    def dibujaEncabezado():
        c.setFont("Helvetica-Bold", 16)
        c.drawString(72, alto - 72, datos.nombre)
        c.setFont("Helvetica", 12)
        c.drawString(72, alto - 90, datos.titulo)
        c.drawString(72, alto - 110, datos.contacto)
        c.drawString(72, alto - 130, datos.ubicacion)
        c.drawString(72, alto - 150, f"LinkedIn: {datos.linkedin}")
        c.drawString(72, alto - 170, f"GitHub: {datos.github}")

    # Función auxiliar para escribir secciones con salto de página dinámico
    def escribirSeccion(titulo, texto, y_pos):
        if not texto.strip():
            return y_pos

        # Crear párrafo para medir altura
        p = Paragraph(texto.replace("\n", "<br/>"), normal_style)
        w, h = p.wrap(ancho - 144, alto)

        # Validar si cabe en la página actual
        if y_pos - h < 72:  # margen inferior
            c.showPage()
            dibujaEncabezado()
            y_pos = alto - 210  # reiniciar posición debajo del encabezado

        # Escribir título
        c.setFont("Helvetica-Bold", 14)
        c.drawString(72, y_pos, titulo)

        # Dibujar párrafo debajo del título
        p.drawOn(c, 72, y_pos - 20 - h)

        return y_pos - 40 - h

    # Dibujar encabezado inicial
    dibujaEncabezado()
    y = alto - 210

    # Secciones dinámicas
    y = escribirSeccion("Perfil Profesional", datos.perfil, y)
    y = escribirSeccion("Experiencia Profesional", datos.experiencia, y)
    y = escribirSeccion("Formación Académica", datos.formacion, y)
    y = escribirSeccion("Certificaciones", datos.certificaciones, y)
    y = escribirSeccion("Conocimientos Técnicos", datos.conocimientos, y)
    y = escribirSeccion("Idiomas", datos.idiomas, y)
    y = escribirSeccion("Logros Destacados", datos.logros, y)

    c.save()
    return ruta_salida
