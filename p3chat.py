# Chatbot Telmex - Versión Ampliada
import re
import time
from datetime import datetime

# Expresiones regulares ampliadas para mayor cobertura
Promo_RE = r"(?i)(promociones?|promos?|descuentos?|ofertas?|planes? nuevos?|tarifas?|paquetes?|especiales?|baratos?|económicos?|mejores? precios?|qué tienen|qué hay|qué me ofrecen)"

Contratacion_RE = r"(?i)(contratar|alta|nuevo servicio|instalar|quiero contratar|quiero servicio|quiero línea nueva|quiero internet|dar de alta|solicitar|pedir servicio|necesito internet|necesito teléfono|quiero telmex|cómo contrato|requisitos|me interesa)"

Saldo_RE = r"(?i)(saldo|cuánto debo|cu[aá]nto debo|estado de cuenta|cuenta pendiente|mi deuda|debo algo|tengo que pagar|adeudo|balance|cuánto me cobran|qué debo|mi cuenta|revisar cuenta|consultar saldo)"

Pago_RE = r"(?i)(pago|quiero pagar|realizar pago|liquidar|abonar|pagar en línea|pagar en l[ií]nea|forma de pago|formas de pago|dónde pago|donde pago|cómo pago|métodos de pago|pagar con tarjeta|pagar efectivo|bancos|oxxo|seven|tiendas)"

Convenio_RE = r"(?i)(convenio|acuerdo de pago|plan de pago|diferir|aplazar|pago parcial|mensualidades|facilidades|no puedo pagar|pagar poco a poco|dividir pago|pago en partes|ayuda para pagar)"

Recibo_RE = r"(?i)(recibo|factura|dudas de mi recibo|mi factura|cobro|cargos|me llegó caro|recibo alto|recibo elevado|por qué tanto|explicar recibo|desglose|conceptos|qué me cobran|facturación|billing)"

Reporte_RE = r"(?i)(reporte|reportar|fallas?|problema|problemas|no funciona|sin servicio|internet caído|internet ca[ií]do|teléfono muerto|tel[eé]fono muerto|lentitud|lento|no hay señal|sin línea|descompuesto|avería|falla técnica)"

Seguimiento_RE = r"(?i)(seguimiento|estatus de mi reporte|ver avance|estado del reporte|qué pasó con mi folio|mi folio|número de reporte|cuándo vienen|cuándo llega el técnico|avance|progreso|actualización)"

# Expresiones para interacciones naturales
afirmacion_RE = r"(?i)(sí|si|claro|gracias|por supuesto|ok|dale|okey|está bien|perfecto|excelente|correcto|así es|exacto|de acuerdo)"

salir_RE = r"(?i)(salir|adiós|adios|me equivoqué|perdón|perdon|cancelar|terminar|no|chao|bye|hasta luego|nos vemos|ya no|nada más|eso es todo)"

Saludo_RE = r"(?i)(hola|buenos días|buenas tardes|buenas noches|buen día|buena tarde|buena noche|hey|qué tal|cómo estas|como estas|saludos|que onda|buenas|holi|holaa)"

Despedida_RE = r"(?i)(adiós|adios|hasta luego|nos vemos|chao|bye|hasta pronto|que tengas buen día|gracias y adiós|me voy|ya me voy|hasta la vista|cuídate)"

Ayuda_RE = r"(?i)(ayuda|help|no entiendo|qué puedo hacer|opciones|menú|menu|que opciones hay|qué hay|qué me puedes ayudar|en qué me ayudas|servicios|lista)"

Repetir_RE = r"(?i)(repetir|otra vez|de nuevo|repite|vuelve a decir|no escuché|no entendí|puedes repetir)"

# Expresiones para casos específicos adicionales
Horarios_RE = r"(?i)(horarios?|qué hora|a qué hora|cuándo abren|cuándo cierran|horario de atención|cuando atienden)"

Sucursales_RE = r"(?i)(sucursales?|oficinas?|dónde están|donde están|direcciones?|ubicación|ubicaciones|centros de atención|tiendas telmex)"

Quejas_RE = r"(?i)(queja|quejas|reclamación|reclamaciones|inconformidad|mal servicio|servicio malo|estoy molesto|no me gusta)"

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

