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

#### Apéndice A

El lenguaje de programación escogido es C++.

##### Estructuras de control de flujo

C++ ofrece las siguientes estructuras de control de flujo

- **Secuenciales**: Las instrucciones se ejecutan en el orden en que aparecen.
- **Selección**: Permite ejecutar un bloque de instrucciones si se cumple una condición.
  - `if`: Permite ejecutar un bloque de instrucciones si se cumple una condición.
  - `if-else`: Permite ejecutar un bloque de instrucciones si se cumple una condición y otro bloque si no se cumple.
  - `switch`: Permite ejecutar un bloque de instrucciones dependiendo del valor de una variable.
  - `?:`: Operador ternario que permite ejecutar un bloque de instrucciones si se cumple una condición y otro si no se cumple.
  - `if constexpr`: Permite ejecutar un bloque de instrucciones si se cumple una condición en tiempo de compilación.
  - `if constexpr-else`: Permite ejecutar un bloque de instrucciones si se cumple una condición en tiempo de compilación y otro si no se cumple.
  - `switch constexpr`: Permite ejecutar un bloque de instrucciones dependiendo del valor de una variable en tiempo de compilación.
  - `?: constexpr`: Operador ternario que permite ejecutar un bloque de instrucciones si se cumple una condición en tiempo de compilación y otro si no se cumple.
- **Iteración**: Permite ejecutar un bloque de instrucciones repetidamente.
  - `for`: Permite ejecutar un bloque de instrucciones un número determinado de veces.
  - `while`: Permite ejecutar un bloque de instrucciones mientras se cumpla una condición.
  - `do-while`: Permite ejecutar un bloque de instrucciones al menos una vez y luego mientras se cumpla una condición.
  - `for-range`: Permite iterar sobre un rango de valores.
  - `for-range constexpr`: Permite iterar sobre un rango de valores en tiempo de compilación.
  - `for-range-ref`: Permite iterar sobre un rango de valores por referencia.
- **Transferencia de control**: Permite cambiar el flujo de ejecución de un programa.
  - `break`: Permite salir de un bucle.
  - `continue`: Permite saltar a la siguiente iteración de un bucle.
  - `goto`: Permite saltar a una etiqueta en el código.
  - `return`: Permite salir de una función y devolver un valor.
  - `throw`: Permite lanzar una excepción.
  - `try-catch`: Permite capturar una excepción y manejarla.
  - `try-catch-else`: Permite capturar una excepción y manejarla si se lanza.
  - `try-catch-finally`: Permite capturar una excepción y manejarla y ejecutar un bloque de instrucciones al final.

##### Evaluación de expresiones y funciones

Particularmente, C++ tiene evaluación normal y aplicativa. Ademas, la evaluación de argumentos/operandos se hace de izquierda a derecha. C++ no tiene evaluación perezosa, por lo que todos los argumentos de una función se evalúan antes de llamar a la función. De igual forma, las expresiones se evalúan de izquierda a derecha en el orden en que aparecen a la hora de revisar una condición, y pese a que el resultado sea definitivo, se sigue evaluando el resto de la expresión.

Adicionalmente, C++ permite la sobrecarga de operadores, lo que permite definir el comportamiento de los operadores para tipos de datos personalizados.

#### Apéndice B

Para ejecutar el programa, se debe correr el siguiente comando:

```bash
./main exe1-b <n> 
```

Donde `<n>` es el número entero que se desea evaluar.

#### Apéndice C

Para ejecutar el programa, se debe correr el siguiente comando:

```bash
./main exe1-c <n1> <n2> <n3> ... <n>
```

Donde `<n1> <n2> <n3> ... <n>` son los números enteros que se desean ordenar.

##### Implementación

El algoritmo Mergesort es un algoritmo de ordenamiento que sigue la estrategia de divide y vencerás. Consiste en dividir la lista en dos mitades, ordenar cada mitad y luego combinar las dos mitades ordenadas. La implementación del algoritmo Mergesort en C++ es la siguiente:

```cpp
void merge(int arr[], int l, int m, int r){
    // Get the sizes of the two arrays
    int n1 = m - l + 1;
    int n2 = r - m;

    int L[n1], R[n2];

    // Copy the data to the two arrays
    for (int i = 0; i < n1; i++){
        L[i] = arr[l + i];
    }

    for (int i = 0; i < n2; i++){
        R[i] = arr[m + 1 + i];
    }

    int i = 0;
    int j = 0;
    int k = l;

    // Merge the two arrays
    while (i < n1 && j < n2){
        if (L[i] <= R[j]){
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of L[] and R[]
    while (i < n1){
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2){
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int l, int r){
    // If the left index is greater or equal to the right index, return
    if (l >= r){
        return;
    }

    // Get the middle index
    int m = l + (r - l) / 2;
    // Sort the two halves
    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);
    // Merge the two halves
    merge(arr, l, m, r);
}
```

Se puede ver que el algoritmo Mergesort se divide en dos funciones: `merge` y `mergeSort`. La función `merge` se encarga de combinar dos arreglos ordenados en uno solo, mientras que la función `mergeSort` se encarga de dividir el arreglo en dos mitades, ordenar cada mitad y luego combinarlas.

Tomé la decisión de implementar el algoritmo Mergesort de esta forma para separar la lógica de combinar dos arreglos ordenados de la lógica de dividir el arreglo en dos mitades y ordenarlas. De esta forma, se puede reutilizar la función `merge` en otros algoritmos de ordenamiento que requieran combinar dos arreglos ordenados.

Adicionalmente, por simplicidad, decidí utilizar arreglos de tamaño fijo para almacenar los elementos de los dos arreglos que se van a combinar. Esto se debe a que el tamaño de los arreglos es conocido y no cambia durante la ejecución del programa. Además, crear subarreglos de tamaño fijo en la pila es más eficiente que utilizar memoria dinámica en este caso.

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
  - `EVAL POST 8 3 - 8 4 4 + * +` deberá imprimir `69`.
  
- `MOSTRAR <orden> <expr>`: Representa una impresión en orden in–fijo de la expresión en `<expr>`, que está escrita de acuerdo a `<orden>`.
  
  El <orden> sigue el mismo patrón que en el punto anterior. Su programa debe tomar la precedencia y asociatividad estándar, donde:
  
  - La suma y la resta tienen la misma precedencia. 
  - La multiplicación y la división entera tienen la misma precedencia. 
  - La multiplicación y la división entera tienen mayor precedencia que la suma y la resta. 
  - Todos los operadores asocian a izquierda.
  
  La expresión resultante debe tener la menor cantidad posible de paréntesis, de tal forma que la expresión mostrada como resultado tenga la misma semántica que la expresión que fue pasada como argumento a la acción. Por ejemplo: 
    
  - `MOSTRAR PRE + * + 3 4 5 7` deberá imprimir (3 + 4) * 5 + 7. 

  - `MOSTRAR POST 8 3 - 8 4 4 + * +` deberá imprimir 8 - 3 + 8 * (4 + 4).
  
- `SALIR`: Debe salir del programa. 

Al finalizar la ejecución de cada acción, el programa deberá pedir la siguiente acción al usuario. 

Investigue herramientas para pruebas unitarias y cobertura en su lenguaje escogido y agregue pruebas a su programa que permitan corroborar su correcto funcionamiento. Como regla general, su programa debería tener una cobertura (de líneas de código y de bifuración) mayor al 80%.

### Respuesta

Para ejecutar el programa, se debe correr el siguiente comando:

```bash
./main exe2
```

<!-- TODO: Realizar la pruebas -->

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