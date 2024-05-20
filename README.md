# DIO | Resumos
repositório dedicado para resumos e explicações do curso [Python AI Backend Developer](https://web.dio.me/track/coding-future-vivo-python-ai-backend-developer)

## Git e GitHub
### •📝 Documentação:
- [Documentação Git](https://git-scm.com/doc)
- [Documentação GitHub](https://docs.github.com/)
### •💻Comandos Relacionados
```
\\comandos cmd windows

mkdir "Nome-da-Pasta" //cria uma pasta pelo
mkdir "nome-pasta/nome-pasta/.../Nome-da-Pasta" //cria uma pasta em um endereço especifico
New-Item "Nome-do-Arquivo.extenção" //cria um arquivo
New-Item "nome-pasta/nome-pasta/.../Nome-do-Arquivo.extenção" //cria um arquivo em um endereço especifico
New-Item "nome-pasta/nome-pasta/.../Nome-do-Arquivo.gitKeep" //o arquivo .gitKeep é uma convenção para diretorio vazio
Remove-Item "Nome-do-Arquivo" //remove um arquivo com nome especifico
cd "Nome-da-Pasta" //abre a pasta no cmd
cd.. //retorna para a pasta anterior
ls //lista todos os arquivos e pastas inclusive as ocultas

git init //transforma a pasta que esta aberta no cmd em um repositorio Git
cd .git //abre a pasta oculta .git
cat config //informação sobre as configuraçoes do repositorio
git clone "URL completo de um repositorio do GitHub" "Nome que quer dar para a pastado repositorio" //cria uma pasta de um repositorio git ja existente no pc, obs.: o nome do arquivo depois do URL é opcional, se nao só tera o nome padrao do repositorio
git remote -v //mostra os repositorios que a pasta aberta esta conectada
git remote add "Nome-Repositorio-Remoto, por padrao origin" "URL" //vincula a pasta ja existente ao repositorio do URL colocado
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