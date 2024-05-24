
# 🐍 Python
Area dedicada a comandos, sintexes, utilidades, etc. Do Python

## 📝 Documentação 
-  sintaxes](https://pythoniluminado.netlify.app sintaxe)
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
| []() |

## 🚪 Inputs
```python
x = input()       #input padrão qualquer

x = input("texto de exemplo")   #input padrão qualque porem com um texto/valor antes da opção de input

x = int(input())  #input porem definindo o tipo da variavel direto nesse caso 'int'

x, y, z = input().split()       #input com multiplas variaveis

int(x)            #converte a variavel para o tipo que deseja nesse caso 'int'
```

## ✏️ Manipulação de Print
```python
print(nome, idade) #a separação por virgulas faz com que retorne diferentes variaveis

print(f"meu nome é {nome} e minha idade é {idade}") #o print(f) faz com que possa ser colocadas variaveis dentro de uma string

print(f"O valor de PI é {PI:x.2f}") #o mesmo do anterior porem só com 2 casas decimais se for uma variavel com ponto flutuante, o x define espaços em branco antes da variavel se não colocar nada fica sem adção de espaços em branco {PI:.2f}


print(x, y, z, sep = "o que quiser")    #faz com que a separação das variaveis sejam o que voce decidir por padrão é " "

print(x, y, z, end = "o que quiser")  #faz com que o final do print seja o que voce quiser, por padrão é "/n"
```

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

## ❔ Operadores Lógicos 
```python
x > y and x == y    #comparação onde as duas tem que ser verdadeiras, é o valor logico 'e'

x > y or x == y     #comparação onde uma tem que ser verdadeiras, é o valor logico 'ou'

not x > y           #inverte o valor, exemplo se fosse True retorna False e se for False retorn True
```

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

## ✏️ Strign
- * sintaxes**

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