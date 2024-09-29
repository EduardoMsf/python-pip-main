# Crear y usar entornos virtuales en Python


## Crear un entorno virtual

Para crear un entorno virtual, sigue los siguientes pasos:

1. Navega al directorio donde deseas crear el entorno virtual.
2. Ejecuta el siguiente comando para crear un entorno virtual llamado `venv`:

```bash
git clone
cd python-pip
```

3. Muevete al directorio deseado y crea el entorno virtual utilizando el siguiente comando:

```bash
cd [directorio] 
python3 -m venv [directorio]
```

4. Activa el entorno virtual utilizando el siguiente comando:

```bash
source [directorio]/bin/activate
```

5. Instala las dependencias necesarias utilizando el siguiente comando:

```bash
pip install -r requirements.txt
```

Si prefieres utilizar Conda, puedes seguir los siguientes pasos:

1. Para crear un nuevo ambiente virtual con conda, usa el siguiente comando. Puedes reemplazar myenv con el nombre que prefieras para tu ambiente. Crea un nuevo ambiente virtual utilizando el siguiente comando:

```bash
conda create --name myenv
```

2. Activa el ambiente virtual utilizando el siguiente comando:

```bash
conda activate myenv
```

3. Instala los paquetes necesarios en el ambiente virtual. Por ejemplo, para instalar NumPy y pandas, utiliza el siguiente comando:

```bash
conda install numpy pandas
```

4. Exporta las instalaciones del ambiente a un archivo .yml utilizando el siguiente comando:

```bash
conda env export > environment.yml
```

5. Desactiva el ambiente virtual utilizando el siguiente comando:

```bash
conda deactivate
```

Recuerda que puedes reemplazar los nombres de los directorios y ambientes virtuales según tus preferencias.