DNA = input("Enter DNA sequence :- ").upper()
Complement = []

for seq in DNA:
  if seq == "A":
    Complement.append("T")
  elif seq == "T":
    Complement.append("A")
  elif seq == "G":
    Complement.append("C")
  elif seq == "C":
    Complement.append("G")

JoinComplement = "".join(Complement)

ReverseComplement = JoinComplement[::-1]

print(f"Original sequence is :- {DNA}")
print(f"Complement sequence is :- {JoinComplement}")
print(f"Reverse complement is :- {ReverseComplement}")