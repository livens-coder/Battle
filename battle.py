teks = input("Antre yon tèks: ")
teks = teks.lower()

kantite_a = 0
kantite_i = 0

for let in teks:
    if let == 'a':
        kantite_a += 1
    elif let == 'i':
        kantite_i += 1

if kantite_a == kantite_i:
    print("Kantite fwa 'a' ak 'i' se menm.")
    print("Nan tèks ou gen:", kantite_a, "'a'")
    print("Nan tèks ou gen:", kantite_i, "'i'")
else:
    print("Kantite 'a' ak 'i' pa menm.")
    print("Nan tèks ou gen:", kantite_a, "'a'")
    print("Nan tèks ou gen:", kantite_i, "'i'")


