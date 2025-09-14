# Resumen de la actividad

Actividad del modulo 3 de curso de **conexión y protección de redes** del certificado en ciberseguridad de google. 

Se analiza un archivo que contiene el trafico DNS de la capa de aplicación y ICMP de la capa de internet en el modelo TCP/I de un pagina web ficticia "yummyrecipesforme.com", con la finalidad de identificar un posible ataque de denegación de servicio (DoS) e identificar el método usado para realizar el ataque.

## Objetivos
- Analizar el tráfico de red para identificar patrones inusuales.
- Determinar que protocolo de rede se vio afectado durante el incidente.
- Redactar infor

## Hallazgos

- Al visitar la pagina web se observa el error "puerto de destino inalcanzable".
- Al enviar paquetes UDP en el analizador de red se recibe un mensaje ICMP con el mensaje "udp port 53 unreachable".