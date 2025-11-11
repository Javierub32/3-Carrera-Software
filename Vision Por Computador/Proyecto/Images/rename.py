import os

# carpeta donde está este script (Images)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# subcarpetas que quieres procesar
subcarpetas = ["English", "Japanese", "Multiple", "Final"]

for carpeta in subcarpetas:
    ruta_carpeta = os.path.join(BASE_DIR, carpeta)
    if not os.path.isdir(ruta_carpeta):
        continue  # por si alguna no existe

    contador = 1
    # listamos solo archivos
    for nombre in sorted(os.listdir(ruta_carpeta)):
        ruta_vieja = os.path.join(ruta_carpeta, nombre)

        # saltar si no es archivo o no es .jpg
        if not os.path.isfile(ruta_vieja):
            continue
        if not nombre.lower().endswith(".jpg"):
            continue

        nuevo_nombre = f"{carpeta}_{contador}.jpg"
        ruta_nueva = os.path.join(ruta_carpeta, nuevo_nombre)

        # por si ya existe ese nombre (muy raro), avanza contador
        while os.path.exists(ruta_nueva):
            contador += 1
            nuevo_nombre = f"{carpeta}_{contador}.jpg"
            ruta_nueva = os.path.join(ruta_carpeta, nuevo_nombre)

        os.rename(ruta_vieja, ruta_nueva)
        contador += 1
