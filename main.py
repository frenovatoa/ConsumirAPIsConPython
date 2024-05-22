import requests
import json

if __name__ == '__main__':
    
    # Con el método post se crea un recurso en el servidor.
    # En el atributo data se envía la información que se quiere almacenar en el servidor.
    url = 'https://httpbin.org/post'
    payload = {'nombre': 'felipe', 'curso': 'python', 'nivel': 'intermedio'}
    
    # response = requests.post(url, json=payload)
    response = requests.post(url, data=json.dumps(payload))
    
    '''
    - json: POST se encarga de serializar el diccionario en un formato JSON.
    - data: Nosotros debemos serializar los datos.
    '''
    print(response.url)
    
    if response.status_code == 200:
        print(response.content)