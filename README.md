# Tarea 2 - CI3641 (Septiembre - Diciembre 2024)

**Hecho por**: Juan Cuevas _19-10056_

## Pregunta 1

Escoja algún lenguaje de programación de alto nivel y de propósito general cuyo nombre empiece con la misma letra que su apellido (por ejemplo, si su apellido es “Rodríguez”, podría escoger “Ruby”, “Rust”, “R”, etc.).

### Apéndice A

De una breve descripción del lenguaje escogido.

- Enumere y explique las estructuras de control de flujo que ofrece.
- Diga en qué orden evalúan expresiones y funciones.
  - ¿Tiene evaluación normal o aplicativa? ¿Tiene evaluación perezosa?
  - La evaluación de argumentos/operandos se hace de izquierda a derecha, de derecha a izquierda o en un orden arbitrario.

### Apéndice B

Implemente los siguientes programas en el lenguaje escogido:

- Considere la siguiente función:

  $$ f(n) = \begin{cases} n/2 & \text{si n es par} \\ 3n + 1 & \text{si n es impar} \end{cases} $$

  Definimos la función $\text{count}(n)$ como la cantidad de aplicaciones consectuvias de $f$ que se deben hacer sobre $n$, hasta que el resultado sea $1$.

  Por ejemplo: 
  $$f(42) = 21$$ 
  $$f(21) = 64$$
  $$f(64) = 32$$
  $$f(32) = 16$$
  $$f(16) = 8$$
  $$f(8) = 4$$
  $$f(4) = 2$$
  $$f(2) = 1$$
  
  Por lo tanto, $\text{count}(42) = 8$.

  Escriba un programa que, dado un entero $n$, calcule $\text{count}(n)$.

- Implemente el algoritmo Mergesort y explique los detalles de su implementación. 

  _Nota: Explicar los detalles no implica traducir línea por linea a lenguaje natural, sino explicar el funcionamiento a grandes rasgos y las decisiones de implementación._

### Respuesta

<!-- TODO -->

## Pregunta 2

Se desea que modele e implemente, en el lenguaje de su elección, un programa que maneje expresiones aritmáticas sobre enteros. Este programa debe cumplir con las siguientes características:

### Apéndice A

Debe saber tratar expresiones escritas en orden pre–fijo y post–fijo, con los siguientes operadores: 
- suma: Representada por el símbolo $+$. 
- resta: Representada por el símbolo $-$. 
- multiplicación: Representada por el símbolo $*$. 
- división entera: Representada por el símbolo $/$.

### Apéndice B

Una vez iniciado el programa, pedirá repetidamente al usuario una acción para proceder. Tal acción puede ser:

- `EVAL <orden> <expr>`: Representa una evaluación de la expresión en `<expr>`, que está escrita de acuerdo a `<orden>`.
  
  El orden solamente puede ser:
  - `PRE`: Que representa expresiones escritas en orden pre–fijo. 
  - `POST`: Que representa expresiones escritas en orden post–fijo.
  
  Por ejemplo:
  - `EVAL PRE + * + 3 4 5 7` deberá imprimir `42`. 
  - `EVAL POST 8 3- 8 4 4 + * +` deberá imprimir `69`.
  
- `MOSTRAR <orden> <expr>`: Representa una impresión en orden in–fijo de la expresión en `<expr>`, que está escrita de acuerdo a `<orden>`.
  
  El <orden> sigue el mismo patrón que en el punto anterior. Su programa debe tomar la precedencia y asociatividad estándar, donde:
  
  - La suma y la resta tienen la misma precedencia. 
  - La multiplicación y la división entera tienen la misma precedencia. 
  - La multiplicación y la división entera tienen mayor precedencia que la suma y la resta. 
  - Todos los operadores asocian a izquierda.
  
  La expresión resultante debe tener la menor cantidad posible de paréntesis, de tal forma que la expresión mostrada como resultado tenga la misma semántica que la expresión que fue pasada como argumento a la acción. Por ejemplo: 
    
  - `MOSTRAR PRE + * + 3 4 5 7` deberá imprimir (3 + 4) * 5 + 7. 

  - `MOSTRAR POST 8 3- 8 4 4 + * +` deberá imprimir 8- 3 + 8 * (4 + 4).
  
- `SALIR`: Debe salir del programa. 

Al finalizar la ejecución de cada acción, el programa deberá pedir la siguiente acción al usuario. 

Investigue herramientas para pruebas unitarias y cobertura en su lenguaje escogido y agregue pruebas a su programa que permitan corroborar su correcto funcionamiento. Como regla general, su programa debería tener una cobertura (de líneas de código y de bifuración) mayor al 80%.

### Respuesta

<!-- TODO -->

## Pregunta 3

