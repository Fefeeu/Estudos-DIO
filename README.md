# DIO | Resumos
repositório dedicado para resumos e explicações do curso [Python AI Backend Developer](https://web.dio.me/track/coding-future-vivo-python-ai-backend-developer)

## Git e GitHub
### • 📝 Documentação:
- [Documentação Git](https://git-scm.com/doc)
- [Documentação GitHub](https://docs.github.com/)
- [Resumos em um Repositorio](https://github.com/elidianaandrade/dio-curso-git-github)
### • 💻 Comandos Relacionados
#### •• Comandos basicos do cmd do Windows
```
mkdir "Nome-da-Pasta" //cria uma pasta pelo
mkdir "nome-pasta/nome-pasta/.../Nome-da-Pasta" //cria uma pasta em um endereço especifico
New-Item "Nome-do-Arquivo.extenção" //cria um arquivo
New-Item "nome-pasta/nome-pasta/.../Nome-do-Arquivo.extenção" //cria um arquivo em um endereço especifico
New-Item "nome-pasta/nome-pasta/.../Nome-do-Arquivo.gitKeep" //o arquivo .gitKeep é uma convenção para diretorio vazio
Remove-Item "Nome-do-Arquivo" //remove um arquivo com nome especifico
cd "Nome-da-Pasta" //abre a pasta no cmd
cd.. //retorna para a pasta anterior
ls //lista todos os arquivos e pastas inclusive as ocultas
```
#### •• Comandos para "configurar" toda a pasta do git

```
git init //transforma a pasta que esta aberta no cmd em um repositorio Git
cd .git //abre a pasta oculta .git
cat config //informação sobre as configuraçoes do repositorio
git clone "URL completo de um repositorio do GitHub" "Nome que quer dar para a pastado repositorio" //cria uma pasta de um repositorio git ja existente no pc, obs.: o nome do arquivo depois do URL é opcional, se nao só tera o nome padrao do repositorio
git remote -v //mostra os repositorios que a pasta aberta esta conectada
```
#### •• Comandos para Commits Locais

```
git status //mostra os status da area de trabalho que estamos usandos
git add "Nome-do-Arquivo.extenção" //adiciona na "fila" para enviar(commit) para o repositorio
git add . //adiiona todos os arquivos da pasta na "fila"
git commit -m"comentario-sobre-o-commit"
git commit --amend -m"comentario-sobre-o-comit" //muda o comentario do ultimo commit
git log //mostra as informaçoes do commit realizado
Remove-Item .git //remove a pasta atual de trabalho como uma pasta git
git reset --soft "hash-commit" //reseta o commit para o status do hash ja com 'add' 
git reset --mixed "hash-commit" //reseta o commit para o status do hash sem 'add', não precisa colocar o '--mixed' pois é o reset padrao
git reset --hard "hash-commit" //reseta o comit ignorando e desfazendo ele deixando a "lista" completamente limpa
git reflog //da um log mais detalhado inclusive com os resets
git reset "Nome-do-Arquivo.extenção" //tira o arquivo do 'lista' de commit 
git reset . //tira todos os arquivos do 'lista' de commit
```
#### •• Comandos para Linkar e manejar arquivos Local-GitHub
```
git remote add "Nome-Repositorio-Remoto, por padrao origin" "URL" //vincula a pasta ja existente ao repositorio do URL colocado, linka diretamente a pasta-local-de-repositorio a um repositorio do git, aparentemente só precisa fazer isso na primeira vez na pasta
git push -u origin main //envia o commit final para o repositorio do GitHub
git pull //copia todas as modificaçoes realizadas online o GitHub para o Local da maquina
```
### • 🌿 O que são Branches
Basicamente são ramificações para o projeto.
Exemplo: podendo testar funcionalidades sem alterar a Branche principal(a main)

Um exemplo visual do siginificado de uma branch(no caso a branch teste)
![Um exemplo visual do significado de uma branch](https://i.imgur.com/sLQJfIm.png)
Ela esta "mandando" commits sem alterar a branch principal(main)

#### •• Comandos para Branchs
```
git checkout -b "Nome-para-a-branch" //cria uma branch local para fazer alterações sem mudar a main mantendo ela a salvo
git branch "Nome-para-a-branch" //aparentemente tbm cria a branch
git checkout "Nome-da-branch" //muda para branch colocada
git branch //mostra todas as branchs que existem no momento, e deixa em destaque qual branch "você" se encontra obs.: se colocar '-v' depois da 'branch' aparece mais informações
git merge "Nome-da-branch" //"envia" a branch para a branch que "você" esta
git branch -d "Nome-da-branch" //deleta a branch criada
```
obs.: É recomendado nomear as branchs com [convenções de nome](https://gist.github.com/digitaljhelms/4287848)

#### •• Conflitos para quando se trabalha com branchs
Quando se trabalha com branchs e esta em equipe pode acontecer da haver conflitos na hora de enviar commits, como por exemplo alguem enviar algo que vc esta alterando e quando vc enviar ele ja vai ter alterado algo, entao vai dar um erro avisando o conflito de alterações:

Quando der a mesagem de conflito o que é preiso fazer é dar 'git pull' para receber todas as alterações localmente porem quando receber essas alterações tera uma informação mostrando as alterações em conflito assim você pode escolher qual manter, dai é só enviar novamente após já ter dado 'git pull'.
#### •• Comandos úteis
```
git clone "URL-repositório" --branch "Nome-da-branch" --sigle-branch //clona para o Local sómente a branch escolhida do repositório 
```
obs.: mais comandos em [no cap 3.](https://git-scm.com/book/en/v2).

## 🤝 Formas de Contribuir em um Projetp Open Source
![barra do repositório do github](https://i.imgur.com/3ASLWxw.png)
-**Issues:**
	Uma forma de terceiros fazerem recomendações para alteral algo, corrigir problemas, fazer mudanças, etc..., podendo ser usadas também para quando alguém fazer uma 'Issue' alocar a uma pessoa expecifica para realiza-la.
 
 -**Pull Requests:**
 	Uma forma de pessoas que ja sabem alguma forma de realizar as mesmas coisas dos Issues, porem ela já sabe como realizar, então ela faz um request ja com a solução do "problema", assim podendo alterar de maneira mais fácil o repositório.
