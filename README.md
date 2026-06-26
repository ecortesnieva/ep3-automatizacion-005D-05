# Informe Técnico de Implementación y Automatización de Red
**Cliente:** Energia Solar Austral SA  
**Ingeniero a Cargo:** Emilio Alejandro Cortés Nieva  
**Código de Alumno:** 005D-05  
**Asignatura:** Programación y Redes Virtualizadas (DRY7122)  

---

## 1. Objetivo del Proyecto
El presente proyecto consistió en el diseño, despliegue y auditoría automatizada de la configuración estándar de red corporativa sobre un nuevo router Cisco CSR1kv integrado a la infraestructura de Energia Solar Austral SA. El objetivo principal radica en mitigar errores humanos de aprovisionamiento manual a través de un ciclo integral de automatización (DevOps/NetDevOps) que abarca el levantamiento del estado inicial del dispositivo, el despliegue idempotente de políticas de cumplimiento y la validación independiente multifase empleando interfaces programables.

## 2. Alcance
* **Dentro del Alcance:** 
  * Captura del estado base del router mediante herramientas de análisis estructurado SSH.
  * Respaldo previo automatizado de la configuración de fábrica de la plataforma.
  * Habilitación de protocolos de gestión programable de última generación (NETCONF, RESTCONF y HTTP Seguro).
  * Aprovisionamiento automatizado de parámetros de red asignados: Hostname corporativo, banners legales de acceso, servidores globales de tiempo (NTP), descripción formal de interfaces WAN e inyección de interfaces virtuales (Loopback) para la gestión remota.
  * Validación programática de la correcta inyección de variables utilizando respuestas nativas estructuradas en XML y JSON.
  * Generación dinámica de reportes de cumplimiento diferencial (Compliance Audit).
* **Fuera del Alcance:** 
  * Enrutamiento dinámico perimetral (OSPF/BGP), políticas avanzadas de firewalling, hardening de listas de control de acceso (ACL) de producción, y conexionado físico o aprovisionamiento del hipervisor de virtualización.

## 3. Infraestructura Utilizada
* **Estación de Trabajo de Ingeniería (Control Node):** DEVASC VM ejecutando entorno basado en Linux Ubuntu, equipado con Ansible 2.x, Python 3.x, pyATS/Genie framework, y bibliotecas de desarrollo de software `ncclient` y `requests`.
* **Dispositivo de Red Objetivo (Managed Node):** Cisco Cloud Services Router (CSR1kv) ejecutando el sistema operativo Cisco IOS XE.
* **Medio de Conectividad:** Red interna privada virtualizada (Modo Host-Only) operando bajo el segmento `192.168.56.0/24`, con el router ubicado en la dirección IP estática de gestión `192.168.56.101`.

## 4. Tecnologías Empleadas y Justificación
* **pyATS / Genie:** Se utilizó en la Fase 1 y Fase 5 para capturar snapshots de bajo nivel del estado de la red (interfaces, plataformas, enrutamiento). Permite convertir outputs crudos de consola CLI en diccionarios estructurados de Python y generar un reporte diferencial (`genie diff`) sumamente preciso para auditorías de cumplimiento.
* **Ansible:** Se seleccionó en la Fase 2 como el motor de orquestación principal gracias a su arquitectura sin agentes (*agentless*) y su capacidad intrínseca de idempotencia, garantizando que el playbook corporativo pueda ejecutarse múltiples veces sin alterar configuraciones correctas ni generar duplicados.
* **NETCONF (Network Configuration Protocol):** Empleado en la Fase 3 mediante el puerto TCP 830 para realizar una validación de solo lectura basada en el modelo de datos unificado de la industria `Cisco-IOS-XE-native`. Garantiza transacciones seguras y robustas basadas en árboles de datos XML.
* **RESTCONF:** Utilizado en la Fase 4 para validar de manera modular recursos específicos en formato JSON mediante llamadas HTTP (API REST-like). Se justifica por su ligereza y agilidad para interactuar con sistemas de monitoreo externos utilizando verbos estándar de la web (GET).

## 5. Configuración Aplicada
La siguiente tabla detalla la parametrización corporativa obligatoria inyectada de manera automatizada al nodo de red:

| Parámetro de Red | Valor Corporativo Inyectado |
| :--- | :--- |
| **Código de Alumno** | 005D-05 |
| **Empresa Mandante** | Energia Solar Austral SA |
| **Hostname Corporativo** | RTR-ENERSOL |
| **IP Loopback de Gestión (Loopback10)** | 10.5.5.1 |
| **Máscara de Subred Loopback** | 255.255.255.0 (/24) |
| **Descripción Interfaz WAN (Gi1)** | Enlace-WAN-Antofagasta |
| **Banner de Acceso Legal** | ACCESO RESTRINGIDO - ENERSOL |
| **Servidor NTP Primario** | 1.1.1.1 |
| **Dirección IP de Acceso Base** | 192.168.56.101 |

## 6. Resultados de Validación
Las auditorías programáticas de datos se ejecutaron con éxito, arrojando un estado de cumplimiento absoluto sin registrar fallos de consistencia:

| Fase de Validación | Protocolo / Herramienta | Criterios Evaluados | Estado Final |
| :--- | :--- | :--- | :--- |
| **Fase 3: Auditoría Externa** | NETCONF (`ncclient`) | Hostname, IP Loopback, Máscara, Descripción WAN, Servidor NTP (XML) | **[OK] CONFORME** |
| **Fase 4: Auditoría API** | RESTCONF (`requests`) | Endpoint Hostname, Endpoint Loopback, Endpoint Interfaces, Endpoint NTP (JSON) | **[OK] CONFORME** |
| **Fase 5: Compliance Diff** | Genie Diff Engine | Comparativa estructural de estados operativos pre vs. post-aprovisionamiento | **[OK] CONFORME** |

## 7. Conclusiones
El despliegue automatizado del nuevo enrutador para **Energia Solar Austral SA** concluyó de forma totalmente exitosa. Las pruebas de idempotencia de Ansible ratificaron la estabilidad de la configuración de red y las llamadas remotas por API (NETCONF/RESTCONF) comprobaron la concordancia bit a bit de las variables desplegadas frente al diccionario maestro del proyecto. El router se encuentra catalogado en estado **CONFORME**, con sus capacidades de automatización locales operativas, quedando formalmente entregado para su paso inmediato al entorno de producción y operaciones de la empresa.
