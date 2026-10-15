# AP 22 · Comprobador de congruencias

El programa pide dos números enteros `a` y `b` y un módulo positivo `n`.
Comprueba si `a ≡ b (mod n)`, es decir, si `a - b` es divisible por `n`.
También muestra el resto de dividir cada número entre el módulo.

## Ejecutarlo en VS Code

Abre esta carpeta en VS Code. En **Terminal → Nuevo terminal**, ejecuta:

```powershell
py .\comprobador_congruencia.py
```

Ejemplo: con `17`, `5` y `12`, ambos restos son `5`, así que los números son congruentes. Con `17`, `6` y `12`, los restos son distintos y no lo son.

Si escribes texto donde se espera un entero o un módulo igual o menor que cero, el programa vuelve a pedir ese dato.
