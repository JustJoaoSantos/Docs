# GIT 
## Creating Repository

* $git init
	> cria ou reinicia um repositorio git
* $git add .
	> adiciona todos os arquivos para a stage area
* $git add archive.txt                                    
	> adiciona um arquivo especifico(in this case 'archive.txt) a stage area
* $git commit -m "Title" -m "Message"                               
	> prepara todos os arquivos da fila para serem enviados
* $git status
	> mostra o status do commit

* $git branch -M <new name>                                     
	> rename the Main/Master branch
* $git checkout -b <branch name>
	> Create and switch to a new branch
 
> $git remote add origin <URL.git>                       
	* cria uma conecção com o repositorio remoto
> $git push -u origin main                                
	* envia os arquivos do 'commit' para o repositorio remoto
> $git pull origin main				       
	* puxa os arquivos do repositorio remoto para o local e merge com os locais
	* refere aos comandos git fetch + git merge
* $git clone <URL.git>  
    > e.g git clone <html or ssh .git file> <new name>
	> clona um diretorio remoto
* $clear                                                  
	> limpa o terminal
	
> $git fetch origin main 
- *traz o commit do remoto(origin) para branch local(main)*

---
> $git diff main origin/main
- mostra diferenca entre main(branch) e main(remoto/branch)

## Branches
> $git checkout -b <branch_name>
	* cria e muda para a branch especificada
> $git checkout <branch_name>
	* muda para branch especificada 
> $git branch -v 
	* lista branch e branch commit 
> $git branch -d <branch_name>
	* deleta branch

## Setting Up Remote
* $git remote set-url                                     
	> muda a URL de um remote ja existente, pode mudar de https para ssh ou vice-versa
* $git remote -v                                          
	> verifica a conecção remote
* $git remote rename <old_name> <new_name>                
	> renomeia a conecção remote
* $git remote rm <remote_name>                            
	> remove a URL do remote indicado
* $git config --global user.name 'user_name'              
	> configura o nome de usuario 
* $git config --global user.email 'user_email'            
	> configura o email do usuario

## Generating SSH Key
* $ssh-keygen -t ed25519 -C "your_email@example.com"      
	> gera uma nova ssh key
* Enter a file in which to save the key (/home/you/.ssh/id_ed25519): [Press enter]
* Enter passphrase (empty for no passphrase): [Type a passphrase]
* Enter same passphrase again: [Type passphrase again]
* $eval "$(ssh-agent -s)"                                 
	> inicia o ssh agent
* Agent pid 59566
* $ssh-add ~/.ssh/id_ed25519                              
	> adiciona a ssh key ao ssh agent

## Logs and COmmit History
* $git log                                                
	> mostra o log de commits
* $git log --oneline                                      
	> filtra o log de commit de maneira resumida
* $git log -n 5                                           
	> filtra os ultimos 5 logs de commits
* $git log --since=aaaa-mm-dd                             
	> filtra o log a partir da data especificada
* $git log --until=aaaa-mm=dd                             
	> filtra o log ate a data especificada
* $git log --author=author_name                           
	> filtra o log pelo nome do autor
* $git log --grep="commit_name"                           
	> filtra o log pelo nome do commit
* $git rm --cached <file>                                 
	> remove um arquivo commitado do stage area
* $git diff                                               
	> conpara as modificacao entre o stage area e repositorio
* $git rm <file>                                          
	> remove um arquivo do repositorio local
* $git mv <file> <new_name>                               
	> renomeia um arquivo
* $git mv <file> <folder/file>                            
	> move o arquivo

* $git restore <file>                                     
	> restaura as modificacoes 
* $git restore --staged <file>                            
	> restaura os arquivos na stage area

* $git clean -n                                           
	> mostra quais untracked files irao ser permanentemente apagado
* $git clean -f                                           
	> permanentemente apaga untracked files
* $git revert HEAD~5                                      
	> ira recuperar commits anteriores em forma de uma novo commit
* $git show <5e9c8f9d66>                                  
	> mostra todas as modificacoes de um commit
* $git rm -r --cached .                                   
	> limpa todos os arquivos cached para usar o gitignore
	
* $git reset --soft <commit tag from git log>
	> remove todos commits postiores ao especificado e deixa os arquinos na stage area 
* $git reset --mixed <commit tag from git log>
	> remove todos commits posteriores ao especificado e deixa os arquivos como untracked 
* $git reset --hard <commit tag from git log>
	> deleta todos os commits posteriores ao especificado e deleta os arquivos do local e do server
	
# DEBUG
* commit not allowed, file above size limit 
	> $git reset --hard <commit tag>
	
## Convenção de Commits 

| Tipo de Commit |Descrição                                                            | Exemplo
| ---------------|----------------------------------------------------------------------|-----------
| `feat`         | Adiciona uma nova funcionalidade ao projeto.                         | `feat: add USENAME.md profile`
| `fix`          | Corrige um bug ou problema no projeto.                               | `fix: fixed issue fix#IssueNumber`
| `docs`         | Altera a documentação do projeto.| `docs: update README.md`
| `style`        | Realiza mudanças na aparência, sem alterar a funcionalidade.         | `style: add EFFECTNAME to COMPONENT`
| `refactor`     | Realiza mudanças no código que não alteram a funcionalidade.         | `refactor: refactor at CLASSNAME`
| `test`         | Adiciona ou modifica testes no projeto.                              | `test: add unit test for UserService`