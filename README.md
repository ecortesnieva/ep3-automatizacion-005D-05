# Informe Técnico de Implementación de Automatización de Red con Compliance Auditado

**Alumno:** Emilio Alejandro Cortés Nieva  
**Asignatura:** Programación y Redes Virtualizadas (DRY7122)  
**Sección / Código:** 005D-05  
**Cliente:** Energía Solar Austral SA  
**Dispositivo:** RTR-ENERSOL  

---

### 1. Objetivo del proyecto
Este proyecto consistió en el diseño y la ejecución de un ciclo completo de implementación automatizada e infraestructura como código para incorporar un nuevo enrutador perimetral a la red corporativa de Energía Solar Austral SA. El objetivo principal fue asegurar un despliegue estandarizado, seguro y auditable, minimizando errores de configuración manual a través de herramientas modernas de automatización de redes.

### 2. Alcance
*   **Dentro del alcance:** Levantamiento de la línea base (baseline) del estado del router, respaldo automatizado de la configuración inicial, aprovisionamiento programático del hostname corporativo, banners de acceso, servidores de tiempo NTP, descripciones de interfaces y creación de interfaces Loopback de gestión. Además, incluye la verificación automatizada e independiente de la configuración mediante los protocolos NETCONF y RESTCONF.
*   **Fuera del alcance:** Enrutamiento dinámico avanzado, políticas de seguridad complejas (firewalling/ACLs corporativas externas) y el aprovisionamiento de interfaces físicas secundarias de la red LAN interna del cliente.

### 3. Infraestructura utilizada
*   **Estación de Trabajo:** Máquina Virtual DEVASC (Ubuntu Linux, entorno labvm).
*   **Dispositivo de Red:** Router Cisco CSR1kv (IOS-XE nativo).
*   **Protocolos y Puertos:** SSH (Puerto 22), NETCONF (Puerto 830), RESTCONF (Puerto 80/443).

### 4. Tecnologías empleadas y justificación
*   **pyATS / Genie:** Se utilizó en la Fase 1 y Fase 5 para capturar de forma agnóstica el estado operativo del hardware y generar análisis diferenciales (*diff*) que evidencien el impacto exacto de los cambios realizados.
*   **Ansible:** Elegido para la Fase 2 por su naturaleza idempotente y declarativa, permitiendo empaquetar la configuración en playbooks reproducibles e independientes de los valores fijos (*hardcoded*) mediante archivos de variables.
*   **NETCONF (ncclient):** Utilizado en la Fase 3 como protocolo de validación independiente para extraer de manera estructurada en formato XML la configuración e interactuar directamente con los modelos de datos del sistema operativo.
*   **RESTCONF (Python requests):** Implementado en la Fase 4 para verificar de manera ágil recursos específicos a través de solicitudes de API HTTP tradicionales, abstrayendo los datos en objetos JSON nativos.

### 5. Configuración aplicada
*   **Hostname:** `RTR-ENERSOL`
*   **Interfaz Loopback 10:** IP `10.5.5.1` con máscara `255.255.255.0`
*   **Descripción WAN (Gi1):** `Enlace-WAN-Antofagasta`
*   **Servidor NTP:** `1.1.1.1`
*   **Banner MOTD:** Configurado de acuerdo al estándar de restricción corporativo de Energía Solar Austral SA.

### 6. Resultados de validación
| Protocolo | Criterio Evaluado | Estado | Resultado Global |
| :--- | :--- | :--- | :--- |
| **NETCONF** | Hostname, IP Loopback, Máscara, Descripción WAN, Servidor NTP | **[OK]** | **CONFORME** |
| **RESTCONF** | Hostname, IP Loopback, Descripción WAN, Servidor NTP | **[OK]** | **CONFORME** |

### 7. Conclusiones
El enrutador corporativo `RTR-ENERSOL` fue configurado, auditado y aprobado exitosamente siguiendo estrictamente las pautas de ingeniería de la empresa. Mediante el uso combinado de Ansible, NETCONF y RESTCONF, se garantiza que la infraestructura se encuentra en un estado saludable, estandarizado y 100% listo para ser entregado al equipo de operaciones de Energía Solar Austral SA. El repositorio actual provee un historial completo y auditable de cumplimiento técnico.
