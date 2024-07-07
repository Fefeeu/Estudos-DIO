
# 🐍 Python
Area dedicada a comandos, sintexes, utilidades, etc. Do Python

## 📝 Documentação 
-  [sintaxes](https://pythoniluminado.netlify.app)
- [Repositório DIO](https://github.com/digitalinnovationone/trilha-python-dio)

## Sumário
|               | 
| ------------- | 
| [🚪 Inputs](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#-inputs)  | 
| [✏️ Manipulação de Print](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#%EF%B8%8F-manipulação-de-print)  |
| [🔢 Operadores Aritiméticos](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#-operadores-aritiméticos)  |
| [❔ Operadores de Comparação](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#-operadores-de-comparação)  |
| [🟰 Operadores de Atribuição](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#-operadores-de-atribuição)  |
| [❔ Operadores Lógicos](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#-operadores-lógicos)  |
| [🧠 Operadores de Identidade](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#-operadores-de-identidade)  |
| [🔍 Operadores de Assosiação](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#-operadores-de-assosiação)  |
| [🛑 Estruturas Condicionais](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#-estruturas-condicionais)  |
| [🔁 Estruturas de Repetição](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#-estruturas-de-repetição)  |
| [✏️ Strign](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#%EF%B8%8F-strign)  |
| [📃 Lista](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#-lista) |
| [📄 Tuplas](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#-tuplas) |
|[🪢 Conjuntos](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#-conjuntos)|
|[🖇️ Dicionários](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#%EF%B8%8F-dicionários)|
|[📥 Funções](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#-funções)|
||

## 🚪 Inputs
```python
x = input()       #input padrão qualquer

x = input("texto de exemplo")   #input padrão qualque porem com um texto/valor antes da opção de input

x = int(input())  #input porem definindo o tipo da variavel direto nesse caso 'int'

x, y, z = input().split()       #input com multiplas variaveis

int(x)            #converte a variavel para o tipo que deseja nesse caso 'int'
```
### [Home](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#sumário)

## ✏️ Manipulação de Print
```python
print(nome, idade) #a separação por virgulas faz com que retorne diferentes variaveis

print(f"meu nome é {nome} e minha idade é {idade}") #o print(f) faz com que possa ser colocadas variaveis dentro de uma string

print(f"O valor de PI é {PI:x.2f}") #o mesmo do anterior porem só com 2 casas decimais se for uma variavel com ponto flutuante, o x define espaços em branco antes da variavel se não colocar nada fica sem adção de espaços em branco {PI:.2f}


print(x, y, z, sep = "o que quiser")    #faz com que a separação das variaveis sejam o que voce decidir por padrão é " "

print(x, y, z, end = "o que quiser")  #faz com que o final do print seja o que voce quiser, por padrão é "/n"
```
### [Home](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#sumário)

## 🔢 Operadores Aritiméticos
```python
#em:
x = 10
y = 4
print(x + y)    #soma simples
# 14

print(x - y)    #subtração simples
# 6

print(x * y)    #multiplicação simples
# 40

print(x ** y)   #exponenciação x^y
# 10000

print(x / y)    #divisão simples
# 2.5

print(x // y)   #divisão inteira
# 2

print(x % y)    #resto da divisão
# 5
```

## ❔ Operadores de Comparação
```python
#em:
x = 10
y = 4
print(x == y)   #x igual a y?
# False

print(x != y)   #x é diferente de y?
# True

print(x > y)    #x maior que y?
# True

print(x < y)    #x menor que y?
# False

print(x >= y)   #x maior ou igual que y?
# True

print(x <= y)   #x menor ou igual que y?
# False
```
### [Home](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#sumário)

## 🟰 Operadores de Atribuição
```python
x = y   #x recebe o valor de y

x += y  #x recebe o valor de x + y

x -= y  #x recebe o valor de x - y

x *= y  #x recebe o valor de x * y

x **= y #x recebe o valor de x ** y

x /= y  #x recebe o valor de x / y

x //= y #x recebe o valor de x // y

x %= y  #x recebe o valor de x % y
```
### [Home](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#sumário)

## ❔ Operadores Lógicos 
```python
x > y and x == y    #comparação onde as duas tem que ser verdadeiras, é o valor logico 'e'

x > y or x == y     #comparação onde uma tem que ser verdadeiras, é o valor logico 'ou'

not x > y           #inverte o valor, exemplo se fosse True retorna False e se for False retorn True
```
### [Home](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#sumário)
## 🧠 Operadores de Identidade
São operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória
```python
#em:
teste = "testezinho"
nome_teste = teste
valor_x, valor_y = 200, 200

print(teste is nome_teste)     #verifica se oculpam a mesma região de memória
# True

print(teste is not nome_teste) #verifica se não oculpam a mesma região de memória
# False

print(valor_x is valor_y)      #verifica se oculpam a mesma região de memória
# True
```
### [Home](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#sumário)
## 🔍 Operadores de Assosiação
São operadores utilizados para verificar se um objeto está presente em uma sequência.
```python
#em:
curso = "Curso de Python"
frutas = ["Laranja", "Uva", "Limão"]
valores = [1500, 100]

print("Python" in curso)    #verifica se há String "Python" está presente na String 'curso'
# True

print("Uva" in frutas)      #verifica se há String "Uva" está presente na lista de Strings 'frutas'
# True

print("Maçã" not in frutas) #verifica se há String "Maçã" NÃO está presente na lista de Strings 'frutas'
# True

print(200 in valores)       #verifica se o valor '200' está presente na lista de valores 'valores'
# False
```
 ### [Home](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#sumário)
## 🛑 Estruturas Condicionais
- Condições "se" "se não se" "se não"
```python
if (Condição Lógica):   #obs.: não é preciso os parenteses
    #codigo

#fim

elif (Condição Lógica):
    #codigo

#fim

else:
    #codigo

#fim
```
- Condiçoes ternárias no caso 'if ternário'
```python
x "Suecesso" if (saldo >= saque) else "falha"   #define em uma unica linha os possiveis valores da variavel
```
### [Home](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#sumário)
## 🔁 Estruturas de Repetição
- **For**

Repete até a condição de parada/limite

Um 'for' que percorre todo um texto verificando as vogais e printando elas
```python
texto = input("informe um texto")
VOGAIS = "AEIOU"

for letra in texto: #letra vai variar para todas as letras em 'texto'
    if (letra.upper() in VOGAIS):
        print(letra, end="")
else:   #esse else serve só para rodar as linhas a baixo logo apos o termino do for, não faz tanta diferença ele estar la e nao, inclusive pouco usado
    print() #quebra de linha
```
Um 'for' que sai todos os valores de 0 a n-1
```python
n = int(print())

for i in range(0, n):   #for repetindo de 0 a n-1 com i de 1 em 1
    print(i)
```
Obs.: o sentido do range(0,n) é que o python "cria" um vetor com todos os numeros inteiro de 0 a n-1, e o 'i' percorre isso. Para deixar claro:
range(0,10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

```python
n = int(print())

for i in range(0, n, 3):   #for repetindo de 0 a n-1 com i variando de 3 em 3 [0, 3, 6, ..., n-1]
    print(i)
```
- **While**

repete equanto a cndição for verdadeira

```python
opcao = -1

while (opcao != 0):     #repete enquanto opcao for diferente de 0 no momento que for fa
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair"))
else:   #mesma coisa do for: else:
    #codigo
```

```python
    for i in range(0, 10):
        if(i == 8):
            continue    #o 'continue' vai para a proxima execução do for/while
        print(i, end = " ")
```
### [Home](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#sumário)
## ✏️ Strign
- **sintaxes**

```python
palavra = "exemplo"

len(palavra)    #retorna o tamanho da string
# 7
```

- **Manipulação de Caracteres**
```python
curso = "pYtHon"

print(curso.upper())    #converte todas as letras para maiuscula
# PYTHON

print(curso.lower())    #converte todas as letras para minuscula
# python

print(curso.title())    #converte todas as letras para minuscula menos a primeira que é para maiuscula
# Python
```
```python
curso = "   Python  "

print(curso.strip())    #retira todos os espaços vasios da string
# "Python"

print(curso.lstrip())   #retira todos os espaços em branco no começo(a esquerda por isso l)

print(curso.rstrip())   #retira todos os espaços em branco do final(a direita por isso r)
```
```python
curso = "Python"

print(curso.center(10, "#"))    #adiciona nesse caso "#" até ficar com a quantidade de letras definidas, e a string centralizada no meio
# ##Python##

print("-".join(curso))        #adiciona nesse caso "-" entre cada caracter da string nao colocando no final
# P-y-t-h-o-n
```
- **Soma de Strings**
```python
curso = "Python"
caracteristica = "basico"

print(curso + " " + caracteristica) #junta as strings no final da anterior
# "Python basico"
```
- **Fatiamento de String**
```python
nome = "Felipe Ferreira de Carvalho Gabriel Pereira"

nome[x]     #retorna o caracter da posicao x

nome[x:y]   #retorna a substring iniciada em x e terminada em y-1

nome[:x]    #retorna a substring do inicio até x-1

nome[x:]    #retorna a substring iniciada em x até o final

nome[x:y:z] #retorna a substring iniciada em x e terminada em y-1 porem pulando de z em z caracteres

nome[::-1]  #espelha a string
```
- **String com Multiplas Linhas**
```python
nome = "Fefe"

mensagem = f"""
    Olá meu nome é {nome},
e estou tentando abrender python bunitin
testando só as propriedades das strings
"""
#a mensagem vai sair com as linhas quebradas na exibição também
```
Um exemplo melhor do uso
```python
print("""
    ########## MENU ##########

    1 - Depositar
    2 - Sacar
    3 - Sair

    ##########################
""") 
```
### [Home](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#sumário)
## 📃 Lista
lista como o próprio nome ja explica são lista de variaveis, podendo inclusive diferentemente de outras linguagens terem mais de um tipo de variavel na mesma lista, mas são baicamente vetores infinitos.
```python
frutas["Laranja", "Uva", "Banana"]  #lista de strings

frutas[]    #lista vasia

letras = lista("python") #uma lista dada letra por letra

numeros = lista(range(10))   #uma lista de numeros dada numero por numero de 0 a 10-1

carro = ["Ferrari", "F8", 2020, 2900.82, "São Paulo", True]   #lista de diferentes variaveis

#exemplo de print
print(carro)   #vai retornar item por item da lista
```
Para "buscar" um item na lista é só entregar sua posicao
```python
frutas["Laranja", "Uva", "Banana", "Pera", "Kiwi"]

print(frutas[2])
    # Banana

print(frutas[-1])   #se o valor de posicao for negativo então ele ira buscar apartir do final
    # Kiwi
```
**lista Aninhadas**

são listas de listas ou seja matriz
```python
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]              #pode ser na mesma linha

print(matriz[0])    #retorna a lista dessa posicao
    # [1, "a", 2]

print(matriz[0][0]) #retorna a posica da lista na posicao da lista
    # 1

print(matriz[0][-1])
    # 2

print(matriz[-1][-1])
    # c

```

**Repartições**
```python
lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])    #pega do elemento da posicao 2 para frente
    # ["t", "h", "o", "n"]

print(lista[:2])    #pega todos os elementos até a posicao 2-1
    # ["p", "y"]

print(lista[1:3])   #pega todos os elementos da posicao 1 até a posicao 3-1
    # ["y", "t"]

print(lista[:3:2]) #pega todos os elementos da posicao 0 até 3-1 porem pegando 1 de 2 em 2
    # ["p", "t"]

print(lista[::])    #pega todos os elementos
    # ["p", "y", "t", "h", "o", "n"]

print(lista[::-1])  #pega todos os elementos porem invertida
    # ["n", "o", "h", "t", "y", "p"]
```
**Navegando Pela Lista**

Tem como navegar da maneira padrão porem a uma melhor em python
```python
carros = ["gol", "celra", "palio"]

for car in carros:
    print(car)    #vai retornar carro por carro

for indice, car in enumerate(carros):
    print(f"{indice}: {car}")        #retorna a posicao do carro e o carro
```
**Compressão de Lista**


Criar uma lista baseada em outra lista já pré existente, basicamente uma sublista
```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
pares = []
quadrados = []

for num in numeros:
    if num % 2 == 0: 
        pares.append(numero)

for num in numeros:
    quadrados.append(num ** 2)
```
ou no metodo comprehension
```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
pares = []
quadrados =[]

pares = [num for num in numeros if (num % 2 == 0)]  #para fazer uma sublista

quadrados = [num ** 2 for num in numeros]   #para fazer uma lista baseada em uma outra lista
```

### Metodos de usos de lista
- **[].append**

- **[].clear()**

Essas são as sintaxes utilizadas para respectivamente adicionar valores a uma lista vasia e retirar todos os valores da lista
```python
lista = []

lista.append(1)
lista.append("python")
lista.append([40, 30, 20, 10, 0])

print(lista)
# [1, "python", [40, 30, 20, 10, 0]]

lista.clear()

print(lista)
# []
```
- **[].copy()**

Essa sintaxe é utilizada para copiar uma lista para outra porem ambas estarão ocupando espaços diferentes de memória, ou seja apesar de serem iguais serão objetos diferentes
```python
lista = [1, "python", [40, 30, 20, 10, 0]]

l2 = lista.copy()

print(l2)   #apesar de retornarem valores 100% iguais eles são objetos diferentes 
# [1, "python", [40, 30, 20, 10, 0]]
``` 
Esse caso deve ser muito utilizado para quando vai-se mudar uma lista em uma função mas ainda quer manter seus valores anteriores, ou seja como exemplo (se eu alterar o '1' por '2' na 'l2' na 'lista' se mantera a ser '1') e vice-verssa
- **[].count()**

Essa sintaxe é utilizada para contar quantas vezes são repetidos o valor informado
```python
cores = ["azul", "verde", "azul", "amarelo"]

print(cores.count("azul"))
# 2
```
- **[].extend()**

Essa sintaxe é utilizada para mesclar duas listas em uma
```python
lista = ["python", "C++", "js"]
outras_lista = ["java", "csharp"]

lista.extend(outras_lista)    #pode ser com uma lista ja existente
print(lista)
# ["python", "C++", "js", "java", "csharp"]

lista.extend(["java", "csharp"])   #mesmo caso que o anterior porem sem ser com uma lista pronta e sim com uma declarada na hora
print(lista)
# ["python", "C++", "js", "java", "csharp"]
``` 
- **[].index()**

Essa sintaxe é utilizada para busca em qual posição é encontrado o PRIMEIRO valor na lista
```python
lista = ["python", "C++", "js", "java", "csharp"]

print(lista.index("java"))
# 3
```
- **[].pop()**
Essa sintaxe é utilizada para retirar valores da lista, nesse caso é retirado em formato de pilha ou seja retira o ultimo valor colocado
```python
lista = ["python", "C++", "js", "java", "csharp"]

lista.pop()    #retira "csharp"
lista.pop()    #retira "java"
lista.pop(1)   #retira "C++"
```

- **[].remove()**

Essa sintaxe é utilazada para remove o primeiro elemento que seja igual ao pedido
```python
lista = ["python", "C++", "js", "java", "C++", "csharp"]

lista.remove("C++")    #remove o primeiro "c++"
print(lista)
# ["python", "js", "java", "C++", "csharp"]
```
- **[].reverse**

Essa sintaxe é utilizada para inverter a lista
```python
lista = ["python", "C++", "js", "java", "csharp"]

lista.reverse()
print(lista)
# ["csharp", "java", "js", "C++", "python"]
```
- **[].sort**

Essa sintaxe é utilizada para organizar a lista, obs.: se forem strings sera ordenada em ordem alfabetica
```python
lista = ["python", "C++", "js", "java", "csharp"]
lista.sort()    #ordena a lista em ordem padrao
print(lista)
# ["C++", "csharp", "java", "js", "python"]

lista = ["python", "C++", "js", "java", "csharp"]
lista.sort(reverse = True)  #ordena a lista invertida a ordem padrao
print(lista)
# ["python", "js", "java", "csharp", "C++"]


lista = ["python", "C++", "js", "java", "csharp"]
lista.sort(key=lambda x: len(x))    #ordena por tamanho de string
print(lista)
# ['js', 'C++', 'java', 'python', 'csharp']

lista = ["python", "C++", "js", "java", "csharp"]
lista.sort(key=lambda x: len(x), reverse=True)  #ordena de maneira inversa ao tamanho da string
print(lista)
# ['python', 'csharp', 'java', 'C++', 'js']
```
- **len()**

Essa sintaxe é utilizada para retornar o tamanho da lista
```python
lista = ["python", "C++", "js", "java", "csharp"]
print(len(lista))
# 5
```
- **sorted()**

Essa sintaxe é basicamente o mesmo que o [].sort() porem nesse caso ela é uma função padrão do próprio python, então não a muitos motivos para utiliza-la
```python
lista = ["python", "C++", "js", "java", "csharp"]

sorted(lista, key=lambda x: len(x)) #organiza a lista

sorted(lista, key=lambda x: len(x), reverse=True)   #organiza a lista porem invertida 
```
### [Home](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#sumário)
## 📄 Tuplas
Tuplas são estruturas de dados muito parecidas com as listas, mas a diferença entre elas é que são imutaveis, portanto quando criada não há como alteralas. 

A forma de criação de uma Tupla é quase igual a de uma lista, a unica diferença em uma das formas de criação dela é que listas é criada com [] enquanto a tupla é criada com ().

```Python
frutas = ("Laranja", "Pera", "Uva",)
# sim aquela virgula no final é importante para criação da 'Tupla' principalmente se ela for uma Tupla de 1 unico elemento

numeros = tuple([1, 2, 3, 4])
# pode mandar uma lista para a Tupla

letras = tuple("Python")

pais = ("Brasil",)
```

Para acesso de dados é exatamente igual a lista.
```Python
frutas = ("Laranja", "Pera", "Uva", "Banana",)

frutas[1]   #Pera
frutas[-3]  #Pera
```

Também há como criar tuplas de tuplas como exemplo matrizes.
```Python
matriz = (
    ("a", 1, 2,),
    (3, "b", 4,),
    (5, 6, "c",),
)

matriz[0][1]    #1
matriz[1][1]    #b
matriz[-2][-1]  #4
```

**().count**

Conta quantas vezes o valor pedido se repete na Tupla 
```Python
cores = ("Azul", "Vermelho", "Verde", "Azul", "Amarelo",)

cores.count("Azul")     # 2
cores.count("Vermelho") # 1
```

**().index**

Retorna a posiçãodo item buscado
```Python
cores = ("Azul", "Vermelho", "Verde", "Azul", "Amarelo",)

cores.index("Azul")     # 0
cores.index("Vermelho") # 1
```

**len()**

Retorna quantos elementos tem na Tupla
```Python
cores = ("Azul", "Vermelho", "Verde", "Azul", "Amarelo",)

len(cores)  # 5     
```
### [Home](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#sumário)
## 🪢 Conjuntos

Um 'set' é uma coleção que não possue objetos repetidos, usada para representar conjuntos matemáticos e para retirar item repetidos de um interável.

E assim como Listas e Tuplas existe uma forma de crialo de forma direta, e nesse cadso é com {}
```Python
conjunto = {"Python", "Java", "Python", "C++"}
print(conjunto) # {"Java", "Python", "C++"}

set([1, 2, 2, 3, 4, 4, 5, 5, 5])    #{1, 2, 3, 4, 5}

set("abacaxi")  # {"b", "a", "c", "x", "i"}

set(("palio", "gol", "celta", "palio",))    # {"gol", "celta", "palio"}
```

***MUITO IMPORTANTE: o set não garente a organização da lista podendo ou não trocar a ordem dela***

'set' não possui indexação, portanto para lidar com um set é preciso colocalo em uma lista
```Python
cores = {"Azul", "Vermelho", "Verde", "Azul", "Amarelo"}
# {"Vermelho", "Verde", "Azul", "Amarelo"
cores = list(cores)

cores[0]  # Vermelho
cores[2]  # Azul
```

Porem há como percorrelo em um for
```Python
cores = {"Azul", "Vermelho", "Verde", "Azul", "Amarelo"}

for cor in cores
    print(cor)
# Vermelho Verde Azul Amarelo
```

Assim como conjuntos matemáticos tem forma de fazer operações entre conjuntos

**{}.union**

Faz a união entre 2 conjuntos
```Python
numsA = {1, 2}
numsB = {3, 4}

numsA.union(numsB)  # {1, 2, 3, 4}
```

**{}.intersection**

Verifica quais objetos estão em comum entre os dois set's
```Python
numsA = {1, 2, 3}
numsB = {2, 3, 4}

numsA.intersection(numsB)   # {2, 3}
```

**{}.difference**

Verifica quais objetos não estão em comum entre o set pedido
```Python
numsA = {1, 2, 3}
numsB = {2, 3, 4}

numsA.difference(numsB) # {1}
numsB.difference(numsA) # {4}
```

**{}.symmetric_difference**

O mesmo que o anterior porem mostrando os dois unidos
```Python
numsA = {1, 2, 3}
numsB = {2, 3, 4}

numsA.symmetric_difference(numsB)   # {1, 4}
```

**{}.issubset**

Retorna a verificação se o conjunto é subconjunto do outro
```Python
numsA = {1, 2, 3}
numsB = {1, 2, 3, 4, 5, 6, 7}

numsA.issubset(numsB)   # true
numsB.issubset(numsA)   # false
```

**{}.issuperset**

Retorna a verificação se o conjunto é subconjunto do outro, porem de forma invertida
```Python
numsA = {1, 2, 3}
numsB = {1, 2, 3, 4, 5, 6, 7}

numsA.issuperset(numsB)   # false
numsB.issuperset(numsA)   # true
```

**{}.isdisjoint**

Retorna a verificação se o conjunto é completamente independente do outro
```Python
numsA = {1, 2, 3}
numsB = {4, 5, 6, 7}
numsC = {0, 1}

numsA.isdisjoint(numsB)   # true
numsA.isdisjoint(numsC)   # false
```

**{}.add**

Adiciona um valor ao set se já não existir o mesmo
```Python
nums = {1, 40}

nums.add(23)    #{1, 23, 40}
nums.add(17)    #{1, 17, 23, 40}
nums.add(64)    #{1, 17, 23, 40, 64}
nums.add(23)    #{1, 17, 23, 40, 64}
```

**{}.clear**

Limpa toda o set
```Python
nums = {1, 40}

nums    # {1, 40}
nums.clear()
nums    # {}
```

**{}.copy**

Copia todo o set para outro
```Python
nums = {1, 40}

nums    # {1, 40}
nums_B.copy(nums)
nums_B  # {1, 40}
```

**{}.discard**

Remove um item especifico do set
```Python
nums = {1, 2, 2, 3, 4, 4, 4, 5, 6, 6}

nums    # {1, 2, 3, 4, 5, 6}
nums.discard(1)
nums    # {2, 3, 4, 5, 6}
nums.discard(45)    # se o item não esta no set não muda nada
nums    # {2, 3, 4, 5, 6}
```

**{}.pop**

Remove o primeiro item do set
```Python
nums = {1, 2, 2, 3, 4, 4, 4, 5, 6, 6}

nums    # {1, 2, 3, 4, 5, 6}
nums.pop()
nums.pop()
nums    # {3, 4, 5, 6}
```

**{}.remove()**

Remove um item em especifico, porem da erro se for pedido um item que não esta no set 
```Python
nums = {1, 2, 2, 3, 4, 4, 4, 5, 6, 6}

nums    # {1, 2, 3, 4, 5, 6}
nums.remove(1)
nums    # {2, 3, 4, 5, 6}
nums.remove(45)    # da erro
```
### [Home](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#sumário)
## 🖇️ Dicionários

Um metodo de organização onde são utilizados pares de informações, onde há uma chave e um valor, e assim como a Tupla os valores são das chaves imutáveis, porem os valores podem ser mutaveis

Ele pode ser criado de forma direta ou pelo chamar da função
```Python
pessoa = {"nome":"Felipe", "idade":19}

pessoa = dict(nome = "Felipe", idade = 19)

pessoa  # {"nome":"Felipe", "idade":19}

pessoa["sexo"] = "Masculino"    # adiciona mais uma chave ao dict

pessoa  # {"nome":"Felipe", "idade":19, "sexo":"Masculino"}
```

Para cessar o valor, no lugar do indice deve-se usar a chave
```Python
pessoa = {"nome":"Felipe", "idade":19, "sexo":"Masculino"}

pessoa["nome"]  # "Felipe"
pessoa["idade"] # 19
pessoa["sexo"]  # "Masculino"

pessoa["nome"]  # "Mica"
pessoa["idade"] # 44
pessoa["sexo"]  # "Feminino"

pessoa  # "nome":"Mica", "idade":44, "sexo":"Feminino"
``` 

**Dicionários Aninhados**

Dicionários dessa forma são basicamente dicionários, dentro de outros dicionários
```Python
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

contatos["guilherme@gmail.com"]["nome"] #Guilherme
```

Interando um Dicionário
```Python
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

for chave in contatos   # maneira "errada" de se fazer
    print(chave, contatos[chave])

for chave, valor in contatos.items()    # maneira "correta" de se interar um dict
    print(chave, valor)
    # "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
    # "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"}
    # "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"}
    # "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"}

#obs.: os 2 for possuem a mesma saida

```

**{}.clear**

Metodo padrão, somente limpa o dict
```Python
pessoa = {"nome":"Felipe", "idade":19, "sexo":"Masculino"}

pessoa.clear()
pessoa  # {}
```

**{}.copy**

Copia diretamente um dicionario para outro
```Python
pessoa = {"nome":"Felipe", "idade":19, "sexo":"Masculino"}

pessoa_copia = pessoa.copy()

pessoa_copia    # {"nome":"Felipe", "idade":19, "sexo":"Masculino"}
```

**{}.fromkeys**

Serve para crias as chaves de um dicionário não necessariamente criando os valores vinculados a elas
```Python
pessoa.fromkeys(["nome", "idade"])
pessoas # {"nome":None, "idade":None}

info.fromkeys(["ID", "nome", "idade"], "NoInfo")
info    # {"ID":"NoInfo", "nome":"NoInfo", "idade":"NoInfo"}
```

**{}.get**

Serve principalmente para dar um retorno padrão para quando a chave não existe no dicionário
```Python
pessoa = {"nome":"Felipe", "idade":19, "sexo":"Masculino"}

pessoa["telefone"] # como não existe KeyError

pessoa.get("telefone")  # None
#obs.: o retorno padrão da função é None

pessoa.get("telefone", 404)  # 404
#obs.: retorna o que foi colocado 

pessoa.get("nome")  # "nome":"Felipe"
#obs.: retorna a chave e o valor, ja que eles existem
```

**{}.item**

Retorna uma lista de Tuplas
```Python
contato = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
    }

contato.item()  #dict_items([("guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"})])
```

**{}.keys**

Retorna as chaves do dict
```Python
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

contatos.keys() # ([guilherme@gmail.com, giovanna@gmail.com, chappie@gmail.com, melaine@gmail.com])
```

**{}.values**

Retorna todos os valores das chaves que o dict
```Python
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

contatos.value() # ([{"nome": "Guilherme", "telefone": "3333-2221"}, {"nome": "Giovanna", "telefone": "3443-2121"}, {"nome": "Chappie", "telefone": "3344-9871"}, {"nome": "Melaine", "telefone": "3333-7766"}])
```

**{}.pop**

Remove uma chave em expecifico e seu valor, retornando o valor da chave que removeu
```Python
contato = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

contato.pop(guilherme@gmail.com)    # {"nome": "Guilherme", "telefone": "3333-2221"}

contato.pop(guilherme@gmail.com, "Valor não encontrado")    # se não encontrar o valor ele ira retornar o que foi colocado, e se não for colocado nada para retornar ele dara um erro
```

**{}.popitem**

Remove em ordem os items do dicionario
```Python
contato = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

contato.popitem()   # {"nome": "Guilherme", "telefone": "3333-2221"}

contato.popitem()   # KeyError
```

**{}.setdefault**

Se a chave já existir retorna o que esta na chave, se não existir cria a chave e da a ela o valor pedido
```Python
contato = {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("nome", "Felipe")    # Guilherme
contato # {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefaut("idade", 26)  # 28
contato # {"nome": "Guilherme", "telefone": "3333-2221", "idade":28}
```

**{}.update**

É usado para literalmente atualizar os valores, verificando se o valor não exixtir criando um novo para atualizalo
```Python
contato = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
    }

contato.update("guilherme@gmail.com": {"nome": "Felipe"})   
contato # {guilherme@gmail.com": {"nome": "Felipe}}
#se existir a chave atualiza para os novos valores

contato.update("felipe301204@gmail.com": {"nome": "Felipe"})   
contato # {guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}, felipe301204@gmail.com": {"nome": "Felipe}}
#se não existir a chave adiciona a nova chave com seus novos valores
```

**in**

Serve para fazer verificação de maneira "bonita" no codigo mas só serve mesmo para verificar se a chave esta no dict
```Python

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

"guilherme@gmail.com" in contatos       #true
"felipe301204@gmail.com" in contatos    #false
"nome" in contatos[guilherme@gmail.com] #true
```

**del**

Usado para remover uma chave e por consequência o seu valor do dict
```Python
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["guilherme@gmail.com"]["telefone"] # remove a "chave da chave"
del contatos["melaine@gmail.com"]   # remove toda a chave com todo seu valor
```
### [Home](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#sumário)
## 📥📤 Funções 
Funções são blocos de códigos que possuem "nomes"(identificadore) com parametros que podem ser recebidos, e também retornos, em geral usada para códigos recursivos, e para organizar o código em geral.

**Criando uma Função**
```Python
def falando_oi():
    print("Hello World")

def pessoa_falando_oi(nome):
    print(f"Olá eu sou {nome}")

def pessoa_falando_oi_pronto(nome = "Anônimo"):
    # Nesse caso o que está acontecendo é que o(s) parametro(s) terão um nome "padrão", onde se não for enviado nada sera usado o declarado anteriormente  
    print(f"Olá eu sou {nome}")
```
Formas de enviar o(s) valor(es) pra função.
```Python
def salvar_carro(marca, modelo, ano, palca)
    print(f"carro criado como: {marca} / {modelo} / {ano} / {placa}")

info1, info2, info3, info4 = input().split()
info3 = int(info3)

salvar_carro(info1, info2, info3, info4)

salvar_carro(marca = info1, modelo = info2, ano = info3, placa = info4)
    # A diferença entre os tipos de envio é que nesse caso os parametros são tanto mais organizados quanto não precisam estar na mesma ordem que a esta na função

salvo_carro(**{"marca":info1, "modelo":info2, "ano":info3, "placa":info4})
```

**Retornando Valores**

Funções em phyton diferente de algumas linguagens de programação permitem o retorno de mais de um valor simultaneamente.

Obs.: por padrão a função é void ou seja retorna 'None'

```python
def numeros_vizinhos(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

num = int(input())   # 10

print(numeros_vizinhos(numero = num))   # (9, 11)


num1, num2 = numeros_vizinhos(num)
print(num1, num, num2)  # 9, 10, 11
```

**args e kwargs**

São formas de declarar Tuplas e Dicionários respectivamente, sendo que por convenção é usado as palavras *args e **kwargs, mas pode ser usado qualquer palavra no lugar delas
```Python
def lista_moradores(casa, *args, **kwargs):
    moradores = ", ".join(args)
    idade_moradores = ", ".join([f"{chave}: {valor}" for chave, valor in kwargs.items()])

    print(f"A casa {casa} possue {len(args)} moradores de nomes: {moradores}, a qual a idade de cada um é {idade_moradores}")

moradia = "Guaxupé"
nomes = ("Fefe", "Mica", "Lucas",)
idades = {"Fefe":19, "Mica":44, "Lucas":45}

lista_moradores(moradia, *nomes, **idades)
# A casa Guaxupé possue 3 moradores de nomes: Fefe, Mica, Lucas, a qual a idade de cada um é Fefe: 19, Mica: 44, Lucas: 45
```

**Separando Maneiras de Enviar Parametros**

Como visto anteriormente há diferente maeiras de enviar os parametros para a função sende alguns deles por posição(ordem de entrada), por palavra-chave("kw" = 'valor') e por posição_ou_palavra-chave(qualquer um dos dois)

![Exemplificação](https://i.imgur.com/Pb8osWH.png)

A ordem como mostrado na imagem em uma função seria antes do '/' só ***posição***, depois do '*' ***palavra-chave***, e o resto seria ambos.
```Python
def so_exemplo(posicao1, posicao2, /, ambos1, ambos2, *, palavra_chave1, palavra_chave2):
    print(posicao1, posicao2, ambos1, ambos2, palavra_chave1, palavra_chave2)

a, b, c, d, e, f = input().split()

so_exemplo(a, b
           c, ambos2 = d)
           palavra_chave1 = e, palavra_chave2 = f)
# Éssa é a maneira correta de se enviar para a função
```

**Objetos de Primeira Classe**

Objetos de Primeira Classe são objetos que podem ser enviados e retornados por funções, e funções são objetos de primeira classe, inclusive da para dar o valor de uma variavel como uma função.

```Python
def soma(a, b):
    return a + b

def modulo(a, b, funcao):
    resultado = funcao(a, b)    # a funcao 'soma' foi enviada para função módulo porem agora com o nome 'funcao'

    if(resultado >= 0)
        return resultado
    elif(resultado < 0)
        return -resultado

modulo(10, -20, soma)   # |10 - 20| = 10

operacao = soma
operacao(a, b)  # ele vai literalmente fazer a mesma coisa que a soma.
```

**Escopo Local e Global**

No Python tem como usar variaveis em um escopo local assim como um escopo global, sendo que o local deixa de existir quando o escopo se encerra.

obs.: se a variavel for global na hora de usala é preciso usar a palavra reservada 'global' para utilizala

```Python
salario = 2000

def lucro_no_mes (gastos):  # gastos é uma variavel no escopo local portanto ela não existe fora da função
    global salario
    return salario - gastos

lucro_no_mes(1200)  # 800
```

**Pequenas Adições**
```Python
derf funcao_generica(variavel):
    pass    # essa palavra reservada 'pass' faz com que o Python "feche" a funcao
```

### [Home](https://github.com/Fefeeu/Estudos-DIO/blob/main/resumos/Python_basico.md#sumário)
