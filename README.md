# MediverseBack

## Configuración del archivo `.env`

Crea un archivo llamado `.env` en la raíz del proyecto con el siguiente contenido:

```
MONGO_URI=******
ENV=dev  # Usa "prod" para producción o "dev" para desarrollo
FrontendOrigin=ttps://mediverse-3d.vercel.app  # Solo necesario si ENV=prod
```

- `MONGO_URI`: Cadena de conexión a tu base de datos MongoDB.
- `ENV`: Define el entorno de ejecución. Usa `dev` para desarrollo (CORS abierto) o `prod` para producción (CORS restringido).
- `FrontendOrigin`: (Solo producción) URL permitida para peticiones desde el frontend.

## Pasos para ejecutar el proyecto en local

1. **Clona el repositorio y entra a la carpeta del proyecto**

2. **Crea y activa un entorno virtual (opcional pero recomendado):**

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Instala las dependencias:**

   ```powershell
   pip install -r requirements.txt
   ```

4. **Configura el archivo `.env`** (ver ejemplo arriba).

5. **Ejecuta la aplicación:**

   ```powershell
   python app.py
   ```

6. La API estará disponible en: http://localhost:5000

---


