def DNA_strand(dna):
    dna = list(dna)
    i = 0
    while i < len(dna):
        if dna[i] == "A": dna[i]="T"
        elif dna[i] == "T": dna[i] = "A"
        elif dna[i] == "C": dna[i] = "G"
        elif dna[i] == "G": dna[i] = "C"
        i+=1
    return "".join(dna)

DNA_strand("CATA")
