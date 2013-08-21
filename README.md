Monomi-Scrapy
=============

###Requisitos
Scrapy: Para instalar ejecutar "pip install scrapy"

###Configuración básica

####monomi_spider.py

url: La url principal de la tienda en Monomi.co ej: "http://fsh-store.monomi.co"

¡Listo!

Ejecutar:

    scrapy crawl monomi -o items.json -t json

Ésto genera un archivo .json que se puede usar para cargar los productos de una tienda en Monomi.co en un sitio web propio.

@c_samiro[http://twitter.com/c_samiro]