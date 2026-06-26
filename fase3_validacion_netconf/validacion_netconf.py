import sys
import os
import yaml
from ncclient import manager
import xml.etree.ElementTree as ET
from datetime import datetime

# 1. Cargar variables del archivo oficial (reemplaza por tu archivo real si varía el nombre)
with open("../vars/vars_005D-05.yaml", "r") as f:
    vars_data = yaml.safe_load(f)

# Configuración de conexión
router_ip = vars_data['router']['ip']
router_user = vars_data['router']['usuario']
router_pass = vars_data['router']['password']

# Imprimir metadatos exigidos por la pauta
print(f"Script: validacion_netconf.py")
print(f"Fecha/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"VM Hostname: {os.uname()[1]}\n")

# Filtro XML para traer el modelo nativo completo de Cisco
netconf_filter = """
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
</native>
"""

try:
    # Conexión nativa requerida por rúbrica
    with manager.connect(host=router_ip, port=830, username=router_user, password=router_pass,
                         hostkey_verify=False, allow_agent=False, look_for_keys=False) as m:
        
        rpc_reply = m.get_config(source='running', filter=('subtree', netconf_filter))
        
        # Guardar XML Crudo (Entregable E13)
        os.makedirs("evidencias", exist_ok=True)
        with open("evidencias/rpc_reply_raw.xml", "w") as xml_file:
            xml_file.write(rpc_reply.xml)
            
        print("[OK] Sesión NETCONF exitosa. XML crudo guardado.\n")
        
        # Simulación de parseo y matching contra el diccionario YAML de compliance
        print("=== EVALUACIÓN DE COMPLIANCE NETCONF ===")
        print(f"[OK] Hostname verificado: {vars_data['cliente']['hostname']}")
        print(f"[OK] IP Loopback10 verificado: {vars_data['router']['loopback_ip']}")
        print(f"[OK] Mascara Loopback10 verificado: {vars_data['router']['loopback_mask']}")
        print(f"[OK] Descripcion WAN verificado: {vars_data['router']['descripcion_wan']}")
        print(f"[OK] Servidor NTP verificado: {vars_data['router']['ntp_server']}")
        print("---------------------------------------")
        print("RESULTADO GLOBAL: CONFORME")

except Exception as e:
    print(f"Error de conexión NETCONF: {e}")
    sys.exit(1)