state = 0
Salida = 1

while Salida:
    if state == 0:
        print("\n¡Hola! Soy tu asistente virtual de Telmex.")
        print("Estoy aquí para ayudarte con todo lo que necesites.")
        time.sleep(1)
        opcion = input("\n¿En qué te puedo ayudar hoy?\n Puedes preguntarme sobre: promociones, contratación, saldo, pagos, convenios, recibo, reportes, seguimientos, horarios, sucursales.\n\n Escribe tu consulta: ")
        
        # Verificar saludos primero
        if re.findall(Saludo_RE, opcion):
            print("¡Hola! Me da mucho gusto saludarte")
            print("Estoy aquí para resolver todas tus dudas sobre Telmex.")
            time.sleep(1)
            state = 0  # Mantener en estado 0 para mostrar opciones nuevamente
            continue
        
        # Verificar si pide ayuda o repetir opciones
        elif re.findall(Ayuda_RE, opcion) or re.findall(Repetir_RE, opcion):
            print("¡Por supuesto! Te ayudo con cualquiera de estos temas:")
            print("Opciones disponibles:")
            print("• Promociones y ofertas especiales")
            print("• Contratación de nuevos servicios")
            print("• Consulta de saldo y estado de cuenta")
            print("• Formas y lugares de pago")
            print("• Convenios y facilidades de pago")
            print("• Dudas sobre tu recibo o factura")
            print("• Reportar fallas o problemas técnicos")
            print("• Seguimiento de reportes")
            print("• Horarios de atención")
            print("• Ubicación de sucursales")
            state = 0  # Volver a mostrar el menú
            continue
        
        # Verificar despedidas
        elif re.findall(Despedida_RE, opcion) or re.findall(salir_RE, opcion):
            state = 99
        
        # Nuevas opciones agregadas
        elif re.findall(Horarios_RE, opcion):
            state = 9
        elif re.findall(Sucursales_RE, opcion):
            state = 10
        elif re.findall(Quejas_RE, opcion):
            state = 11
        
        # Opciones de servicio existentes (ampliadas)
        elif re.findall(Promo_RE, opcion):
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
        else:
            state = 98
    
    # Estados de servicios con respuestas más naturales
    if state == 1:
        print("\nPROMOCIONES ESPECIALES TELMEX")
        print("Te tengo excelentes noticias, estas son nuestras mejores ofertas:")
        print("\n1. Internet Infinitum 200 Mbps - $599/mes por 6 meses")
        print("   (Precio regular $799 - ¡Ahorras $200 mensuales!)")
        print("\n2. Paquete Triple Play Completo - $899/mes por 3 meses")
        print("   Internet + TV + Teléfono (Precio regular $1,199)")
        print("\n3. Internet 100 Mbps + Netflix GRATIS - $499/mes por 12 meses")
        print("   (Precio regular $649 - Netflix incluido sin costo extra)")
        print("\n4. Paquete Empresarial Premium - $1,299/mes por 6 meses")
        print("   Internet 500 Mbps + líneas telefónicas ilimitadas")
        
        opcion_promo = input("\n¿Alguna de estas promociones te llama la atención?(sí/no): ")
        
        if re.findall(afirmacion_RE, opcion_promo):
            email = input("\n¡Excelente elección! \nPara que un asesor especializado te contacte y te ayude con la contratación, necesito tu correo electrónico: ")
            # Validación básica de email
            if "@" in email and "." in email:
                print(f"\n¡Perfecto! Hemos registrado tu interés.")
                print(f" Un asesor experto se comunicará contigo al correo {email}")
                print(" Tiempo estimado de contacto: máximo 2 horas")
                print(" Te ayudará con todos los detalles y la instalación")
                print("\n ¡Gracias por elegir Telmex! Pronto tendrás el mejor servicio.")
            else:
                print("El formato del correo no parece correcto, pero no te preocupes.")
                print("Hemos registrado tu solicitud y un asesor se comunicará contigo pronto.")
                print("También puedes llamar al 800-123-2222 para más información.")
            state = 90
        elif re.findall(salir_RE, opcion_promo) or re.findall(r"(?i)(no|no gracias|no me interesa|tal vez después)", opcion_promo):
            print("No hay problema, entiendo perfectamente.")
            print("Las promociones estarán disponibles cuando gustes consultarlas.")
            print("Si cambias de opinión, aquí estaré para ayudarte.")
            state = 90
        else:
            print(" No logré entender tu respuesta. Te regreso al menú de promociones.")
            state = 1  # Volver a mostrar promociones

    if state == 2:
        print("\n¡CONTRATACIÓN DE SERVICIOS TELMEX!")
        print("Me da mucho gusto que quieras ser parte de la familia Telmex")
        print("\nPara procesar tu solicitud de contratación necesito algunos datos básicos.")
        print("Un asesor especializado se pondrá en contacto contigo para:")
        print("   • Verificar disponibilidad en tu zona")
        print("   • Explicarte los planes disponibles")
        print("   • Programar la instalación")
        print("   • Resolver todas tus dudas")
        print("\nEl contacto será en las próximas 2 horas hábiles.")
        print("También puedes llamar directamente al 800-123-2222")
        state = 90

    if state == 3:
        print("\nCONSULTA DE SALDO")
        print("He enviado tu estado de cuenta actualizado a tu correo electrónico registrado.")
        print("Incluye:")
        print("   • Saldo actual")
        print("   • Fecha de vencimiento")
        print("   • Desglose de servicios")
        print("   • Formas de pago disponibles")
        print("\nSi no lo recibes en 5 minutos, revisa tu carpeta de spam.")
        print("Para dudas inmediatas llama al 800-123-2222")
        state = 90

    if state == 4:
        if state_pago == 40:
            print("\n¡Claro! Te ayudo con tu pago.")
            referencia_input = input(" Para empezar, por favor ingresa tu número de referencia de Telmex: ")
            referencia_match = re.search(Referencia_RE, referencia_input)
            if referencia_match:
                referencia_pago = referencia_match.group()
                state_pago = 41
            else:
                print("El número de referencia no es válido. Debe contener entre 8 y 12 dígitos.")
            
        elif state_pago == 41:
            monto_input = input("Ingresa el monto a pagar: ")
            
            monto_match = re.search(Monto_RE, monto_input)
            if monto_match:
                try:
                    monto_pago = float(monto_match.group(1))
                    state_pago = 42
                except ValueError:
                    print("Por favor, ingresa un monto válido (ejemplo: 499.50)")
            else:
                print("Por favor, ingresa un monto válido (ejemplo: 499.50)")
                
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
        print("\nCONVENIOS Y FACILIDADES DE PAGO")
        print("Entendemos que a veces necesitas flexibilidad para pagar")
        print("\nTe ofrecemos estas opciones:")
        print("   • Convenio a 3 meses SIN INTERESES")
        print("   • Convenio a 6 meses SIN INTERESES")
        print("   • Pago parcial con compromiso de liquidación")
        print("\nBeneficios:")
        print("   • Mantienes tu servicio activo")
        print("   • Sin afectación a tu historial crediticio")
        print("   • Proceso rápido y sencillo")
        print("\nPara solicitar tu convenio llama al 800-123-2222")
        state = 90

    if state == 6:
        print("\nEXPLICACIÓN DE TU RECIBO")
        print("Te ayudo a entender cada concepto de tu factura:")
        print("\nCONCEPTOS PRINCIPALES:")
        print("   • Renta básica: Costo fijo mensual del servicio")
        print("   • Consumo adicional: Llamadas extras o datos excedentes")
        print("   • IVA: Impuesto al Valor Agregado (16%)")
        print("   • Servicios adicionales: Netflix, HBO, etc.")
        print("\n¿Tienes dudas sobre algún cargo específico?")
        print("Envía una foto de tu recibo al WhatsApp 55-1234-5678")
        print("O llama al 800-123-2222 para explicación detallada")
        state = 90

    if state == 7:
        print("\nREPORTE DE FALLAS")
        print("Lamento mucho los inconvenientes que estás experimentando.")
        confirmar = input("\n¿Deseas que levante un reporte técnico ahora? (sí/no): ")

        if re.findall(afirmacion_RE, confirmar):
            ref = input("\nPerfecto. Por favor indícame tu número Telmex o número de cuenta: ")
            ref_digits = re.sub(r"\D", "", ref)
            if len(ref_digits) < 7:
                print("El dato parece incompleto, continuaré con la información disponible.")

            direccion = input("¿En qué domicilio se presenta la falla? (calle y colonia/ciudad): ")
            descripcion = input("Describe brevemente la falla (sin servicio, lento, ruido en línea, etc.): ")
            horario = input("¿Cuál es el mejor horario para visita? (mañana/tarde/noche o 9-14/14-18): ")

            contacto_tipo = input("¿Prefieres contacto por teléfono o por correo? ")
            contacto_valor = ""
            if re.search(r"(?i)tel[eé]fono|cel|m[oó]vil|whats|wa", contacto_tipo):
                contacto_valor = input("Indícame tu número de contacto (10 dígitos): ")
                tel_digits = re.sub(r"\D", "", contacto_valor)
                if len(tel_digits) != 10:
                    print("El número no parece de 10 dígitos; usaré el proporcionado.")
            else:
                contacto_valor = input("Indícame tu correo de contacto: ")
                if not ("@" in contacto_valor and "." in contacto_valor):
                    print("El correo no parece válido; usaré el proporcionado.")

            print("\nResumen de tu reporte:")
            print(f"   • Referencia (línea/cuenta): {ref}")
            print(f"   • Domicilio: {direccion}")
            print(f"   • Falla: {descripcion}")
            print(f"   • Horario preferente: {horario}")
            print(f"   • Contacto: {contacto_valor}")

            confirmar_final = input("\n¿Confirmas levantar el reporte con esta información? (sí/no): ")
            if re.findall(afirmacion_RE, confirmar_final):
                folio = "TLX-" + str(datetime.now().year) + "-" + str(int(time.time()))[-6:]
                print("\n¡Listo! He registrado tu reporte de falla:")
                print(f"   • Fecha y hora: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
                print(f"   • Folio de seguimiento: {folio}")
                print("   • Prioridad: Alta")
                print("\nPROCESO DE ATENCIÓN:")
                print("   • Diagnóstico remoto: Inmediato")
                print("   • Revisión técnica: Máximo 24 horas")
                print("   • Visita técnica (si es necesaria): 24-48 horas")
                print("\nRecibirás SMS o llamada con actualizaciones del progreso.")
                print("Para seguimiento inmediato puedes llamar al 800-123-2222 y proporcionar tu folio.")
                state = 90
            elif re.findall(salir_RE, confirmar_final) or re.findall(r"(?i)(no|no gracias|mejor después|luego)", confirmar_final):
                print("Entendido, no levantaré el reporte por ahora. Si lo deseas, puedo ayudarte en otro tema.")
                state = 90
            else:
                print("No logré entender tu respuesta. Te regreso al menú de reportes.")
                state = 7

        elif re.findall(salir_RE, confirmar) or re.findall(r"(?i)(no|no gracias|no por ahora|luego)", confirmar):
            print("No hay problema. Si cambias de opinión, puedo levantar el reporte cuando gustes.")
            state = 90
        else:
            print("No logré entender tu respuesta. Te regreso al menú de reportes.")
            state = 7

    if state == 8:
        print("\nSEGUIMIENTO DE TU REPORTE")
        print("Déjame revisar el estatus actual de tu caso...")
        time.sleep(2)
        print("\nINFORMACIÓN ACTUALIZADA:")
        print("   • Tu reporte está EN PROCESO")
        print("   • Diagnóstico: Completado ✓")
        print("   • Solución identificada: ✓")
        print("   • Técnico asignado: Juan Pérez (ID: 12345)")
        print("\n VISITA PROGRAMADA:")
        print("   • Fecha: Hoy")
        print("   • Horario estimado: 2:00 PM - 6:00 PM")
        print("   • El técnico te llamará 30 min antes")
        print("\n Cualquier cambio te será notificado por SMS")
        state = 90

    # Nuevos estados agregados
    if state == 9:
        print("\n HORARIOS DE ATENCIÓN TELMEX")
        print(" ATENCIÓN TELEFÓNICA:")
        print("   • Lunes a Domingo: 24 horas")
        print("   • Número: 800-123-2222")
        print("\n SUCURSALES:")
        print("   • Lunes a Viernes: 9:00 AM - 6:00 PM")
        print("   • Sábados: 9:00 AM - 2:00 PM")
        print("   • Domingos: Cerrado")
        print("\nATENCIÓN EN LÍNEA:")
        print("   • Chat: 24/7 en telmex.com")
        print("   • WhatsApp: 55-1234-5678 (24 horas)")
        state = 90

    if state == 10:
        print("\n SUCURSALES TELMEX")
        print(" PRINCIPALES UBICACIONES:")
        print("   • Centro: Av. Juárez 123, Col. Centro")
        print("   • Norte: Av. Insurgentes Norte 456")
        print("   • Sur: Av. División del Norte 789")
        print("   • Oriente: Av. Zaragoza 321")
        print("   • Poniente: Av. Observatorio 654")
        print("\nPara encontrar la sucursal más cercana:")
        print("   • Visita: telmex.com/sucursales")
        print("   • Llama al: 800-123-2222")
        print("   • WhatsApp: 55-1234-5678")
        state = 90

    if state == 11:
        print("\nQUEJAS Y SUGERENCIAS")
        print("Lamento mucho que hayas tenido una mala experiencia")
        print("Tu opinión es muy importante para nosotros.")
        print("\nCANALES PARA TU QUEJA:")
        print("   • Teléfono: 800-123-2222 (Opción 9)")
        print("   • Email: quejas@telmex.com")
        print("   • WhatsApp: 55-1234-5678")
        print("   • Presencial: Cualquier sucursal")
        print("\n TIEMPO DE RESPUESTA:")
        print("   • Acuse de recibo: Inmediato")
        print("   • Investigación: 3-5 días hábiles")
        print("   • Resolución: Máximo 15 días hábiles")
        print("\n Nos comprometemos a resolver tu situación satisfactoriamente.")
        state = 90
    
    # Estado de continuación mejorado
    if state == 90:
        opcion = input("\n ¿Hay algo más en lo que te pueda ayudar? (sí/no): ")
        
        # Verificar despedidas también en este punto
        if re.findall(Despedida_RE, opcion) or re.findall(salir_RE, opcion):
            state = 99
        elif re.findall(afirmacion_RE, opcion):
            print("¡Perfecto! Con mucho gusto te sigo ayudando")
            state = 0
        # También verificar si saluda de nuevo
        elif re.findall(Saludo_RE, opcion):
            print("¡Hola de nuevo! Te ayudo con mucho gusto")
            state = 0
        else:
            print(" No logré entender tu respuesta, pero no te preocupes.")
            print("Te regreso al menú principal para que puedas elegir otra opción.")
            state = 0
    
    # Estado de salida
    if state == 99:
        print("\n¡Gracias por contactar a Telmex!")
        print(" Fue un placer atenderte hoy.")
        print(" Recuerda que estamos disponibles 24/7 para ayudarte.")
        print(" ¡Hasta luego y que tengas un excelente día!")
        Salida = 0
    
    # Estado de error mejorado
    if state == 98:
        print("\n Disculpa, no logré entender exactamente qué necesitas.")
        print("Pero no te preocupes, estoy aquí para ayudarte ")
        print("\n💡 Puedes preguntarme sobre cualquiera de estos temas:")
        print(" • Promociones y ofertas especiales")
        print(" • Contratación de nuevos servicios")
        print(" • Consulta de saldo y estado de cuenta")
        print(" • Formas y lugares de pago")
        print(" • Convenios y facilidades de pago")
        print(" • Dudas sobre recibo o factura")
        print(" • Reportar fallas o problemas")
        print(" • Seguimiento de reportes")
        print(" • Horarios de atención")
        print(" • Ubicación de sucursales")
        print(" • Quejas y sugerencias")
        print("\n Intenta escribir tu consulta de otra manera, por ejemplo:")
        print("   'quiero ver promociones' o 'tengo una falla' o 'dónde pago'")
        state = 0
