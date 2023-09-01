def tower(n, source, destination, auxillary):
    if n == 1:
        print("move disk 1 from ", source, "to ", destination)
        return
    tower(n-1, source, auxillary, destination)
    print("move disk ", n, "from ", source, "to ", destination)
    tower(n-1, auxillary, destination, source)

tower(3, 'A', 'B', 'C')