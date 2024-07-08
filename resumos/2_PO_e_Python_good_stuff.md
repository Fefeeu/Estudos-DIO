
## Sumário
|       |
|-------|
||

# Programação Orientada a Objetos
## O que é?
O paradigma de programação orientada a objetos estrutura o código abstraindo problemas em objetos do mundo real, facilitando o entendimento do código e tornando-o mais modular e extensível. Os dois conceitos chaves para aprenser POO são: **Classes** e **Objetos**.
### O que são Classes e Objetos:
Uma ***classes*** define as características e comportamentos de um ***objeto***, porém não conseguimos usá-las diretamente. Já os ***objetos*** podemos usá-los e eles possuem as características e comportamentos que foram definidos pelas ***classes***.

***Classes*** são partes mais abstratas 

## **Criando uma Classe e Objeto**

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

## **Construtores e Destruidores**

### **Método Construtor / Inicializador**
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

### **Método Destrutor**
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

## **Herança em POO**
Em programação herança é a capacidade de uma classe filha derivar ou herdar as caracteristicas e comportamentos da classe pa(base).

### Beneficios:
- Representa bem os relacionamentos no mundo real.

- Fornece a reutilização de códigos, não precisando escrever o mesmo código repetidamente. Além disso, permite adicionar mais recursos a uma classe sem modificá-la.

- É de natureza transitiva, o que significa que, se a classe B herdar da classe A, todas as subclasses de B herdarão automaticamente da classe A também.

### **Código Base**
```Python
class A:
    pass

class B(A):
    pass    # a classe B herda a classe A
```

### **Herança Simples e Múltiplas**
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

## **Encapsulamento em POO**

Encapsulamento é um dos conseitos fundamentais em POO. Ele descreve a ideia de agrupar dados e os métodos que manipulam essse dados em uma unidade. Isso Impõe restrições ao acesso direto a variáveis e métodos e pode evitar a modificação acidental de dados. Para evitar alterações acidentais, a variável de um objeto só pode ser alterada pelo método desse objeto.

![alt text](https://imgur.com/asdasdasd-hjgP2CO)

Esse é um exeplo onde a váriavel *saldo* é encapsulada, ou seja não é possivel altera-la de maneira direta, mas sómente pelos métodos *depositar* e *sacar*

obs.: o sinal de **'-'** simboliza que o metodo/variavel é restrito enquanto o sinal de **'+'** simboliza que é "publico"

### **Recursos Públicos e Privados**
Em linguagens como Java e C++, existem palavras reservadas para definir o nível de acesso aos atributos e métpdps da classe. Já em **Python não exitem palavras reservadas para isso**, porém usamos **convenções** no nome do recurso, para definir se a váriavel é pública ou privada.

### ***Definição:***
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

## **Propriedades**
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

## **Polimorfismo**
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