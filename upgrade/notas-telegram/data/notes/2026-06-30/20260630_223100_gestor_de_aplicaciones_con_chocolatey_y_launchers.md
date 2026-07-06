---
id: "20260630223100"
title: "22:31 - Gestor de aplicaciones con chocolatey y launchers"
key: "gestor_de_aplicaciones_con_chocolatey_y_launchers"
created_at: "2026-06-30T22:31:00.833145"
tags:
  - "Gestor de aplicaciones"
  - "Chocolatey"
  - "Validación de instalación"
  - "Flujo instalar/actualizar"
  - "Integración con menú"
  - "Launchers"
  - "Gestor de rutas"
  - "Pestañas"
related_terms:
  - "gestor de aplicaciones"
  - "Chocolatey"
  - "instalación"
  - "actualización"
  - "menú"
  - "launchers"
  - "rutas"
  - "gestor de rutas"
  - "Calibre"
  - "PowerShell"
  - "pestañas"
  - "última versión"
---

# 22:31 - Gestor de aplicaciones con chocolatey y launchers

## Nota limpia

El gestor de aplicaciones debe poder administrar aplicaciones de Chocolatey y validar si Chocolatey está instalado. Esto podría hacerse con un intento de instalación desde el propio menú: si ya está instalado, no pasa nada o se procede a actualizar; si no está instalado, se instala.

Una vez que Chocolatey esté disponible, el sistema debe revisar si otras aplicaciones ya están instaladas. Esas aplicaciones deben aparecer tanto en el gestor como en el menú. Desde el menú, al hacer clic en una aplicación, el comportamiento debe ser el siguiente: si está instalada, intentar actualizarla; si no hay actualización, mostrar un mensaje indicando que ya se tiene la última versión; si no está instalada, instalarla.

El gestor también debe permitir agregar aplicaciones o entradas específicas, por ejemplo Calibre y otro elemento para el gestor de rutas.

Hay un tema pendiente con los launchers: el menú también los maneja, pero dependen de cierta ruta y posiblemente también del nombre del launcher. Esto no está del todo claro todavía, así que conviene revisar si puede resolverse usando el mismo nombre del launcher.

Además, si PowerShell se va a manejar en otra pestaña, entonces se podría tener un gestor de aplicaciones con tres pestañas, todas integradas en un solo menú.

## Conceptos clave

- **Gestor de aplicaciones**: Componente que debe administrar aplicaciones, su instalación, actualización y visibilidad dentro del menú.
- **Chocolatey**: Sistema cuya instalación debe validarse y desde el cual se gestionan aplicaciones.
- **Validación de instalación**: Proceso para comprobar si Chocolatey ya está instalado y decidir si se instala o actualiza.
- **Flujo instalar/actualizar**: Comportamiento esperado al seleccionar una aplicación: instalar si no existe, actualizar si ya está instalada o informar que ya está en la última versión.
- **Integración con menú**: Las aplicaciones gestionadas deben aparecer tanto en el gestor como en el menú principal.
- **Launchers**: Elementos que también maneja el menú y que dependen de una ruta y posiblemente del nombre del launcher.
- **Gestor de rutas**: Elemento mencionado como parte de las entradas o aplicaciones que el gestor debería poder agregar.
- **Pestañas**: Organización propuesta del gestor, con tres pestañas integradas en un solo menú.

## Terminos relacionados

- gestor de aplicaciones
- Chocolatey
- instalación
- actualización
- menú
- launchers
- rutas
- gestor de rutas
- Calibre
- PowerShell
- pestañas
- última versión
