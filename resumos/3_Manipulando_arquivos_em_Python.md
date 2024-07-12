## Sumário
|       |
|-------|
||

## 📝 Documentação 
-  [sintaxes](https://pythoniluminado.netlify.app)
- [Repositório DIO](https://github.com/digitalinnovationone/trilha-python-dio)
-  [Python.org](https://docs.python.org/3/)

## Obnjetivo Geral
Como abrir, ler, escrever e gerenciar arquivos em Python. Trabalhando com os formatos txt e csv.

Um arquivo é um container no computador onde as informações são armazenadas em formato diital. Existem dois tipos de arquivos que podemos manipular em Python: arquivos de texto e arquivos binarios(que são melhores por usar menos memoria)

## Abrindo e Fechando arquivos
Para manipular arquivos em Python, primeiro precisamos abrir-los. Usamos a função ```open()``` para isso. Quando terminamos de trabalhar com o arquivo, usamos a função ```close()``` para liberar recursos computacionais.

```Python
file = open("example.txt", "r")
# FAZEMOS ALGO COM O ARQUIVO
file.close()
```

#### Modos de abertura de arquivo
Existem diferentes modos para abrir um arquivo, como somente leitura ('r'), gravação ('w') e anexar ('a'). O modo de abertura deve ser escolhido de acordo com a operação que iremos realizar no mesmo.

## Lendo um arquivo
O ```file.read()``` pega todo o arquivo e coloca em uma string.
```Python
file = open("example.txt", "r")
print(file.read())

file.close()
```

O ```readline()``` retorna linha por linha do arquivo

```Python
file = open("example.txt", "r")
print(file.readline())  # linha 1
print(file.readline())  # linha 2
print(file.readline())  # linha 3
print(file.readline())  # linha 4

file.close()

#Uma dica:
file = open("example.txt", "r")

while len(linha := arquivo.readline()): #isso retorna linha por linha todas as linhas, ja que o que esta sendo feito é medir o tamanho da string e se ela for 0(false) o while se encerra
    print(linha)

file.close()
```
O ```readlines()``` (obs.: add s) retorna todas as linhas do arquivo em uma lista de strings,

```Python
file = open("example.txt", "r")
print(file.readlines())

file.close()
```

## Escrevendo em um arquivo
Podemos usar ```write()``` ou ```writelines()``` para escrever em um arquivo. Lembrando de abrir o arquivo da maneira correta.

```Python
file = open("example.tx", "w")
file.write("Olá, mundo!")   # escreve tudo de uma vez

file.close()
```
```Python
file = open("example.tx", "w")
file.writelines("Olá, mundo!")   # caracter por caracter

file.writelines(["Sairia", "Assim", "O", "Texto"]) # tbm pode ser usado para ler uma lista de strings
# SairiaAssimOTexto

file.close()
```

## Gerenciando arquivos e diretórios
Podemos criar, renomar e excluir arquivos e diretorios usando os módulos ```os``` e ```shutil```.

```Python
import os
import shutil

import pathlib import path

os.mkdir("exemplo") # cria um arquivo com esse nome

os.rename("exemplo", "texto.txt")   # renomeia o arquivo

os.remove("texto.txt")  # deleta o arquivo

shutil.move("texto.txt", "destino") # move o arquivo para o diretorio de destino

print(__files__)    # o caminho até o diretorio onde o arquivo esta sendo executado junto do arquivo
ROOT_PATH = Path(__file__).parent   # o mesmo que o de cima porem excluindo o arquivo em si ou seja dó o caminho

os.mkdir(ROOT_PATH / "exemplo") # cria um arquivo com esse nome no local que o programa esta todando

os.rename(ROOT_PATH / "exemplo", ROOT_PATH / "texto.txt")   # renomeia o arquivo no local que o programa esta todando

os.remove(ROOT_PATH / "texto.txt")  # deleta o arquivo no local que o programa esta todando

shutil.move(ROOT_PATH / "texto.txt", "destino.txt") # move o arquivo no local que o programa esta todando para o diretorio de destino
```

## Tratamento de exceções em manipulação de arquivos
### Exceções mais comuns:
- **FileNotFoundError:** Lançada quando o arquiovo que está sendo aberto não pode ser encontrado no diretório especificado.

- **PermissionError:** Lançada quando ocorre uma tentativa de abrir um arquivo sem as permissçoes adequadas para leitura ou gravação.

- **IOError:** Lançada quando ocorre um erro geral de E/S (entrada/saída) ao trabalhar com o arquivo, como problemas de permissão, falta de espaço em disco, entre outros.

- **UnicodeDecodeError:** Lançada quando ocorre um ero ao tentar decodificar os dados de um arquivo de texto usando uma codificação inadequada.

- **UnicodeEncodeError:** Lançado quando ocorre um erro ao tentar codificar dados em uma determinada codificação ao gravar em um arquivo de texto.

- **IsADirectoryError:** Lançada quando e feira uma tentativa de avrir um diretório em vez de um arquivo de texto.

```Python
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    file = open(ROOT_PATH / "non_existent_file.txe", "r")
except FileNotFoundError as exc:
    print("Arquivo não encontrado")
    print(exc)
except IsADexcirectoryError as exc:
    print(f"Não foi possivel abri o arquivo: {exc}")
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")
except Exception as exc:
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")
```

## Boas praticas
Use o gerenciamento de contexto(context manager) com a declaração ```with```. O gerenciamento de contexto permite trabalhar com o arquivos de forma segura, garantindo que eles sejam fechados corretamente, mesmo em caso de exceções.
```Python
from pathlib import Path

ROOT_PATH = Path(__file__).parent

with open(ROOT_PATH / "arquivo.txt", "r") as arquivo:
    # operações de leitura/gravacao no arquivo
```
Verificar se o arquivo abriu corretamente antes de trabalhar com ele.
```Python
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / "arquivo.txt", "r") as arquivo:
    # operações de leitura/gravacao no arquivo
except IOError:
    print("Não foi possivel abrir o arquivo")
```

Certificar-se de usar a codificação correta ao ler ou gravar arquivos de texto. O argumento ```encoding``` da função ```open()``` permite especificar a codificação.
```Python
from pathlib import Path

ROOT_PATH = Path

try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding="utf-8") as arquivo:
except IOError:
    print("Não foi possivel abrir o arquivo")
```

## Trabalhando com arquivos CSV
