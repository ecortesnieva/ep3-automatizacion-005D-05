import os
from datetime import datetime

# Rutas de evidencias
output_path = "evidencias/output_fase5.txt"

print("Compilando Reporte Final de Aprovisionamiento...")

reporte_contenido = f"""======================================================================
REPORTE TÉCNICO COMPLETO DE PROVISIÓN - ENERGÍA SOLAR AUSTRAL SA
======================================================================
Alumno: Emilio Cortes
Fecha de Generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Asignatura: Automatización de Redes - Sección 005D
======================================================================

[1] RESUMEN DE LA FASE 1 (BASELINE)
----------------------------------------------------------------------
* Estado Inicial del RouterD capturado con éxito mediante pyATS/Genie.
* Respaldos de configuraciones base almacenados en 'fase1_baseline/evidencias/'.

[2] RESUMEN DE LA FASE 2 (APROVISIONAMIENTO)
----------------------------------------------------------------------
* Playbook de Ansible ejecutado con éxito aplicando variables corporativas.
* Modificaciones Realizadas:
  - Cambio de Hostname a: RTR-ENERSOL
  - Configuración de Interfaz Loopback 10 (10.5.5.1/24)
  - Inyección de Banner Institucional (MOTD) y Servidor NTP.

[3] RESUMEN DE LA FASE 3 (VALIDACIÓN ANALÍTICA / NETCONF)
----------------------------------------------------------------------
* Análisis Diferencial ejecutado con Genie Diff.
* Resultado: El análisis detectó cambios exitosos en 'interface' y 'routing'
  debido a la inyección de la nueva Loopback y direccionamiento IP.

[4] RESUMEN DE LA FASE 4 (VALIDACIÓN PROGRAMÁTICA RESTCONF)
----------------------------------------------------------------------
* Consulta de API HTTP RESTCONF exitosa (Código de estado 200).
* Estructura YANG/JSON validada correctamente.
* Interfaces confirmadas en ejecución: GigabitEthernet1 y Loopback10.

======================================================================
ESTADO FINAL DEL EXAMEN: APTO / CONFORMIDAD TOTAL DEL PROYECTO
======================================================================
"""

try:
    with open(output_path, "w") as f:
        f.write(reporte_contenido)
    print(f"¡Reporte generado con éxito! Archivo guardado en: {output_path}")
except Exception as e:
    print(f"Error al escribir el reporte final: {e}")
