import os
import shutil
from pathlib import Path

print('URL desde donde se ejecuta el programa:', os.getcwd())
os.chdir("C:\\Users\\amaci\\Documents\\EJERCICIO_LECTURA")
print ('PATH de mi carpeta de prueba: ', os.getcwd())
print ('Lista de documentos: ', os.listdir())

# Ruta a la que queremos llevar los documentos
base_dir = Path(r"C:\\Users\\amaci\\Documents\\EJERCICIO_LECTURA")

# Qué documentos va a llevar cada subcarpeta
subdirs = {
    "Imagenes": ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    "Documentos": ['.txt', '.pdf', '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.csv'],
    "Software": ['.exe', '.msi', '.apk', '.sh', '.bat', '.py', '.zip', '.rar'],
    "Otros": []  
}
# Que las cree si no existen
for folder in ['Imagenes', 'Documentos', 'Software', 'Otros']:
    (base_dir / folder).mkdir(exist_ok=True)
    
# Bucle para meter los archivos
for archivo in base_dir.iterdir():
    if archivo.is_file():
        ext = archivo.suffix.lower()
        # Buscar categoría del archivo
        destino = None
        for carpeta, extensiones in subdirs.items():
            if ext in extensiones:
                destino = carpeta
                break
        if not destino:
            destino = 'Otros'
        # Mover el archivo
        shutil.move(str(archivo), str(base_dir / destino / archivo.name))
        
print(":marca_de_verificación_blanca: Archivos organizados correctamente en C:\\Users\\amaci\\Documents\\EJERCICIO_LECTURA")