// Pseudocodigos de la Actividad 2 - Entrada y salida de datos

Algoritmo AreaCuadrado
  Escribir "Ingresa el lado"
  Leer lado
  Si lado <= 0 Entonces
    Escribir "Error: lado invalido"
  SiNo
    area <- lado * lado
    Escribir "Area = ", area
  FinSi
FinAlgoritmo

Algoritmo AreaCuadradoPow
  Escribir "Ingresa el lado"
  Leer lado
  Si lado <= 0 Entonces
    Escribir "Error: lado invalido"
  SiNo
    area <- lado ^ 2
    Escribir "Area = ", area
  FinSi
FinAlgoritmo

Algoritmo AreaCirculo
  PI <- 3.141592653589793
  Escribir "Ingresa el radio"
  Leer radio
  Si radio <= 0 Entonces
    Escribir "Error: radio invalido"
  SiNo
    area <- PI * radio ^ 2
    Escribir "Area = ", area
  FinSi
FinAlgoritmo

Algoritmo AreaTriangulo
  Escribir "Ingresa base y altura"
  Leer base, altura
  Si base <= 0 O altura <= 0 Entonces
    Escribir "Error: datos invalidos"
  SiNo
    area <- base * altura / 2
    Escribir "Area = ", area
  FinSi
FinAlgoritmo

Algoritmo Hipotenusa
  Escribir "Ingresa los dos catetos"
  Leer catetoA, catetoB
  Si catetoA <= 0 O catetoB <= 0 Entonces
    Escribir "Error: catetos invalidos"
  SiNo
    hipotenusa <- RC(catetoA ^ 2 + catetoB ^ 2)
    Escribir "Hipotenusa = ", hipotenusa
  FinSi
FinAlgoritmo

Algoritmo NombreSemestre
  Escribir "Ingresa tu nombre completo"
  Leer nombre
  Escribir "Ingresa el semestre"
  Leer semestre
  Si semestre <= 0 Entonces
    Escribir "Error: semestre invalido"
  SiNo
    Escribir "Nombre: ", nombre
    Escribir "Semestre: ", semestre
  FinSi
FinAlgoritmo

Algoritmo FahrenheitCentigrados
  Escribir "Ingresa grados Fahrenheit"
  Leer fahrenheit
  centigrados <- (fahrenheit - 32) * 5 / 9
  Escribir fahrenheit, " F = ", centigrados, " C"
FinAlgoritmo

Algoritmo PiesMetros
  Escribir "Ingresa la longitud en pies"
  Leer pies
  Si pies < 0 Entonces
    Escribir "Error: longitud invalida"
  SiNo
    metros <- pies * 0.3048
    Escribir "Metros = ", metros
  FinSi
FinAlgoritmo

Algoritmo LibrasKilogramos
  Escribir "Ingresa el peso en libras"
  Leer libras
  Si libras < 0 Entonces
    Escribir "Error: peso invalido"
  SiNo
    kilogramos <- libras * 0.45359237
    Escribir "Kilogramos = ", kilogramos
  FinSi
FinAlgoritmo

Algoritmo AcresHectareas
  Escribir "Ingresa la extension en acres"
  Leer acres
  Si acres < 0 Entonces
    Escribir "Error: extension invalida"
  SiNo
    hectareas <- acres * 4047 / 10000
    Escribir "Hectareas = ", hectareas
  FinSi
FinAlgoritmo

Algoritmo Fuerza
  Escribir "Ingresa masa y aceleracion"
  Leer masa, aceleracion
  Si masa < 0 Entonces
    Escribir "Error: masa invalida"
  SiNo
    fuerza <- masa * aceleracion
    Escribir "Fuerza = ", fuerza, " N"
  FinSi
FinAlgoritmo

Algoritmo VelocidadImpacto
  gravedad <- 9.81
  Escribir "Ingresa la altura"
  Leer altura
  Si altura < 0 Entonces
    Escribir "Error: altura invalida"
  SiNo
    velocidad <- RC(2 * gravedad * altura)
    Escribir "Velocidad = ", velocidad, " m/s"
  FinSi
FinAlgoritmo

Algoritmo EnergiaPotencial
  gravedad <- 9.81
  Escribir "Ingresa masa y altura"
  Leer masa, altura
  Si masa < 0 O altura < 0 Entonces
    Escribir "Error: datos invalidos"
  SiNo
    energia <- masa * gravedad * altura
    Escribir "Energia potencial = ", energia, " J"
  FinSi
FinAlgoritmo

Algoritmo EnergiaCinetica
  Escribir "Ingresa masa y velocidad"
  Leer masa, velocidad
  Si masa < 0 Entonces
    Escribir "Error: masa invalida"
  SiNo
    energia <- masa * velocidad ^ 2 / 2
    Escribir "Energia cinetica = ", energia, " J"
  FinSi
FinAlgoritmo

Algoritmo HipotenusaCatetos
  Escribir "Ingresa los catetos"
  Leer cateto1, cateto2
  Si cateto1 <= 0 O cateto2 <= 0 Entonces
    Escribir "Error: catetos invalidos"
  SiNo
    hipotenusa <- RC(cateto1 ^ 2 + cateto2 ^ 2)
    Escribir "Hipotenusa = ", hipotenusa
  FinSi
FinAlgoritmo

Algoritmo VolumenEsfera
  PI <- 3.141592653589793
  Escribir "Ingresa el radio"
  Leer radio
  Si radio <= 0 Entonces
    Escribir "Error: radio invalido"
  SiNo
    volumen <- (4 / 3) * PI * radio ^ 3
    Escribir "Volumen = ", volumen
  FinSi
FinAlgoritmo

Algoritmo ReciboLuz
  Escribir "Ingresa nombre, consumo y tarifa"
  Leer nombre, consumo, tarifa
  Si consumo < 0 O tarifa < 0 Entonces
    Escribir "Error: datos invalidos"
  SiNo
    pago <- consumo * tarifa
    Escribir "Cliente: ", nombre
    Escribir "Pago: $", pago
  FinSi
FinAlgoritmo

Algoritmo PiesLibras
  Escribir "Ingresa pies y libras"
  Leer pies, libras
  Si pies < 0 O libras < 0 Entonces
    Escribir "Error: datos invalidos"
  SiNo
    metros <- pies * 0.3048
    kilogramos <- libras * 0.45359237
    Escribir "Metros = ", metros
    Escribir "Kilogramos = ", kilogramos
  FinSi
FinAlgoritmo

Algoritmo AreaHeron
  Escribir "Ingresa los lados a, b y c"
  Leer a, b, c
  Si a <= 0 O b <= 0 O c <= 0 O a+b <= c O a+c <= b O b+c <= a Entonces
    Escribir "Error: triangulo invalido"
  SiNo
    semiperimetro <- (a + b + c) / 2
    area <- RC(semiperimetro * (semiperimetro-a) * (semiperimetro-b) * (semiperimetro-c))
    Escribir "Area = ", area
  FinSi
FinAlgoritmo
