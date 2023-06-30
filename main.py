from pysat.solvers import Glucose3

g = Glucose3()
# g.add_clause([1, 2])
# g.add_clause([-1, 2])
# g.add_clause([1, -2])
# g.add_clause([-1, -2])
# print(g.solve())
# print(g.get_model())
N = 5
counter = 1
mapping_to_int = {}
mapping_to_int_inv = {}
positions = [[i,j] for i in range(1,N+1) for j in range(1,N+1)]
for position in positions:
  key = f"Q{position[0]}_{position[1]}"
  mapping_to_int[key] = counter
  mapping_to_int_inv[counter] = key
  counter = counter + 1


  dict(zip(["a","b","c","d"], range(4)))

#gerando uma instancia do solver (DPLL)
g = Glucose3()

#cada linha possui PELO MENOS UMA rainha
for i in range(1,N+1):
  line = []
  for j in range(1, N+1):
    line.append(mapping_to_int[f"Q{i}_{j}"])
  g.add_clause(line)

#implementar cada linha possui NO MAXIMO UMA RAINHA
#implementar cada coluna possui PELO MENOS UMA RAINHA

#cada coluna possui NO MAXIMO uma rainha
for j in range(1,N+1):
  for i in range(1, N+1):
    other_indexes = list(range(1,N+1))
    other_indexes.remove(i)
    for other in other_indexes:
      clause = [-mapping_to_int[f"Q{i}_{j}"], -mapping_to_int[f"Q{other}_{j}"]]
      g.add_clause(clause)

############## ATÉ AQUI CODIGO DO PROFESSOR ###################

#DIAGONAL PRINCIPAL
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N):
            if i + k <= N and j + k <= N:
                clause = [-mapping_to_int[f"Q{i}_{j}"], -mapping_to_int[f"Q{i + k}_{j + k}"]]
                g.add_clause(clause)# Adiciona ao solver a soma de ambos os indexes + k
            if i - k >= 1 and j - k >= 1:
                clause = [-mapping_to_int[f"Q{i}_{j}"], -mapping_to_int[f"Q{i - k}_{j - k}"]]
                g.add_clause(clause)# Adiciona ao solver a diferença de ambos os indexes - k

#DIAGONAL SECUNDÁRIA
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N):
            if i + k <= N and j - k >= 1:
                clause = [-mapping_to_int[f"Q{i}_{j}"], -mapping_to_int[f"Q{i + k}_{j - k}"]]
                g.add_clause(clause)# Adiciona ao solver ao X da matriz Index I + K e ao Y da matriz Index J - K
            if i - k >= 1 and j + k <= N:
                clause = [-mapping_to_int[f"Q{i}_{j}"], -mapping_to_int[f"Q{i - k}_{j + k}"]]
                g.add_clause(clause)# Adiciona ao solver ao X da matriz Index I - K e ao Y da matriz Index J + K

if g.solve():
    lista_rainhas = [mapping_to_int_inv[index] for index in g.get_model() if index > 0]
    print("Solução:")
    for rainha in lista_rainhas:
        print("Posição da rainha: {}".format(rainha))
else:
    print("Sem Solução possível")

