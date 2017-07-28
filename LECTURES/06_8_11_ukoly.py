
"""Pokud pole o délce N, obsahuje všechna čísla od 0..N-1 právě jednou, pak toto pole kóduje permutaci tak, že první prvek se zobrazí na místo, kde se v poli nachází 0, druhý prvek na místo, kde se v poli nachází 1,
Pole [0, 1, 2, 3], kóduje identickou tzv. jednotkovou permutaci o čtyřech prvcích, pole [3, 2, 1, 0] kóduje otočení prvků v poli.
Napište program, který načtěte z jednoho řádku standardního vstupu vektor reprezentující permutaci a najde a vytiskne inverzní permutaci, tj. permutaci, která převede zadanou permutaci na jednotkovou.
Inverzní permutace k permutaci [2, 0, 1], je permutace [1, 2, 0], neboť první permutace zobrazí 0→2 a druhá permutace 2→0, obdobně 1→0, druhá permutace 0→1; první 2→1 a druhá 1→2."""""

def permutation (a):
   
    b = [0]* len(a)
    
    for i in range (len(a)):
        b [a [i]] = i
    
    return b
        
print (permutation([2,0,1]) ) 
print(permutation([1,2,0]) )



"Napište funkci multiVecMat(v,m), která vypočte součin vektoru v a matice m."
"Pokud nesouhlasí rozměry matice a vektoru, pak funkce vrací None"  
def multiVecMat(v,m):  
    if (len(v) != len (m [0])):
        return None
    else :
        for i in range (len(m)):
            for j in range (len (m [i])):
                m [i][j] *=v [j]
                
            print(m [i])   
m=[[0,0,1],[0,1,0],[1,0,0]]
v=[2, 4, 6]
multiVecMat (v,m)  

""" Napište program, který načte matici a následně permutaci,
 která definuje prohození řádků zadané matice. 
 Na výstup program vytiskne matici s řádky prohozenými podle zadané permutace"""
def prohozz (p,m):
    
    b= [[0] * len(m[0])]*len(m)   
    
    for i in range (len(m)):
        b [p [i]] = m [i]
    print ()    
    for i in range (len(m)):    
        print(b [i])        

prohozz ([1,2,0], m)


"""--------------------GAUSS ELIMINATION METHOD-------------------"""
#does not work yet
def gauss(matrix):


    def findmaxrowincolumn (column):
        max,maxrow =0,0
        for i in range (column,len(matrix)):
            if abs( matrix [i][column]) > max:
                maxrow = i
                max = abs( matrix [i][column])

        return maxrow

    def set (column):
        maxrow =findmaxrowincolumn(column)
        if  maxrow !=column:
            temp = matrix [column]
            matrix [column] = matrix [maxrow]
            matrix [maxrow] = temp

    def do_line (i):
        set (i)
        if matrix [i][i] != 0:

            for r in range (len (matrix)):
                for l in range (len(matrix[r])):
                    if r!=i:
                        matrix [r][l] -= (matrix[r][i]*matrix [i][l])
                    else:
                        matrix[i][l] = matrix[i][l] / matrix[i][i]
            return True
        else:
            return False

    for i in range (len(matrix)):
        if not do_line(i):
            return False
    return True


matrix = [
        [12,-7,3, 26],
        [4 ,5,-6, -5],
        [-7 ,8,9, 21]
    ]
from fractions import Fraction
mm = [list(map(Fraction, v)) for v in matrix]
result = [list(map(Fraction, v)) for v in mm]

gauss(mm)