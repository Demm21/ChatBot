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

negacion_RE = r"(?i)(no|nunca|jamás|negativo|nop|na|n/nel/nope|no gracias|no, gracias|es todo/eso es todo|nada más|nada|no más|no, nada más|no, nada|no, no más)"
afirmacion_RE = r"(?i)(sí|claro|gracias|por supuesto|ok|dale|vale|bueno|perfecto|claro que sí|si|afirmativo/sí por favor/si, por favor/sí, por favor)"
salir_RE = r"(?i)(salir|adiós|me equivoqué|perdón|cancelar|terminar)"

state = 0
Salida = 1

Falla_Internet_RE = r"(?i)(internet lento|sin internet|falla conexión|caída|no carga páginas|desconexión|internet|no conecta|no tengo internet)"
Falla_Telefono_RE = r"(?i)(sin tono|línea muerta|ruido|interferencia/no funciona|no marca|teléfono|no tengo línea|no hay tono/no me permiten hacer llamadas/no tengo línea/no puedo llamar/no permite recibir llamadas)"

# Expresiones para el módulo de pago
Referencia_RE = r"\b\d{8,12}\b"
Monto_RE = r"\$?\s*(\d+(?:\.\d{1,2})?)"
Email_RE = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
Tarjeta_RE = r"(?i)(tarjeta|crédito|credito|débito|debito|visa|mastercard|master card|amex|american express|pagar con tarjeta|plástico)"
Transferencia_RE = r"(?i)(transferencia|transferencia bancaria|banco|depósito|deposito|spei|clabe|interbancaria|app del banco|bancaria|pago digital)"
Efectivo_RE = r"(?i)(efectivo|oxxo|7eleven|7 eleven|farmacias|tienda|super|supermercado|conveniencia|en persona|pago en tienda|en tienda|a la mano|cash|en cualquier tienda)"
Numero_RE = r"\b[1-3]\b"

