
# 📚 Programación

## 🔢 Variables

### Escalares (Primitivas)
- `int`
- `float`
- `str`
- `bool`

### No Escalares (No Primitivas)

#### Lineales

- **Estáticas**
  - Vectores
  - Matrices

- **Dinámicas**
  - Listas
  - Pilas (LIFO)
  - Colas (FIFO)

#### No Lineales

- Grafos
- Árboles

---
<br/>
## 🧠 Estructura de Memoria

```
 _________________________________________________________
|                             |                          |
|          Pila/Stack         |        Montón/Heap       |
|   (Llamadas, Parámetros)    |      (Referencias)       |
|_____________________________|__________________________|
|                             |                          |
|           Estático          |          Código          |
|        (Var Globales)       |    (Código de funciones) |
|_____________________________|__________________________|
```

---
<br/>
## 📊 Comparación visual de Pila y Montón

```
        Pila/Stack                    Pila/Stack                    Monton/Heap
(Orden uno encima del otro)     |                            (Sin un orden en particular)
         ___________            |     ___________          _________________________________
        |           |           |    |           |        |                                 |
      __|___________|__         |    |           |        |  _______                        |
     |                 |        |    |           |   |--->| |       |                       |
     |        5        | 0x40   |    |           |   |    | |   5   |_                      |
     |_________________|        |    |           |   |    | |_______| |                     |
     |                 |        |    |           |   |    |    2138   |    _______          |
     |        9        | 0x44   |    |           |   |    |           |-->|       |         |
     |_________________|        |    |___________|   |    |             __|   9   |         |
     |                 |        |    ||   ID    ||   |    |            |  |_______|         |
     |        7        | 0x48   |    ||  2344   ||   |    |            |    3128            |
     |_________________|        |    ||_________||   |    |  _______   |          _______   |
     |                 |        |    |           |   |    | |       |<-|         |       |  |
     |        8        | 0x52   |    |           |   |    | |   7   |----------->|   7   |  | 
     |_________________|        |    |           |___|    | |_______|            |_______|  |
        |           |           |    |           |        |    4444                 4444    |
        |___________|           |    |___________|        |_________________________________|
                                |                            
                                |
```
<br/>
## 🔢 Git

# git status

> verificar el estado del repositorio

# git clone NombreDelRepo

> clonar el repositorio

# git add

NombreDelArchivo

> añadir el archivo especifico al area de preparacion
> .
> añadir todos los archivos al area de preparacion

# git commit -m "primer comit"

> añadir los archivos al git local junto con un mensaje

# git log

> ver todos los commits hechos por los usuarios

# git push

> subir archivos a github (pushear)
