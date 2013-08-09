# -*- coding: utf-8 -*-
import re, codecs
from glob import glob

dir = "outTANL2"

xmlHead = \
'<?xml version="1.0"?>' \
'<mysqldump xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">' \
'<database name="wiki">' \
'	<table_structure name="articulo">' \
'		<field Field="id" Type="bigint(20)" Null="NO" Key="PRI" Extra="auto_increment" Comment="" />' \
'		<field Field="titulo" Type="varchar(200)" Null="YES" Key="" Extra="" Comment="" />' \
'		<field Field="subtitulo" Type="varchar(200)" Null="YES" Key="" Extra="" Comment="" />' \
'		<field Field="cuerpo" Type="mediumtext" Null="YES" Key="" Extra="" Comment="" />' \
'		<key Table="articulo" Non_unique="0" Key_name="PRIMARY" Seq_in_index="1" Column_name="id" Collation="A" Cardinality="2" Null="" Index_type="BTREE" Comment="" Index_comment="" />' \
'		<options Name="articulo" Engine="InnoDB" Version="10" Row_format="Compact" Rows="2" Avg_row_length="8192" Data_length="16384" Max_data_length="0" Index_length="0" Data_free="0" Auto_increment="3" Create_time="2013-08-01 02:54:08" Collation="latin1_swedish_ci" Create_options="" Comment="" />' \
'	</table_structure>' \
'	<table_data name="articulo">'
	

files = glob(dir + "/*.raw")
f = codecs.open('data.xml','w')
f.write(xmlHead + '\n')

for fil in files:
    with open (fil, "r") as myfile:

        articulos = re.findall(r'<doc\ id=".*?"\ url=".*?"\ title="(.*?)">(.*?)\n(.*?)</doc>', myfile.read(),re.DOTALL )

        #artic es un articulo de wikipedia
        for artic in articulos:
            articulo = artic[2].replace("</ref>","")

                #primera parte sin subtitulo
            intro = re.search(r'^(.*?)<h[0-9]>', articulo)
            if intro:
                if intro.group(1).strip():
                    #introduccion
                    f.write(u'<row>\n')
                    f.write(u'<field name="titulo">'+artic[0].strip()+u'</field>\n')#.decode('utf-8-sig')
                    f.write(u'<field name="cuerpo">'+intro.group(1).strip().decode('utf-8-sig')+u'</field>\n')
                    f.write(u'</row>\n')
                
                #subtitulos
                subtitulos = re.findall(r'<h[0-9]>(.*?)</h[0-9]>(.*?)(?=<h[0-9]>)', articulo, re.DOTALL )
                for subt in subtitulos:
                    if subt[1].strip():
                        f.write(u'<row>\n')
                        f.write(u'<field name="titulo">'+artic[0].strip().decode('utf-8-sig')+u'</field>\n')
                        f.write(u'<field name="subtitulo">'+subt[0].strip().decode('utf-8-sig')+u'</field>\n')
                        f.write(u'<field name="cuerpo">'+subt[1].strip().decode('utf-8-sig')+u'</field>\n')
                        f.write(u'</row>\n')
            else:
                #el articulo no tiene subtitulos
                if articulo.strip():
                    f.write(u'<row>\n')
                    f.write(u'<field name="titulo">'+artic[0].strip().decode('utf-8-sig')+u'</field>\n')
                    f.write(u'<field name="cuerpo">'+articulo.strip().decode('utf-8-sig')+u'</field>\n')
                    f.write(u'</row>\n')
                
f.write(u'</table_data>\n')
f.write(u'</database>\n')
f.write(u'</mysqldump>\n')
f.close()
