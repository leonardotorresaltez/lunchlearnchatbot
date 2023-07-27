
from flask import Flask, jsonify, request
import mychatbot


app = Flask(__name__)
myChatBot = mychatbot.MyChatBot()




@app.route("/webhook/", methods=["POST", "GET"])
def webhook_whatsapp():
    #SI HAY DATOS RECIBIDOS VIA GET
    if request.method == "GET":
        #SI EL TOKEN ES IGUAL AL QUE RECIBIMOS
        if request.args.get('hub.verify_token') == "mimacom":
            #ESCRIBIMOS EN EL NAVEGADOR EL VALOR DEL RETO RECIBIDO DESDE FACEBOOK
            return request.args.get('hub.challenge')
        else:
            #SI NO SON IGUALES RETORNAMOS UN MENSAJE DE ERROR
          return "Error de autentificacion."
    #RECIBIMOS TODOS LOS DATOS ENVIADO VIA JSON
    data=request.get_json()


    mensaje = None
    telefonoCliente = None
    try:
        #EXTRAEMOS EL NUMERO DE TELEFONO Y EL MANSAJE
        telefonoCliente=data['entry'][0]['changes'][0]['value']['messages'][0]['from']
        #EXTRAEMOS EL TELEFONO DEL CLIENTE
        mensaje=data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
        #EXTRAEMOS EL ID DE WHATSAPP DEL ARRAY
        idWA=data['entry'][0]['changes'][0]['value']['messages'][0]['id']
        #EXTRAEMOS EL TIEMPO DE WHATSAPP DEL ARRAY
        timestamp=data['entry'][0]['changes'][0]['value']['messages'][0]['timestamp']
        recipient_id=data['entry'][0]['changes'][0]['value']['messages'][0]['timestamp']
        #ESCRIBIMOS EL NUMERO DE TELEFONO Y EL MENSAJE EN EL ARCHIVO TEXTO
        #SI HAY UN MENSAJE
        print("datos de json:")
        print("telefonoCliente:",telefonoCliente)
        print("mensaje:",mensaje)
        print("idWA:",idWA)
        print("timestamp:",timestamp)
        print("recipient_id:",recipient_id)
    except Exception  as err:
        print('Handling run-time error:', err)
    
    if mensaje is not None:
      myChatBot.initializeBot()  
      resp = myChatBot.newmessage(telefonoCliente,mensaje)
      enviar(telefonoCliente,resp)
    return jsonify({"status": "success"}, 200)
    


def enviar(telefonoRecibe,respuesta):
   from heyoo import WhatsApp
   #token de acceso temporal de la pestaña "Configuracion de la api" de la app en developer.facebook
   token = "AAAA"
   #id del numero de telefono origen ( desde donde contesta el chatbot) aparece en la pestaña "Configuracion de la api" de la app en developer.facebook
   idNumeroTelefono = "1111"
   mensajeWa = WhatsApp(token,idNumeroTelefono)
   response = mensajeWa.send_message(respuesta,telefonoRecibe)
   print("reponse:",response)

#INICIAMSO FLASK
if __name__ == "__main__":
  app.run(debug=True)
