Monomi-Scrapy
=============

Instalar Scrapy
    
    pip install scrapy

Actualizar el archivo monomi_spider.py

    url = "http://fsh-store.monomi.co"

Cambiar *url* por la url principal de la tienda en Monomi.co

¡Listo!

Ejecutar

    scrapy crawl monomi -o items.json -t json

Ésto genera un archivo .json que se puede usar para cargar los productos de una tienda en Monomi.co en un sitio web propio.

[@c_samiro](http://twitter.com/c_samiro)