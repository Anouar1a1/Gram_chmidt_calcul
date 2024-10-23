import math
import random
import numpy as np
# Fonctions utiles
def p(a, b):
    c = 0
    for i in range(len(a)):
        c += a[i] * b[i]
    return c
def s(a, b):
    s = []
    for i in range(len(a)):
        s.append(a[i] + b[i])
    return s
def P(a, b):
    C = []
    for i in range(len(b)):
        C.append(a * b[i])
    return C
def sqrt2(d):
    sum = 0
    for i in range(len(d)):
        sum += d[i] ** 2
    q = math.sqrt(sum)
    return q
def est_liee(vecteurs):
  matrice = np.array(vecteurs)
  rang = np.linalg.matrix_rank(matrice)
  nombre_vecteurs = matrice.shape[0]
  return rang < nombre_vecteurs
def find_linearly_independent_subset(vectors):
    matrix = np.array(vectors)
    rank = np.linalg.matrix_rank(matrix)
    Vh = np.linalg.svd(matrix)
    basis = Vh[:rank].T
    return basis.tolist()
# Demander les entrées utilisateur
n = int(input("Donner le cardinal de votre famille: "))
m= int(input("Donner le nombre de coordonnées: "))
while n>m:
    print(f"Un de ces valeurs et erronne car{n} le nombre du cardinal est superieur a {m}le nombre de coordonnees ")
    n = int(input("Donner le cardinal de votre famille: "))
    m= int(input("Donner le nombre de coordonnées: "))
# Initialiser le dictionnaire pour stocker les vecteurs
g =dict()
for i in range(n):
    g[i] = []
    print(f"Pour le vecteur {i + 1}")
    for k in range(m):
        j = float(input(f"Donner la coordonnée {k + 1}: "))
        g[i].append(j)
d= [g[i] for i in range (n)]
if est_liee(d)==True:
  print(f"votre famille {d} est liée")
  d=find_linearly_independent_subset(d) 
if n< m :
    for o in range (n,m-n):
        while True :
            e =0
            kc= [random.randint(-10,10) for j in range (m)]
            for h in range (n):
                if p (kc,d[h])==0 and kc!=[0 for j in range (m)]:
                   e+=1
            if e == n:
                d[o]=kc
print(d)
# Initialiser les listes
L_u = []
L_e = []
# Calcul des vecteurs orthonormaux
L_u.append(d[0])
L_e.append(P(1 / sqrt2(L_u[0]), L_u[0]))
for i in range(1, n):
    c = d[i]
    for j in range(i):
        c = s(c, P(-p(d[i], L_e[j]), L_e[j]))
    L_u.append(c)
    L_e.append(P(1 / sqrt2(L_u[i]), L_u[i]))
print(L_e)