Considere los siguientes iteradores, escritos en Python: 

### Apéndice A

El iterador suspenso: 

```python
def suspenso(a, b): 
    if b == []: 
        yield a 
    else: 
        yield a + b[0] 
        for x in suspenso(b[0], b[1:]): 
            yield x 
```

Tomando como referencia las constantes X, Y y Z planteadas en los párrafos de introducción del examen, considere también el siguiente fragmento de código que hace uso del iterador suspenso:

```python
for x in suspenso(X + Y + Z, [X, Y, Z]): 
    print x 
```

Ejecute, paso a paso, el fragmento de código mostrado (por lo menos al nivel de cada nuevo marco de pila creado) y muestre lo que imprime.

### Apéndice B

El iterador misterio: 

```python
def misterio(n):
    if n == 0: 
        yield [1] 
    else: 
        for x in misterio(n-1): 
            r = [] 
            for y in suspenso(0, x): 
                r = [*r, y] 
            yield r
```

Considere también el siguiente fragmento de código que hace uso del iterador misterio: 

```python
for x in misterio(5): 
    print x 
```

Ejecute, paso a paso, el fragmento de código mostrado (por lo menos al nivel de cada nuevo marco de pila creado) y muestre lo que imprime. 

_Nota: cómo ya conocemos el comportamiento del iterador suspenso no es necesario mostrar los pasos internos en el ciclo interno de misterio._

### Apéndice C

Dada una lista de enteros, queremos un iterador que devuelva todos los elementos de la lista en orden (de menor a mayor). 

Por ejemplo, para la lista `[1,3,3,2,1]`, los elementos en orden serían: 

`1 1 2 3 3` 

Implemente este iterador en el lenguaje de su preferencia. 

_Nota: el ordenamiento debe ser parte de la lógica del iterador. No es válido ordenar primero la lista y luego devolver los elementos de la lista previamente ordenada._

### Respuesta

<!-- TODO -->

## Pregunta 4

Considere la siguiente definición para una familia de funciones:

$$ F_{\alpha, \beta}(n) = \begin{cases} n & \text{si } 0 \leq n < \alpha \times \beta \\ \sum_{i=1}^{\alpha} F_{\alpha, \beta}(n - \beta \times i) & \text{si } n \geq \alpha \times \beta \end{cases} $$

Tomando como referencia las constantes X, Y y Z planteadas en los párrafos de introducción del examen, definamos: 
- $\alpha = ((X + Y) \text{ mod } 5) + 3$ 
- $\beta = ((Y + Z) \text{ mod } 5) + 3$

Se desea que realice implementaciones, en el lenguaje imperativo de su elección:

### Apéndice A

Una subrutina recursiva que calcule $F_{\alpha, \beta}$ para los valores de $\alpha$ y $\beta$ obtenidos con las fórmulas mencionadas anteriormente. Esta implementación debe ser una traducción directa de la fórmula resultante a código.

### Apéndice B

Una subrutina recursiva de cola que calcule $F_{\alpha, \beta}$.

### Apéndice C

La conversión de la subrutina anterior a una versión iterativa, mostrando claramente cuáles componentes de la implementación recursiva corresponden a cuáles otras de la implementación iterativa.

Debe usar el mismo el lenguaje para estos tres ejercicios y asegurarse que su lenguaje tenga las estructuras de control de flujo necesarias para realizarlos (su lenguaje escogido debe, por tanto, ser imperativo). 

Realice también un análisis comparativo entre las tres implementaciones realizadas, mostrando tiempos de ejecución para diversos valores de entrada y ofreciendo conclusiones sobre la eficiencia. Es recomendable que se apoye en herramientas de visualización de datos (como los plots de Matlab, R, Octave, Excel, etc.)

### Respuesta

<!-- TODO -->

## Pregunta 5

Considere la misma función maldad, definida en el parcial anterior:

$$\text{maldad}(n) = trib(\lfloor \log_2(N(n, \lfloor \log_2(n) \rfloor)) \rfloor + )$$

Decimos que unprogramaes políglota si el mismo código fuente puede ser compilado/interpretado por al menos dos diferentes lenguajes de programación. 

Desarrolle un programa políglota que: 

- Reciba por entrada estándar o argumento del sistema un valor para n, tal que $n \geq 2$ (esto puede suponerlo, no tiene que comprobarlo). Debe indicar en su informe claramente si su reto recibe la entrada vía entrada estándar o argumento del sistema.  
- Imprima el valor de $\text{maldad}(n)$. 
 
Su programa debe imprimir el valor correcto y tomando menos de 1 segundo de ejecución, por lo menos hasta $n = 50$ en todos los lenguajes de programación considerados.

### Respuesta

<!-- TODO -->