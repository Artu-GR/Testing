FROM fedora:latest

# Instalación de Python, pip y herramientas necesarias para el desarrollo
RUN dnf -y install python3 python3-pip \
    && dnf -y install gcc gcc-c++ make \
    && dnf -y install mariadb-devel \
    && dnf -y install libjpeg-devel zlib-devel \
    && dnf -y install python3-devel \
    && dnf clean all
  
RUN dnf install -y nc
RUN pip install --upgrade pip setuptools wheel
RUN pip install mysqlclient

# Establece el directorio de trabajo
WORKDIR /app


# Copia los archivos de requirements.txt al contenedor
COPY requirements.txt /app/

RUN pip install --no-cache-dir Pillow
RUN pip install --no-cache-dir -r requirements.txt


# Copia el resto de los archivos de la aplicación
COPY . /app/

# Expone el puerto 8000 para la aplicación
EXPOSE 8000

# Configura el entorno para evitar el buffering de los logs
ENV PYTHONUNBUFFERED=1

# Comando para ejecutar la aplicación Django
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

