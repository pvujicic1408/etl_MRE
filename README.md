Python skripte koje:

a) proveravaju koji datasetovi su dostupni na ArcGIS servisu
b) preuzima iterativno podatke iz servisa u json i geojson za sve dostupne layere na linku
c) preuzima parametarski definisano u određeni dataset koji je dostupan na linku i pakuje ih u geopackage format
d) preuzima parametarski definisano određeni dataset koji je dostupan na linku i upisuje ga u lokalnu postgres bazu koja ima postgis ekstenziju
e) preuzima parametarski definisano određeni dataset koji je dostupan na linku i upisuje ga u lokalnu postgres bazu koja ima postgis ekstenziju i 
transformiše podatke iz EPSG:4326 u EPSG:32634 i preimenuje kolone tako da nazivi budu malim slovima bez razmaka, sa dodatom kolonom datum_upisa (klona koja označava kada su podaci sinhronizovani)
