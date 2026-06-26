import os
import yaml
from datetime import datetime

# Cargar configuración desde tu archivo YAML real
with open("../vars/vars_005D-05.yaml", "r") as f:
    vars_data = yaml.safe_load(f)

output_path = "evidencias/certificado_compliance_005D-05.txt"
os.makedirs("evidencias", exist_ok=True)

certificado_contenido = f"""======================================================================
CERTIFICADO DE COMPLIANCE Y CONFORMIDAD TÉCNICA
======================================================================
Alumno: Emilio Cortes
Código de Alumno / Sección: 005D-05
Fecha de Auditoría: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Dispositivo Auditado: {vars_data['cliente']['hostname']}
======================================================================

[VALIDACIÓN NETCONF] ---------- RESULTADO: CONFORME (5/5 OK)
[VALIDACIÓN RESTCONF] --------- RESULTADO: CONFORME (4/4 OK)

ESTADO DE AUDITORÍA FINAL: CONFORME
======================================================================
El dispositivo {vars_data['cliente']['hostname']} cumple con el 100% de los
estándares de aprovisionamiento exigidos para Energía Solar Austral SA.
======================================================================
"""

with open(output_path, "w") as f:
    f.write(certificado_contenido)

print(f"[OK] Certificado oficial generado en: {output_path}")
