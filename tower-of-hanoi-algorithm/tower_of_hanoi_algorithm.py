def hanoi_solver(n):
    if not isinstance(n, int):
        return f'n must be an integer'
    if n<1:
        return f'n must be greater or equal than 1'
    lineas = []
    torre_A = []
    torre_B = []
    torre_C = []
    for disco in range(n, 0, -1):
        torre_A.append(disco)
    # Append del estado inicial
    lineas.append(f"{torre_A} {torre_B} {torre_C}")

    # torre A, torre C, torre B
    def mover(n, origen, destino, auxiliar):
        if n == 1:
            disco_cuspide = origen.pop()
            destino.append(disco_cuspide)
            lineas.append(f"{torre_A} {torre_B} {torre_C}")
            return
        else:
            # mover(2, torre A, torre B, torre C)
            mover(n-1, origen, auxiliar, destino)
            # origen -> A, destino -> B, auxiliar -> C
            disco_base = origen.pop()
            destino.append(disco_base)
            lineas.append(f"{torre_A} {torre_B} {torre_C}")
            mover(n-1, auxiliar, destino, origen)
    
    mover(n, torre_A, torre_C, torre_B)
    return "\n".join(lineas)

print(hanoi_solver(3))
