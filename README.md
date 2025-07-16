##API que genera un codigo QR y lo codifica en base64.
Tiene un endpoint POST /generate_qr que recibe por body (json) un texto.
Ese texto lo convierte a imagen QR y lo codifica en base64 y se lo devuelve al cliente

###Documentacion
	FastAPI: https://fastapi.tiangolo.com/es/

###Crear entorno virtual para las dependencias
	```python -m venv venv```

###Activar entorno virtual
	```.\venv\Scripts\activate```

###Instalar dependencias
	```pip install -r requirements.txt```

###Levantar local
	```fastapi dev main.py```

###Levantar en servidor
	```uvicorn main:app --host 0.0.0.0 --port 8000 --workers 1 (cantidad de nucleos)
