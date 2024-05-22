import requests
import json

if __name__ == '__main__':
    
    url = 'https://httpbin.org/post'
    payload = { 'nombre': 'felipe', 'curso': 'python', 'nivel': 'intermedio' }
    # Se pueden enviar n cantidad de encabezados al servidor.
    headers = { 'Content-Type': 'application/json', 'access-token': '12345' }
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    
    print(response.url)
    
    if response.status_code == 200:
        # print(response.content)
        # Como cliente, puede ser necesario leer los encabezados que el servidor envía.
        headers_response = response.headers # Diccionario.
        print(headers_response)
        server = headers_response['Server']
        print(server)