# Estados específicos para pago
state_pago = 0
monto_pago = 0
referencia_pago = ""

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

    elif state_pago == 42:
            print(f"\nConfirmado: Vas a pagar ${monto_pago:.2f} para la referencia {referencia_pago}")
            print("¿Cómo deseas realizar tu pago?")
            print("1. Tarjeta de crédito/débito")
            print("2. Transferencia bancaria")
            print("3. Efectivo en tiendas")
            
            metodo_input = input("\nSelecciona una opción (1-3) o describe tu método preferido: ")
            
            if re.findall(Tarjeta_RE, metodo_input) or re.search(Numero_RE, metodo_input) and re.search(r"\b1\b", metodo_input):
                print("\nSerás redirigido a nuestro portal seguro de pagos con tarjeta...")
                time.sleep(2)
                print("Pago procesado exitosamente")
                print(f"Número de transacción: PAG-{datetime.now().strftime('%Y%m%d%H%M%S')}")
                state_pago = 43
            elif re.findall(Transferencia_RE, metodo_input) or re.search(Numero_RE, metodo_input) and re.search(r"\b2\b", metodo_input):
                print("\nDatos para transferencia:")
                print("Banco: BBVA")
                print("CLABE: 012 180 00123456789 1")
                print("Beneficiario: TELMEX SA DE CV")
                print(f"Referencia: {referencia_pago}")
                print(f"Monto: ${monto_pago:.2f}")
                print("\nUna vez realizada la transferencia, tu pago se reflejará en 24-48 horas.")
                state_pago = 43
            elif re.findall(Efectivo_RE, metodo_input) or re.search(Numero_RE, metodo_input) and re.search(r"\b3\b", metodo_input):
                print("\nPuedes pagar en efectivo en:")
                print("- OXXO")
                print("- 7-Eleven")
                print("- Farmacias del Ahorro")
                print("- Supermercados participantes")
                print(f"\nReferencia: {referencia_pago}")
                print(f"Monto: ${monto_pago:.2f}")
                print("Tu pago se procesará en cuanto se realice el depósito.")
                state_pago = 43
            else:
                print("No pude identificar tu método de pago. Por favor selecciona 1, 2 o 3.")
                
        elif state_pago == 43:
            while True:
                print(f"\n¿Deseas recibir el comprobante de pago de ${monto_pago:.2f} por correo?")
                respuesta = input("(sí/no): ")
                
                if re.findall(afirmacion_RE, respuesta):
                    while True: 
                        email_input = input("Por favor ingresa tu correo electrónico: ")
                        if re.fullmatch(Email_RE, email_input):
                            print(f"Comprobante enviado a {email_input}")
                            break
                        else:
                            print("El correo electrónico no es válido. Por favor, intenta de nuevo.")
                    break 
                    
                elif re.findall(negacion_RE, respuesta):
                    print("De acuerdo, no se enviará comprobante.")
                    break
                    
                else:
                    print("No entendí tu respuesta.")
                    print("Por favor responde 'sí' para continuar o 'no' para salir.")
            
            print("¡Gracias por tu pago!")
            state = 90
            state_pago = 0 

    if state == 5:
        print(" Podemos ofrecerte un convenio de pago a 3 o 6 meses sin intereses.")
        state = 90

    if state == 6:
        print("Tu recibo detalla los cargos de renta básica y consumo adicional. ¿Quieres que lo desglose?")
        state = 90

    if state == 7:
        print("\nPor favor, selecciona un numero para el tipo de reporte:")
        print("1. Fallas de Internet")
        print("2. Fallas de Telefonía")
        
        tipo_falla = input("\n¿Qué tipo de falla deseas reportar? (1/2): ")
        
        if tipo_falla == "1":
            print("\n¿Qué problema tienes con tu internet?")
            print("Problemas comunes:")
            print("- Internet lento")
            print("- Sin internet")
            print("- Falla conexión")
            detalle = input("\nDescribe la falla: ")
            if re.findall(Falla_Internet_RE, detalle):
                print("\nRealizando diagnóstico de tu conexión...")
                time.sleep(2)
                print("He registrado tu reporte de falla de internet.")
                print("Número de reporte: INT-" + str(datetime.now().strftime("%Y%m%d%H")))
            else:
                print("No pude identificar el tipo específico de falla, pero registraré tu reporte.")
        
        elif tipo_falla == "2":
            print("\n¿Qué problema tienes con tu teléfono?")
            print("Problemas comunes:")
            print("- Sin tono")
            print("- Línea muerta")
            print("- Ruido o interferencia")
            detalle = input("\nDescribe la falla: ")
            if re.findall(Falla_Telefono_RE, detalle):
                print("\nRealizando diagnóstico de tu línea telefónica...")
                time.sleep(2)
                print("He registrado tu reporte de falla de telefonía.")
                print("Número de reporte: TEL-" + str(datetime.now().strftime("%Y%m%d%H")))
            else:
                print("No pude identificar el tipo específico de falla, pero registraré tu reporte.")
        
        else:
            print("\nOpción no válida. Registraré un reporte general.")
        
        print("\nUn técnico revisará tu caso en las próximas 24 horas.")
        state = 90

    if state == 8:
        print("Tu reporte está en proceso, estimamos la visita del técnico hoy entre 2pm y 6pm.")
        state = 90

    if state == 90:
        opcion = input("¿Te puedo ayudar en algo más? (sí/no)\n")
        if re.findall(afirmacion_RE, opcion):
            state = 0
        elif re.findall(negacion_RE, opcion) or re.findall(salir_RE, opcion):
            state = 99
        else:
            print("No entendí tu respuesta.")
            print("Por favor responde 'sí' para continuar o 'no' para salir.")
            state = 90

    if state == 99:
        print("Gracias fue un placer atenderte. ¡Hasta luego!")
        Salida = 0


    if state == 98:
        print(" La opción no pudo ser procesada, intenta con otra.")
        state = 0
