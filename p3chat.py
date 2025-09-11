# Chatbot Telmex
import re
import time
from datetime import datetime


Promo_RE = r"(?i)(promociones|promos|descuentos|ofertas)"
Contratacion_RE = r"(?i)(contratar|alta|nuevo servicio|instalar|quiero contratar)"
Saldo_RE = r"(?i)(saldo|cuánto debo|estado de cuenta|cuenta pendiente)"
Pago_RE = r"(?i)(pago|quiero pagar|realizar pago|liquidar)"
Convenio_RE = r"(?i)(convenio|acuerdo de pago|plan de pago|diferir)"
Recibo_RE = r"(?i)(recibo|factura|dudas de mi recibo|mi factura|cobro)"
Reporte_RE = r"(?i)(reporte|fallas|problema|no funciona|sin servicio)"
Seguimiento_RE = r"(?i)(seguimiento|estatus de mi reporte|ver avance)"

afirmacion_RE = r"(?i)(sí|claro|gracias|por supuesto|ok|dale)"
salir_RE = r"(?i)(salir|adiós|me equivoqué|perdón|cancelar|terminar)"


state = 0
Salida = 1


while Salida:
    if state == 0:
        print("\nHola soy el Chatbot de Telmex ¿En qué te puedo ayudar?")
        time.sleep(1)
        opcion = input("Opciones: promociones, contratación, saldo, pago, convenio, dudas sobre mi recibo, reporte, seguimiento.\n")

        if re.findall(Promo_RE, opcion):
            state = 1
        elif re.findall(Contratacion_RE, opcion):
            state = 2
        elif re.findall(Saldo_RE, opcion):
            state = 3
        elif re.findall(Pago_RE, opcion):
            state = 4
        elif re.findall(Convenio_RE, opcion):
            state = 5
        elif re.findall(Recibo_RE, opcion):
            state = 6
        elif re.findall(Reporte_RE, opcion):
            state = 7
        elif re.findall(Seguimiento_RE, opcion):
            state = 8
        elif re.findall(salir_RE, opcion):
            state = 99
        else:
            state = 98


    if state == 1:
        print("Nuestras promociones actuales incluyen descuentos en internet y paquetes de telefonía.")
        state = 90

    if state == 2:
        print("Para contratación necesito algunos datos. Un asesor se pondrá en contacto contigo.")
        state = 90

    if state == 3:
        print("Tu saldo actual fue enviado a tu correo electronico.")
        state = 90

    if state == 4:
        print("Puedes realizar tu pago en línea con tarjeta o en tiendas autorizadas.")
        state = 90

    if state == 5:
        print(" Podemos ofrecerte un convenio de pago a 3 o 6 meses sin intereses.")
        state = 90

    if state == 6:
        print("Tu recibo detalla los cargos de renta básica y consumo adicional. ¿Quieres que lo desglose?")
        state = 90

    if state == 7:
        print("Hemos registrado tu reporte de falla. Un técnico lo revisará en las próximas 24 horas.")
        state = 90

    if state == 8:
        print("Tu reporte está en proceso, estimamos la visita del técnico hoy entre 2pm y 6pm.")
        state = 90

    if state == 90:
        opcion = input("¿Te puedo ayudar en algo más? (sí/no)\n")
        if re.findall(afirmacion_RE, opcion):
            state = 0
        elif re.findall(salir_RE, opcion):
            state = 99
        else:
            print("No entendí tu respuesta, regresando al menú principal.")
            state = 0

    if state == 99:
        print("Gracias fue un placer atenderte. ¡Hasta luego!")
        Salida = 0


    if state == 98:
        print(" La opción no pudo ser procesada, intenta con otra.")
        state = 0
