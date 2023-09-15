#---Ejercicio 1
# Local versus Global
# Definimos una función llamada "local"
def local():
    m = 7  # Creamos una variable local llamada "m" dentro de la función "local"
    print(m)

# Definimos una variable global llamada "m"
m = 5

# Llamamos o ejecutamos la función "local"
local()  # Dentro de la función, se imprimirá el valor de la variable local "m" (7)

# Fuera de la función, se imprimirá el valor de la variable global "m" (5)
print(m)

#---Ejercicio 2
# Local, Enclosing, y Global
def enclosing_func():
    m = 13  # Variable definida en el ámbito "enclosing" (exterior)

    def local():
        # La variable "m" no pertenece al ámbito definido por la función "local",
        # así que Python buscará en el ámbito que lo contiene (el ámbito "enclosing").
        # En este caso, "m" se encuentra en el ámbito "enclosing".
        print(m, 'imprimiendo desde el ámbito local')

    # Llamamos a la función local
    local()

    m = 5  # Cambiamos el valor de la variable "m" en el ámbito "enclosing"
    print(m, 'imprimiendo desde el ámbito global')

# Llamamos a la función "enclosing_func"
enclosing_func()

#---ejercicio 3
# Definimos la clase Bike (Bicicleta)
class Bike:
    # Constructor de la clase Bike
    def __init__(self, colour, frame_material):
        self.colour = colour  # Atributo: color de la bicicleta
        self.frame_material = frame_material  # Atributo: material del marco de la bicicleta

    # Método para frenar la bicicleta
    def brake(self):
        print("¡Frenando!")

# Creamos dos instancias (objetos) de la clase Bike
red_bike = Bike('Rojo', 'Fibra de carbono')
blue_bike = Bike('Azul', 'Acero')

# Inspeccionamos los objetos que tenemos, que son instancias de la clase Bike.
print(red_bike.colour)  # Imprime: Rojo
print(red_bike.frame_material)  # Imprime: Fibra de carbono
print(blue_bike.colour)  # Imprime: Azul
print(blue_bike.frame_material)  # Imprime: Acero

# ¡Frenamos las bicicletas!
red_bike.brake()  # Imprime: ¡Frenando!

#---ejercicio 4
str1 = 'Esto es una cadena. Lo construimos con comillas simples.'
str2 = "Esto es también una cadena, pero construida con comillas dobles."
str3 = '''Esto está construido usando comillas triples,
por lo que puede abarcar varias líneas.'''
str4 = """Esto también
es una cadena multilinea
construida con comillas triples dobles."""

# Al imprimir la cadena str4, obtenemos el resultado (A):
# 'Esto también\nes una cadena multilinea\nconstruida con comillas triples dobles.'

# Al usar la función print() con str4, obtenemos el resultado (B):
# Esto también
# es una cadena multilinea
# construida con comillas triples dobles.

#---ejercicio 5
# Abre el archivo 'fear.txt' en modo lectura de texto ('rt')
fh = open('fear.txt', 'rt')

# Itera a través de todas las líneas del archivo
for line in fh.readlines():
    # Imprime cada línea sin espacios en blanco alrededor
    print(line.strip())

# Cierra el archivo después de terminar de leerlo
fh.close()

#---ejercicio 6
from pathlib import Path

# Crea un objeto Path que representa el archivo 'fear.txt' en el directorio actual
p = Path('fear.txt')

# Obtiene la ruta absoluta del directorio que contiene 'fear.txt'
path = p.parent.absolute()

# Comprueba si 'fear.txt' es un archivo y devuelve True si lo es
print(p.is_file())  # True

# Imprime la ruta absoluta del directorio
print(path)  # /Users/fab/srv/lpp3e/ch08/files

# Comprueba si la ruta 'path' es un directorio y devuelve True si lo es
print(path.is_dir())  # True

# Crea un objeto Path que representa la ruta '/Users/fab/srv/lpp3e/ch08/files'
q = Path('/Users/fab/srv/lpp3e/ch08/files')

# Comprueba si 'q' es un directorio y devuelve True si lo es
print(q.is_dir())  # True

#---ejercicio 7
import shutil
from pathlib import Path

# Se crea un objeto Path llamado 'base_path' que representa un directorio llamado 'ops_example'
base_path = Path('ops_example')

# Realiza una limpieza inicial para asegurarse de que 'base_path' no exista previamente como un directorio.
if base_path.exists() and base_path.is_dir():
    shutil.rmtree(base_path)  # Elimina 'base_path' y su contenido si ya existe.

# Crea el directorio 'ops_example' si no existe.
base_path.mkdir()

