import requests

if __name__ == '__main__':
    url = 'https://www.google.com.mx/'
    response = requests.get(url)
    
    if response.status_code == 200:
        # En este caso, si la petición fue exitosa, guardamos el contenido de la página en un archivo.
        content = response.content
        file = open('google.html', 'wb')
        file.write(content)
        file.close()