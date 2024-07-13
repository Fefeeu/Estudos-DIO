
## Sumário
|       |
|-------|
||

## 📝 Documentação 
-  [sintaxes](https://pythoniluminado.netlify.app)
- [Repositório DIO](https://github.com/digitalinnovationone/trilha-python-dio)
- [PyPI](https://pypi.org)
-  [Python.org](https://docs.python.org/3/)

# Programação Orientada a Objetos
## O que é?
O paradigma de programação orientada a objetos estrutura o código abstraindo problemas em objetos do mundo real, facilitando o entendimento do código e tornando-o mais modular e extensível. Os dois conceitos chaves para aprenser POO são: **Classes** e **Objetos**.
### O que são Classes e Objetos:
Uma ***classes*** define as características e comportamentos de um ***objeto***, porém não conseguimos usá-las diretamente. Já os ***objetos*** podemos usá-los e eles possuem as características e comportamentos que foram definidos pelas ***classes***.

***Classes*** são partes mais abstratas 

## Criando uma Classe e Objeto

**__ init __** = Inicializador 

**self** = Uma referencia explicita para o objeto, basicamente queremos dizer que é a instancia passada para o objeto (pode ser outra palavra, por padrão usamos 'self')

**def's apos __ init __** = O conjuto deles são chamados de comportamento da classe. E ele são individualmente os metodos, são praticamente funções porem com pelo menos um argumento interno, por padrão o self.

```Python
class Bicicleta:    # criando a classe
    def __init__(self, cor, modelo, ano, valor):    #iciciando ela 
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    # daqui para a baixo sao os comportamentos dela
    def buzinar(self):
        print("Buzinando...")
    
    def parar(self):
        print("A bicicleta esta parando...")

    def correr(self):
        print("A bicicleta esta correndo...")

meu_veiculo_1 = Bicicleta("Laranja", "Fuji", 2010, 5000)
# meu_veiculo_1 é em si o objeto que é definido pela classe 'Bicicleta'

# É a forma de chamar os comportamentos do objeto
meu_veiculo_1.buzinar()
meu_veiculo_1.parar()
meu_veiculo_1.correr()

# É a forma de chamar as caracteristicas do objeto
print(meu_veiculo_1.cor)
print(meu_veiculo_1.modelo)
print(meu_veiculo_1.ano)
print(meu_veiculo_1.valor)

# Na hora de chamar o que ele esta fazendo é naverdade isso, mas são sintaxes equivalentes
Bicicleta.buzinar(meu_veiculo_1)    # meu_veiculo_1.buzinar()
Bicicleta.parar(meu_veiculo_1)      # meu_veiculo_1.parar()
Bicicleta.correr(meu_veiculo_1)     # meu_veiculo_1.correr()
```

**Forma de Retornar todo o Objeto**

Existem algumas formas de retornar o objeto iteiro, porem deixarei o exemplo de duas, uma mais maunal e outra mais complexa porem automatica.

**__ str __** = Um metodo que muda o que aparece quando o usuario chama o obejto, se não for colocado retorna informações com a memoria 

**__ class __.__ name __** = Retorna o nome da classe, assim se o nome for alterado, não é preciso mudar no codigo. 

FORMA MANUAL

```Python
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def __str__(self):
        return f"{self.__class__.__name__}: Cor = {self.cor}, Modelo = {self.modelo}, Ano = {self.ano}, Valor = {self.valor}"
    
bike = Bicicleta("Laranja", "Fuji", 2010, 5000)

print(bike)
# Bicicleta: Cor = Laranja, Modelo = Fuji, Ano = 2010, Valor = 5000
```
MANEIRA MAIS OPTIMIZADA

**__ dict __** = Retorna um dicionario com todos os valores e chaves da classe chamada

```Python
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} dela é {valor}' for chave, valor in self.__dict__.items()])}"
    # o ''.join faz a substituição da saida em lista para uma saida em string
    
bike = Bicicleta("Laranja", "Fuji", 2010, 5000)

print(bike)
# Bicicleta: cor dela é Laranja, modelo dela é Fuji, ano dela é 2010, valor dela é 5000

```

## Construtores e Destruidores

### Método Construtor / Inicializador
O metodo construtor é sempre executado quando uma nova instância da classe é criada. Nesse método inicializamos o estado do nosso Objeto. Para declarar o **método construtor** da classe, criamos um método com o nome __ init __

```Python
class Cachorro: 
    def __init__(self, raca, cor):
        print(f"Iniciando a classe {self.__class__.__name__}")
        self.raca = raca
        self.cor = cor

c = Cachorro("camarelo", "amarelo")
# Iniciando a classe Cachorro
```

### Método Destrutor
O metodo destrutor é sempre executado quando uma instância (objeto) é destruida. Destrutores em Python não são tão necessários quanto em C++ já que o Python tem um coloetor de lixo que lida com o gerenciamento de memória automaticamente. Para declarar o método destrutor da classe, criamos um método com o nome __ del __

**__ del __** = Quando ele é utilizado que vai acontecer é: antes de ser deletado o objeto ira realizar o que foi definido na caracteristica

**obs.:** Por conta do __ del __ sempre ser executado quando o objeto é deletado, em alguns momentos dentro do proprio codigo isso vai aconteser, dois exemplos são se eu inicializar o objeto dentro de uma função, quando a função der return, ela vai deletar o objeto, e também quando o código terminar de ser executado.
```Python
class Cachorro: 
    def __init__(self, raca, cor):
        self.raca = raca
        self.cor = cor

    def __del__(self):
        print(f"Deletando o objeto de classe {self.__class__.__name__}")

c = Cachorro("camarelo", "amarelo")

del c
# Deletando o objeto de classe Cachorro
```

## Herança em POO
Em programação herança é a capacidade de uma classe filha derivar ou herdar as caracteristicas e comportamentos da classe pa(base).

### Beneficios:
- Representa bem os relacionamentos no mundo real.

- Fornece a reutilização de códigos, não precisando escrever o mesmo código repetidamente. Além disso, permite adicionar mais recursos a uma classe sem modificá-la.

- É de natureza transitiva, o que significa que, se a classe B herdar da classe A, todas as subclasses de B herdarão automaticamente da classe A também.

### Código Base
```Python
class A:
    pass

class B(A):
    pass    # a classe B herda a classe A
```

### Herança Simples e Múltiplas
A simples é a padrão como o exemplo de cima

Herança múltipla é quando uma classe filha herda várias classes pai.
```Python
class A:
    pass

class B:
    pass

class C(A, B):
    pass    # C possui os pais A e B
```

### Exemplo Codigo Herança Simples
![alt text](https://imgur.com/4YwozrP)

**super().__ init __(...)** = Essa função é utilizada para puxar as caracteristicas da classe pai, podendo ser com as variaveis literiais ou com o uso de dict.

****kw** = Lembrando **kw quer dizer que a função esta recebendo um dict.

```Python
class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando motor...")

    def __str__(self):
        return F"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    

class Motocicleta(Veiculo):
    def __init__(self, cor, placa, numero_rodas, cilindradas):
        self.cilindradas = cilindradas
        super().__init__(cor, placa, numero_rodas)

    def carteira_permitida(self):
        if (self.cilindradas <= 50):
            print("Carteira ACC")
        else:
            print("Carteira A")

class Carro(Veiculo):
    def __init__(self, nivel_fume, **kw):
        self.nivel_fume = nivel_fume
        super().__init__(**kw)

    def legalidade(self):
        if (self.nivel_fume <= 0.75):
            print("Carro legal")
        else:
            print("Carro ilegal")

class Caminhao(Veiculo):
    def __init__(self, carga = False, **kw):
        self.carga = carga
        super().__init__(**kw)
    
    def carregado(self):
        if (self.carga):
            print("Caminhao carregado")
        else:
            print("Caminhao sem carga")

moto = Motocicleta(cor = "Preto", placa = "abc-0000", numero_rodas = 2, cilindradas = 60)
moto.ligar_motor()
moto.carteira_permitida()
print(f'{moto}\n')

carro = Carro(cor = "Marrom", placa = "def-1111", numero_rodas = 4, nivel_fume=0.65)
carro.ligar_motor()
carro.legalidade()
print(f'{carro}\n')

caminhao = Caminhao(cor="Cinza", placa="ghi-2222", numero_rodas=8, carga=True)
caminhao.ligar_motor()
caminhao.carregado()
print(f'{caminhao}\n')
```

### Exemplo Codigo Herança Múltipla

![alt text](https://imgur.com/g5UFuEZ)

**'nome classe'.__ mro __** = essa função retorna a prioridade de execução da classe

```Python
class Animal:
    def __init__(self, numero_de_patas):
        self.numero_de_patas = numero_de_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico
        
# class Cachorro(Mamifero):
#     pass

class Gato(Mamifero):
    def __init__(self, raca, **kw):
        super().__init__(**kw)
        self.raca = raca
    
    def miado(self):
        print("Miau!!!")

# class Leao(Mamifero):
#     pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, veneno = True, **kw):
        print(Ornitorrinco.__mro__)
            # (<class '__main__.Ornitorrinco'>, <class '__main__.Mamifero'>, <class '__main__.Ave'>, <class '__main__.Animal'>, <class 'object'>)
        super().__init__(**kw)
        self.veneno = veneno

    def venenoso(self):
        if self.veneno:
            print("Venenoso! Cuidado")
        else:
            print("Não venenoso")

cerveja = Gato(numero_de_patas=4, cor_pelo="Pelado", raca="sphynx")

perry = Ornitorrinco(numero_de_patas=4, cor_pelo="Verde", cor_bico="Laranja", veneno=False)

cerveja.miado()
print(cerveja)
print()

perry.venenoso()
print(perry)
print()
```

## Encapsulamento em POO

Encapsulamento é um dos conseitos fundamentais em POO. Ele descreve a ideia de agrupar dados e os métodos que manipulam essse dados em uma unidade. Isso Impõe restrições ao acesso direto a variáveis e métodos e pode evitar a modificação acidental de dados. Para evitar alterações acidentais, a variável de um objeto só pode ser alterada pelo método desse objeto.

![alt text](https://imgur.com/asdasdasd-hjgP2CO)

Esse é um exeplo onde a váriavel *saldo* é encapsulada, ou seja não é possivel altera-la de maneira direta, mas sómente pelos métodos *depositar* e *sacar*

obs.: o sinal de **'-'** simboliza que o metodo/variavel é restrito enquanto o sinal de **'+'** simboliza que é "publico"

### Recursos Públicos e Privados
Em linguagens como Java e C++, existem palavras reservadas para definir o nível de acesso aos atributos e métpdps da classe. Já em **Python não exitem palavras reservadas para isso**, porém usamos **convenções** no nome do recurso, para definir se a váriavel é pública ou privada.

### Definição:
- **Público:** Pode ser acessado fora da classe.
- **Privado:** Só pode ser acessado pela classe.

**obs.:** Por padrão quando a variável é iniciada com **'_'** exemplo: **'_saldo'**
```Python 
class Conta():
    def __init__(self, saldo, numero_agencia):
        self._saldo = saldo     # percebe-se que a variavel chama _saldo
        self.agencia = numero_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor


conta = Conta(100, "0087")
conta.depositar(20)
conta.sacar(10)
```
Como é possivel ver eu posso mudar o valor de 'saldo' de qualquer forma mesmo não usando 'depositar' ou 'sacar', porem não é recomendado isso por conta da convenção do _.

**ENTÂO RESPEITA O '_'!!!!**

## Propriedades
Com o property() do Python, você pode criar atributos gerenciados em suas classes. Você pode usar atributos gerenciados, também conhecidos como propriedades, quando precisar modificar sua implementação interna sem alterar a API pública da classe.

**@property** = Basicamente tranforma um metodo em um atributo ou seja, agora pode-se usar o metodo com uma sintaxe de atributo

obs.: Mais explicação: o que faz o property() é definir o que vai acontecer com o atributo se eu usar operadores, palavras reservadas, etc, como =, deletar.

```Python 
class Foo:
    def __init__(self, x = None):
        self._x = x #_x

    @property   # define que pode retornar valor
    def x(self):
        return self._x or 0 # se existir um valor para x retorna x se nao 0
    
    @x.setter   # define que ele pode ter um valor atribuido
    def x(self, vluea):
        _x = self._x or 0
        _value = value or 0
        self._x = _x + _value

    @x.deleter  # define como o valor vai ser "deletado"
    def x(self):
        self._x = -1

foo = Foo(10)
print(foo.x) #10
foo.x = 20
print(foo.x) #30
del foo.x
print(foo.x) #-1
```
Um outro exemplo um pouco mais útil seria uma forma de eu enviar o ano de nascimento e me retornar a idade de forma direta sem ter que fazer a utilização de uma "função".
```Python
class Pessoa():
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento

eu = Pessoa("Felipe", 2004)
print(f'Nome: {eu.nome}\nIdade: {eu.idade}')
# Nome: Felipe
# Idade: 20
```
E no final das contas Sim podemos só fazer um def padrão e utliza-lo, porem esse não é muito o padrão da escrita em python

## Polimorfismo
A palavra porlimorfismo significa ter muitas formas. Em programação, polimorfismo significa o mesmo node de função (mas assinaturas diferentes), sendo usado para tipos diferentes.

Um exemplo é o len(). que retorna em diferentes tipos de tipos.
```Python
len("Python")       # retorna quantidade de letras

len([10, 20, 30])   # retorna quantidade de itens na lista
```

### Mesmo método com comportamento diferente
Na herança, a classe filha herda os métodos da classe pai. No entento, é possivel modificar um método em uma classe filha herdade da classe pai. Isso é particularmente útil nos casos em que o método herdado da classe pai não se encaixa perfeitamente na classe filha.
```Python
from ssl import PROTOCOL_TLSv1_2


class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

def plano_de_voo(obj):
    obj.voar()


p1 = Pardal()
p2 = Avestruz()

plano_de_voo(p1)    # Voando...
plano_de_voo(p2)    # Avestruz não voa

plano_de_voo(Pardal())      # Voando...
plano_de_voo(Avestruz())    # Avestruz não voa
```

## Variáveis de classe e Variáveis de Instância
Todos os objetos nascem com o mesmo numero de atributos de classe e de instância. Atributos de instância são diferentes para cada objeto (cada objeto tem uma cópia), já os atributos de classe são compartilhados entre os objetos.

Basicamente Variáveis de Classe são variaveis que não são individuais para cada objeto, elas são globias para todos os objetos do codigo ou seja se eu trocar o valor de uma delas, trocara para todos os objetos ja criados e também aqueles que ainda serão criados.

```Python
class Estudante:
    escola = "DIO"  # essa é uma variavel de classe

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
aluno1 = Estudante("Felipe", 535610)
aluno2 = Estudante("Michelle", 626738)

print(aluno1)
print(aluno2)
Estudante.escola = "trocada"    # Assim posso trocar permanentemente uma variavel de classe
print(aluno1.escola)
print(aluno2.escola)

aluno3 = Estudante("Lucas", 422334)

print(aluno1)
print(aluno2)
print(aluno3)
```

## Métodos de classe e Métodos estáticos
### Métodos de classe
Métodos de classe estão ligados à classe e não ao objeto. Eles têm acesso ao estado da classe, pois recebem um parâmetro que aponta para a classe e não para a instância do objeto.

### Métodos estáticos
Um método estático não recebe um primeiro argumento explícito. Ele também é um método vinculado à classe e não ao objeto da classe. Este método não pode acessar ou modificar o estado da classe. Ele está presente em uma classe piorque faz sentido que o método esteja presente na classe.

### classe X estático
- Um método de classe recebe um primeirp parâmetro que aponta para a classe, enquanto um método estático não.
- Um método de classe pode acessar ou modificar o estado da classe enquanto um método estático não pode acessá-lo pi modificá-lo.

### Quando utilizar cada um
- Geralmente usamos o método de classe para criar métodos de fábrica.
- Geralmente usamos métodos estáticos para criar funções utilitárias.

### No Código

**@classmethod** = É a forma de definir que o método a baixo é um metodo de classe.

**@staticmethod** = É uma forma de "enfeitar" o codigo para diser que o método é estático.
```Python
class Pessoa: 
    def __init__(self, nome, idade, cor_cabelo):
        self.nome = nome
        self.idade = idade
        self.cor_cabelo = cor_cabelo
    
    @classmethod
    def criar_apartir_data_nascimento(cls, nome, dia, mes, ano, cor_cabelo):
        idade = 2024 - ano
        return cls(nome, idade, cor_cabelo)
    
    @staticmethod
    def maior_de_idade(idade):
        return idade >= 18
    
    def __str__(self):
        return F"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

eu = Pessoa.criar_apartir_data_nascimento("felipe", 30, 12, 2004, "preto")
print(eu)
print(Pessoa.maior_de_idade(19))
print(Pessoa.maior_de_idade(10))
```

## Classes Abstratas

### Interfaces
Interfaces definem o que uma classe deve fazer e não como.

O conceito de interface é definir um contrato, onde são declarados os métodos (o que deve ser feito) e suas respectivas assinaturas. Em Python utilizamos classes abstratas para criar contratos. classes abstratas não podem ser instanciadas.

## Criando classes abstratas com o metodo ABC
*obs.: ABC (Abstract Base Class)*

Por padrão, o Python não fornece classes abstratas. O Python vem com um módulo que fornece a base para definir as classes abstratas, e o nome do módulo é ABC. O ABC funciona decorando métodos da classe base como abstrato e, em seguida, registrando classes concretas como implementações da base abstrata. Um método se torna abstratp quando decorado com **@abstractmethod**

Basicamente assim a classe abstrata obriga o código a seguir suas "regras".

**@abstractmethod** = Define os métodos da classe abstrata

**@abstractproperty** = Define as propriedades da classe abstrata.

```Python
from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass
    

class ControleTV(ControleRemoto):
    def ligar(self):
        print("TV ligada")
    
    def desligar(self):
        print("TV desligada")

    @property
    def marca(self):
        return "Samsung"

class ControleAr(ControleRemoto):
    def ligar(self):
        print("Ar Condicionado ligada")
    
    def desligar(self):
        print("Ar Condicionado desligada")

    @property
    def marca(self):
        return "LG"
    
controle1 = ControleTV()
controle2 = ControleAr()

controle1.ligar()
controle1.desligar()
print(controle1.marca)

print()

controle2.ligar()
controle2.desligar()
print(controle2.marca)
```

## Decoradores
### Inner functions
são funções definidas dentro de outras fuções, são chamadas também de funções internas.

```Python
def pai():
    print("escrevendo da pai() função")

    def filho_1():
        print("Escrevendo da filho_1 função")

    def filho_2():
        print("Escrevendo da filho_2 função")

    filho_2()
    filho_1()
pai()
```
Uma forma de utilizar esse tipo de função.
```Python
def calcular(operacao):
    def somar(a, b):
        return a + b

    def subtrair(a, b):
        return a - b

    if (operacao == "+"):
        return somar(a,b)
    else:
        return subtrair(a,b)

resultado = clacular("-")(10,8)
print(resultado)
    # 2 
```
Como é possivel ver acima, da para enviar os valores para mais de uma função, se ela possuir funções internas.

Outra coisa que podemos fazer é retornar uma funcão em outra função.

```Python
def calculadora(op):
    def soma(a, b):
        return a + b
    def sub(a, b):
        return a - b
    def mult(a, b):
        return a * b
    def div(a, b):
        return a / b

    match op:
        cases "+":
            return soma
        cases "-":
            return sub
        cases "*":
            return mult
        cases "/":
            return div

operacao = calculadora("+")
print(operacao(5,6))  # 11

operacao = calculadora("-")
print(operacao(5,6))  # -1
``` 

## decorador simples

Usamos decoradores para colocar mais comportamentos dentro de outras funções.

```Python
def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a funcao")
        funcao()
        print("Faz algo depois de executar a funcao")

    return envelope

def ola_mundo():
    print("Hello World!")

ola_mundo()
print()

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()
```

### Açúcar sintático
O Python permite que você use **decoradores de maneira mais simples com o símbolo @**.


Mesmo exemplo de cima.
```Python
def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a funcao")
        funcao()
        print("Faz algo depois de executar a funcao")

    return envelope

@meu_decorador
def ola_mundo():
    print("Hello World!")

# não é mais preciso a linha de atribuição a funcao (ola_mundo = meu_decorador(ola_mundo))

ola_mundo()
```

### Funões de decoração com argumentos
Podemos usar *args e **kwargs na função interna, com isso ela aceitará um número arbitrário de argumentos posicionais e de palavras-chave.
```Python
def duplicar(funcao):
    def envelope(*args, **kwargs):
        print("Executa primeira vez:")
        funcao(*args, **kwargs)
        print("Executa uma segunda vez:")
        funcao(*args, **kwargs)
    return envelope

@duplicar
def aprendendo(tecnologia):
    print(f"Eu estou aprendendo {tecnologia}")

aprendendo("Python")
```

### retornando valores de funções decoradas

O decorardor pode decidir se retorna o valor da função decorada ou não, Para que o valor seja retornado a função de **envelope** deve retornar o valor da finção decorada.

```Python
def duplicar(funcao):
    def envelope(*args, **kwargs):
        print("Executa primeira vez:")
        funcao(*args, **kwargs)
        print("Executa uma segunda vez:")
        resultado = funcao(*args, **kwargs)
        
        return resultado

    return envelope

@duplicar
def aprendendo(tecnologia):
    print(f"Eu estou aprendendo {tecnologia}")
    return tecnologia.upper()

tecnologia = aprendendo("Python")
print("\n",tecnologia)
```
### Intropecção
introspecção é a capacidade de um objeto saber sobre seus próprios atributos em tempo de execução 

Da forma que foi programado acima, quando pefirmos as "informações" da função, sua **Introspecção** sera comprometida:

![alt text](https://i.imgur.com/KoqCXZz.png)

```Python
import functools

def duplicar(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        print("Executa primeira vez:")
        funcao(*args, **kwargs)
        print("Executa uma segunda vez:")
        resultado = funcao(*args, **kwargs)
        
        return resultado

    return envelope

@duplicar
def aprendendo(tecnologia):
    print(f"Eu estou aprendendo {tecnologia}")
    return tecnologia.upper()

print(print)
print(print.__name__)
print()
print(aprendendo)
print(aprendendo.__name__)

# ==================== SAIDA ====================
# <built-in function print>
# print

# <function aprendendo at 0x00000189EE189B20>
# aprendendo
```

## Interadores e Geradores
Esses são conceitos poderosos que nos permitem trabalhar com sequências de maneira eficiente.

### Interáveis
Interaveis são todos os tipos de variaveis que possum uma sequencia de valores, exmplos: listas, linhas de um arquivo de texto, sequencia de caracters, etc.

### Iterador
Em Python, um interador é um obheto que contem um nimero contavel de valores que podem ser iterados, o que sugnifica que voce pode percorrer todos os valores. O protocolo do iterador é uma maneira do Python fazer a interação de um objeto, que consiste em dois métodos especiais "__ ite __() " e " __ next __()".

Um exemplo de uso é **Ler arquivos grandes**

Exemplo código:
 É dado uma lista e retorna essa mesma lista porem com os valores dobrados

 **raise StopIteration** = é uma linha  obrigatoria, pois informa ao compilador que foi terminado a interação

```Python
class MeuInterator:
    def __init__(self, numeros:list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        tamanho = len(self.numeros)
        if (self.contador < tamanho):    
            numero = self.numeros[self.contador] * 2
            self.contador += 1
            return numero
        else:
            raise StopIteration

for i in MeuInterator(numeros = [1, 2, 3, 4, 5]):
    print(i)

# 2, 4, 6, 8, 10
```

### Geradores
São tipos especiais de interadores, ao contrário das listas ou outros interáveis, não armazenam todos os seus valores na memória. 

São definidos usando funções regulares, mas, ao invés de retornar valores usando "return", utilizam "yield"

### Características de geradores 
- Uma vez que um item gerado é consumido, ele é esquecido e não pode ser acessado novamente.
- O estado interno de um gerador é mantido entre chamadas.
- A execução de um gerador é pausada na declaração "yield" e retomada daí na próxima vez que ele for chamado.

#### Um exemplo:
##### Recuperando dados de uma API
- Solicitar dados por páginas (paginação)
- Fornece um produto por vez entre as chamadas.
- Quando todos os produtos de uma página forem retornados, verificar se existem novas páginas.
- Tratar o consumo da API como uma lista Python.

```Python
import requests

def fatch_products(api_url, max_pages = 100):
    page = 1
    while page <= max_page:
        response = requests.get(f"{api_url}?page={page}")
        data = response.json()
        for product in data['products']:
            yield product
        if 'next_page' not in data:
            break
        page += 1

# uso do gerador
for product in fetch_products("https://api.example.com/products"):
    print(product['name'])
```

#### Outro exemplo extremamente mais básico

```Python
def meu_gerador()
    yield "texto"

for i in meu_gerador()
print(i)
```

#### Mesmo exemplo do interador
```Python
def meu_interator(numeros:list[int]):
    for numero in numeros:
        yield numero * 2 

for i in meu_gerador(numeros = [1, 2, 3]):
    print(i)
```

### Quando usar cada um

Gerador:
***Um código mais simples, e/ou mais optimizada:***

interador: ***Um código mais complexo (ex: arvore binaria)***

## Lidando com Data, Hora e Fuso horário
### Módulo datetime
O módulo 'detetime' em Python é usado para lidar com datas e horas. Ele possui várias classes úteis como date, time e timedelta.
### DATA
```Python
import datetime

ano = 2024
mes = 7
dia = 12

data = datetime.date(ano, mes, dia)

print(data)
# 2024-07-12

data = datetime.date.today()
print(data)
# (DATA DE HOJE)
```
### HORA
```Python
import datetime

hora = 14
minuto = 44
segundo = 17
microsegundo = 15323

hora = datetime.time(hora, minuto, segundo, microsegundo)

print(time)
# 14:44:17.15323

data = datetime.date.today()
print(data)
# (HORA DE AGORA)
```
### DATA E HORA
```Python
import datetime

ano = 2024
mes = 7
dia = 12
hora = 14
minuto = 39
segundo = 53
microsegundo = 12322
fold = [0, 1]

data_e_hora = datetime.datetime(ano, mes, dia, hora, minuto, segundo, microsegundo, fold)

print(data_e_hora)
# 2024-07-12 14:39:53.12322

print(data_e_hora.time())   # somente hora
# 14:39:53.12322

print(data_e_hora.date())   # somente data
# 2024-07-12

data = datetime.datetime.today()
print(data)
# (DATA E HORA DE AGORA)
```

## Manipulação do objeto date, time e datetime
### Soma e Subtração de "tempos"
```Python
import datetime

data = datetime.datetime(2024, 7, 12, 14, 48)
print(data)
# 2024-7-12 14:48:00

data += datetime.timedelta(weeks=1)
print(data)
# 2024-7-19 14:48:00
```

### Soma e Subtração de DATAS
```Python
import datetime

data = datetime.datetime.now()
data2 = datetime.datetime.now() + datetime.timedelta(weeks=1)

data_resultante = data2 - data
print(data_resultante)
# 7 days, 0:00:00
```

### Converção e Formatação de data e hora
Usamos para fazer essas converções os métodos 'strftime' (string format time) e 'strptime' (string parse time)

```Python
import datetime

data = datetime.datetime.now()

data_convertida = data.strftime("%d/%m/%Y %H:%M")   # converte para a forma que você quer
print(data_convertida)
# 12/07/2023 15:42

data_string = "12/07/2023 15:42"
data = datetime.datetime.strptime(data_string, "%d/%m/%Y %H:%M")    # coneverte novamente ao formato padrão
print(data)
# 2023-07-12 15:42:00
```

### Trabalhando com timezone
obs.: ```datetime.utcnow()``` é um comando do proprio datetime para retornar o horario UTC

Trabalhando com datas e horas é comum a necessidade de usar fuso horário. Para isso usamos ```import pytz```

Se não rodar tem que fazer um ambiente virtual(não entendi muito bem mesmo)

```Python
import datetime
import pytz

data = datetime.datetime.now(pytz.timezone("Europe/Oslo"))

print(data) 
```

## Gerenciamento de pacotes, conveções e boas praticas com Python
### Pacotes
Pacotes são módulos que podem ser instalados e utilizados em seus programas Python. Eles permitem que você utilize código que foi escrito por outras pessoas, economizando tempo e esforço.
### O papel do pip
Pip é o gerenciador de pacotes do Python. Ele nos permite instalar, atualizar e remover pacotes facilmente. Ele se comunica com o [PyPI](https://pypi.org) (Python Package Index), que é onde a maioria dos pacotes Python são armazenados.

```Batchfile
pip install numpy       # Instala um pacote/biblioteca na sua versão Python que esta ativa no ambiente

pip uninstall numpy     # Deleta o pacote/biblioteca

pip list    # Mostra todos os pacote/biblioteca instalados
```

### Uso de ambientes virtuais
Ambientes virtuais, como os criafos por venvs, nos permitem manter as dependências de diferentes projetos, isso é importante para evitar conflitos entre versoes de pacotes.

#### Criando uma maquina virtual de Python
obs.: Normalmente o 'nome' é o nome do projeto que esta sendo feito na quela maquina 
```CMD
python3 -m venv 'nome'env   
source myenv/bin/activate

pip deactivate  # desativa o ambiente virtual
```

### Comandos do pip
```Batchfile
pip install nome_do_pacote              # instala o pacote no ambiente

pip unistall nome_do_pacote             # deleta o pacote no ambiente

pip list                                # lista todos os instalados no ambiente

pip install --upgrade nome_do_pacote    # atualiza o pacote
```

### Gerenciando dependências com Pipenv
Pipenv é uma ferramenta de gernciamento de pacotes que combina a gestão de dependências com a criação de ambiente virtual para seus projetos e adiciona/remove pacotes autokmaticamente do arquivo Pipfile conforme você instala e desinstala pacotes.

**INSTALE O PIPENV NA MAQUINA PARA FUNCIONAR DE MANEIRA GLOBAL EM TODAS AS MAQUINAS VIRTUAIS**
```Batchfile
pip install pipenv

pipenv install numpy

pipenv unistall numpy

pipenv lock
```
