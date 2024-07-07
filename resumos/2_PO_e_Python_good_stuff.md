
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

### Método Construtor / Inicializador 
O metodo construtor é sempre executado quando uma nova instância da classe é criada. Nesse método inicializamos o estado do nosso Objeto. Para declarar o **método construtor** da classe, criamos um método com o nome __ init __

### **Método Destrutor**
O metodo destrutor é sempre executado quando uma instância (objeto) é destruida. Destrutores em Python não são tão necessários quanto em C++ já que o Python tem um coloetor de lixo que lida com o gerenciamento de memória automaticamente. Para declarar o método destrutor da classe, criamos um método com o nome __ del __

**__ del __** = Quando ele é utilizado que vai acontecer é: antes de ser deletado o objeto ira realizar o que foi definido na caracteristica
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