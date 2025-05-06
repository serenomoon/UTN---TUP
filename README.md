
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
