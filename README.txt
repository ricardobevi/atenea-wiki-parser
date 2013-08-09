Pasos para cargar los articulos de wikipedia en mysql



- Descargar el dump de wikipedia y descomprimirlo en dump.xml

- Limpiar el wiki markup:

./WikiExtractor.py -s -f tanl dump.xml outTANL2/

- Convertir a xml (genera un archivo data.xml):

python toXml.py

- Crear BD con el script de sql

- Cargar los datos:

LOAD XML LOCAL INFILE 'h:\\data.xml' INTO TABLE articulo CHARACTER SET UTF8 (titulo, subtitulo, cuerpo);
