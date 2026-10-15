"""AP 22: comprobar si dos enteros son congruentes módulo un tercero."""


def son_congruentes(a: int, b: int, modulo: int) -> bool:
    """Devuelve True si a ≡ b (mod modulo)."""
    if modulo <= 0:
        raise ValueError("El módulo debe ser un entero positivo.")
    return (a - b) % modulo == 0


def pedir_entero(mensaje: str, *, positivo: bool = False) -> int:
    """Solicita un entero hasta recibir una entrada válida."""
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Entrada no válida. Escribe un número entero.")
            continue

        if positivo and valor <= 0:
            print("El módulo debe ser un entero positivo.")
            continue
        return valor


def main() -> None:
    print("Comprobador de congruencias")
    a = pedir_entero("Primer número entero (a): ")
    b = pedir_entero("Segundo número entero (b): ")
    modulo = pedir_entero("Módulo positivo (n): ", positivo=True)

    resto_a = a % modulo
    resto_b = b % modulo
    print(f"\n{a} % {modulo} = {resto_a}")
    print(f"{b} % {modulo} = {resto_b}")

    if son_congruentes(a, b, modulo):
        print(f"Sí: {a} y {b} son congruentes módulo {modulo}.")
    else:
        print(f"No: {a} no es congruente con {b} (mod {modulo}).")


if __name__ == "__main__":
    main()
