# Barcode Validator

Sistema de validación en tiempo real para procesos de reetiquetado e ingreso de mercancía en centros de distribución. Diseñado para mitigar el error humano en la manipulación de productos de cosmética, perfumería y cuidado personal con SKUs de alta similitud (*look-alike SKUs*).

---

## Módulos y Arquitectura del Proyecto

El sistema utiliza captura de video en vivo para extraer, decodificar y auditar códigos de barras (EAN-13, UPC, Code 128) frente a las reglas de negocio predefinidas.

[ Cámara / Stream Video ]
│
▼
[ Decodificación de Píxeles (OpenCV + pyzbar) ]
│
▼
[ Verificación en Reglas de Negocio (database.py) ]
│
┌────────┴────────┐
▼                 ▼
[ Match / OK ]   [ Error / Desconocido ]
(Cuadro Verde)   (Cuadro Rojo)


---

## Capturas de Pantalla / Demostración

| Escaneo Exitoso (Match) | Código No Autorizado / Error |
| :---: | :---: |
| ![Escaneo Exitoso](docs/screenshots/scan_ok.png) | ![Error de Escaneo](docs/screenshots/scan_error.png) |

> *Nota: Colocar las capturas de pantalla en la ruta `docs/screenshots/`.*

---

## Requisitos del Sistema

### Sistema Operativo
* Linux (probado en Fedora Linux) / macOS / Windows

### Dependencias de Sistema (Fedora Linux)
Es necesario instalar la biblioteca nativa `zbar` para la decodificación de patrones de código de barras a nivel de C:

```bash
sudo dnf install zbar
Entorno de Software
Python 3.10 o superior

opencv-python >= 4.8.0

pyzbar >= 0.1.9

numpy >= 1.24.0

Instalación y Configuración
Clonar el repositorio:

Bash
git clone [https://github.com/TU_USUARIO/barcode-validator.git](https://github.com/TU_USUARIO/barcode-validator.git)
cd barcode-validator
Crear y activar el entorno virtual:

Bash
python3 -m venv venv
source venv/bin/activate
Instalar dependencias de Python:

Bash
pip install --upgrade pip
pip install -r requirements.txt
Estructura del Proyecto
Plaintext
barcode-validator/
├── README.md
├── requirements.txt
├── .gitignore
├── docs/
│   └── screenshots/
└── src/
    ├── database.py       # Definición de reglas de negocio y mapeo de SKUs
    └── scanner.py        # Captura de video, procesamiento de frames y renderizado
Uso
Para iniciar el sistema de escaneo con la cámara predeterminada (/dev/video0):

Bash
python src/scanner.py
Presione la tecla q dentro de la ventana de video para finalizar la ejecución.

Hoja de Ruta (Roadmap)
[x] Prototipo funcional de decodificación en tiempo real (OpenCV + pyzbar).

[x] Mapeo básico de reglas de validación local.

[ ] Integración de interfaz web interactiva (FastAPI + WebSockets).

[ ] Implementación de alertas audibles para operarios.

[ ] Soporte para cámaras IP y dispositivos móviles vía RTSP/HTTP.

[ ] Módulo OCR (PaddleOCR/EasyOCR) para validación de texto de empaque.

[ ] Persistencia de eventos de lectura en base de datos PostgreSQL.

Contribución
Haga un Fork del proyecto.

Cree una rama para su funcionalidad (git checkout -b feature/nueva-funcionalidad).

Realice sus cambios y confirme los commits (git commit -m 'Add: nueva funcionalidad').

Envíe los cambios a su rama (git push origin feature/nueva-funcionalidad).

Abra un Pull Request.

Licencia
Este proyecto está bajo la Licencia MIT.
EOF