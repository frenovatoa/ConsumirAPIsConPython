import requests

if __name__ == '__main__':
    
    # Dentro del atributo args del contenido de la respuesta se encuentran los parámetros enviados en la petición GET.
    # La siguiente es una forma no tan eficiente de enviar parámetros en una petición:
    # url = 'https://httpbin.org/get?nombre=felipe&curso=python'
    
    # Resulta más óptimo enviarlos a través de un diccionario, como se muestra a continuación:
    url = 'https://httpbin.org/get'
    args = {'nombre': 'felipe', 'curso': 'python', 'nivel': 'intermedio'}
    response = requests.get(url, params=args)
    
    if response.status_code == 200:
        content = response.content
        print(content)