# Crea tres objetos Path que representan directorios dentro de 'ops_example':
path_b = base_path / 'A' / 'B'
path_c = base_path / 'A' / 'C'
path_d = base_path / 'A' / 'D'

# Crea el directorio 'B' y sus directorios padres ('A') si no existen.
path_b.mkdir(parents=True)

# Crea el directorio 'C' si no existe. No es necesario especificar 'parents=True' aquí, ya que 'A' ya ha sido creado.
path_c.mkdir()

# Agrega tres archivos dentro del directorio 'B' ('ops_example/A/B').
for filename in ('ex1.txt', 'ex2.txt', 'ex3.txt'):
    with open(path_b / filename, 'w') as stream:
        stream.write(f'Some content here in {filename}\n')

# Mueve el contenido del directorio 'B' ('ops_example/A/B') al directorio 'D' ('ops_example/A/D').
shutil.move(path_b, path_d)

# También renombra el archivo 'ex1.txt' a 'ex1.renamed.txt' dentro del directorio 'D'.
ex1 = path_d / 'ex1.txt'
ex1.rename(ex1.parent / 'ex1.renamed.txt')

#---ejercicio 8
from pathlib import Path

# Crea un objeto Path llamado 'p' que representa el archivo 'fear.txt' en el directorio actual.
p = Path('fear.txt')

# Imprime la ruta absoluta del archivo 'fear.txt'.
print(p.absolute())  # Salida: Ruta absoluta de 'fear.txt'

# Imprime el nombre del archivo 'fear.txt'.
print(p.name)  # Salida: fear.txt

# Imprime la ruta absoluta del directorio que contiene 'fear.txt'.
print(p.parent.absolute())  # Salida: Ruta absoluta del directorio que contiene 'fear.txt'

# Imprime la extensión del archivo 'fear.txt' (si la tiene).
print(p.suffix)  # Salida: extensión del archivo (por ejemplo, '.txt')

# Imprime una tupla que contiene las partes de la ruta del archivo 'fear.txt'.
print(p.parts)  # Salida: Tupla con las partes de la ruta

# Imprime una tupla que contiene las partes de la ruta absoluta del archivo 'fear.txt'.
print(p.absolute().parts)  # Salida: Tupla con las partes de la ruta absoluta

# Crea un objeto Path llamado 'readme_path' que representa una ruta que sube dos niveles desde el directorio que contiene 'fear.txt' y luego apunta a 'README.rst'.
readme_path = p.parent / '..' / '..' / 'README.rst'

# Imprime la ruta absoluta de 'readme_path'.
print(readme_path.absolute())  # Salida: Ruta absoluta de 'README.rst'

# Resuelve 'readme_path' para obtener su ruta absoluta completa.
print(readme_path.resolve())  # Salida: Ruta absoluta completa de 'README.rst'

#---ejercicio 9
from tempfile import NamedTemporaryFile, TemporaryDirectory

# Crea un directorio temporal (temporario) en el directorio actual.
# El directorio se eliminará automáticamente cuando salgas del bloque 'with'.
with TemporaryDirectory(dir='.') as td:
    print('Temp directory:', td)  # Imprime el nombre del directorio temporal.

    # Crea un archivo temporal en el directorio temporal 'td'.
    # El archivo se eliminará automáticamente cuando salgas del bloque 'with'.
    with NamedTemporaryFile(dir=td) as t:
        name = t.name  # Obtiene el nombre del archivo temporal.
        print(name)  # Imprime el nombre del archivo temporal.

#---ejercicio 10
from zipfile import ZipFile

# Crea un archivo ZIP llamado 'example.zip' en modo escritura ('w').
with ZipFile('example.zip', 'w') as zp:
    # Agrega 'content1.txt' al archivo ZIP 'example.zip'.
    zp.write('content1.txt')
    # Agrega 'content2.txt' al archivo ZIP 'example.zip'.
    zp.write('content2.txt')
    # Agrega 'subfolder/content3.txt' al archivo ZIP 'example.zip'.
    zp.write('subfolder/content3.txt')
    # Agrega 'subfolder/content4.txt' al archivo ZIP 'example.zip'.
    zp.write('subfolder/content4.txt')

# Abre el archivo ZIP 'example.zip' en modo lectura ('r').
with ZipFile('example.zip') as zp:
    # Extrae 'content1.txt' del archivo ZIP 'example.zip' y lo coloca en la carpeta 'extract_zip'.
    zp.extract('content1.txt', 'extract_zip')
    # Extrae 'subfolder/content3.txt' del archivo ZIP 'example.zip' y lo coloca en la carpeta 'extract_zip'.
    zp.extract('subfolder/content3.txt', 'extract_zip')



