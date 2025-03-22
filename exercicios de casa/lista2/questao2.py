lado = int(input("Digite o lado do quadrado: "))

# for alt in range (lado):
#     for larg in range(lado):
#         print("*", end=" ")
#     print("")

print("* "*lado)
for x in range (lado-2):
    print("* "+ "  "*(lado - 2) + "*")
print("* "*lado)
