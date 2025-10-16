# 🚀 Integración de Flask, Redis y MongoDB

Este proyecto muestra cómo integrar **Flask** (como servidor web), **Redis** (como sistema de caché) y **MongoDB** (como base de datos principal).  
La arquitectura permite optimizar las consultas a la base de datos utilizando Redis como almacenamiento temporal.

---

## 🧰 Tecnologías utilizadas

- **Flask** → Framework web en Python.  
- **Redis** → Sistema de caché en memoria.  
- **MongoDB** → Base de datos NoSQL.  
- **PyMongo** → Cliente para conectarse a MongoDB.  
- **Redis-py** → Cliente Python para Redis.  
- **Docker (opcional)** → Para levantar Mongo y Redis rápidamente.

---

## ⚙️ Requisitos previos

- Python 3.9 o superior  
- Redis y MongoDB instalados o ejecutándose en contenedores Docker  
- pip actualizado

---

## 🧪 Instalación paso a paso

### 1️⃣ Crear entorno virtual

```bash
python -m venv venv

venv\Scripts\activate
source venv/bin/activate #linux

pip install flask pymongo redis

pip freeze > requirements.txt

flask run

