# Docker 
> o docker possibilita lidar com os containers como se fossem maquinas virtuais modulares e extrememente leves.

- $ip a:
	- desc:
		- lista os IPs atuais da maquina.

- $docker inspect:
	- desc:
		- lista as informacoes de um container
	- img:
		- nome ou id do container.
```docker 
docker inspect [img]
```

- $docker pull:
	- desc:
		- para baixar a imagem docker do ubunto:
	- img:
		- nome da iso a ser baixada.
```docker 
docker pull [img]
```

- $docker run:
	- desc:
		- Para rodar uma imagem baixada do docker:
	- img: 
		- pode usar ID ou nome da imagem para criar um container.
	- param:
		- sleep [secs] : executa o container por n segundos e para o processo.
		- -d : permite a execucao do container em background
		- -it : permite interagir/utilizar o container(-i). e aloca um pseudo-terminal(-t).
		- --name [cont_nome] : permite nomer o container.
		- -p [host_porta:cont_porta] : set a porta a ser usada
		- --volume=/hostdir:/containerdir : usa o volume criado na hostdir.
		- -m [max_mem] : limita a quantidade maxima de memoria que pode ser usada pelo container. e.g 128M, 2G
		- --cpus [max_cpu%] : limita a quantidade maxima de cpu para ser usada pelo container
		- --network [network_name] : especifica a qual rede este container deve ser conectado
```docker 
docker run [param] [img]
```

- $docker ps:
	- desc:
		- para verificar containers em execucao:
	- param:
		- -a : mostra as execucoes recentes
```docker
docker ps [param]
```

- $docker stats
	- desc:
		- mostra os status do container, i.e cpu%, nome, memoria, mem%, etc.
```docker 
docker stats [container_nome]
```

- $docker stop:
	- desc:
		- Para parar um container em execucao:
	- img: 
		- pode ser usado o nome ou ID do container.
```
docker stop [img]
```

- docker start:
	- desc:
		- reinicia um container encerrado --via stop
	- img:
		- nome ou id do container
```docker 
docker start [img]
```

- $docker exec
	- desc:
		- Roda um comando em um container em execucao.
	- param:
		- -i : permite interacao com container,
		- -t : utiliza um pseudo-terminal.
	- img:
		- pode ser utilizado o nome ou id do container
	- cmd:
		- /bin/bash : executa o bash do container especificao.
		- mkdir /home : cria uma pasta no /home sem entrar no container.
```docker 
docker exec [param] [img] [cmd]
```

- $docker rm:
	- desc:
		- remove um container
	- param:
		- img: nome ou id do container a ser excluido
```docker 
docker rm [img]
```

- $docker rmi:
	- desc:
		- remove imagems
	- parametros:
		- img: 
```docker
docker rmi [img]
```

- $docker cp:
	- desc:
		- copia um arquivo de uma origem para um destino
	- origin:
		- caminho para arquivo. e.g ./arquivo.zip
	- dest:
		- caminho para arquivo. e.g ubunto:/destivo/arquivo.zip
```
docker cp [origin] [dest]
```

- $docker update
	- desc:
		- atualiza um container 
	- param:
		- -m [max_mem] : memoria maxima permitida pelo container, e.g 128M, 2G
		- --cpus [max_cpu%] : porcentagem maxima de cpu permitida. e.g 1, 0.2
```
docker update [container_nome] [param]
```

- $docker info
	- desc:
		- mostra informacoes sobre o servidor e informacoes dos containes atuais
```docker 
docker info
```

- $docker logs
	- desc: 
		- mostra os logs de execucao de um container
```docker 
docker logs [container_name]
```

- $docker top
	- desc:
		- mostra os processos em execucao de um container
```docker 
docker top [container_name]
```

- $docker network
	- desc:
		- gerenciameto de redes
	- param:
		- ls : lista networks
		- inspect [network_name] : mostra dados de um network
		- create [network_name] : cria uma rede com o nome especificado
```docker 
docker network [param]
```

## Volumes
> volumes criados pela instrucao 'volume', sao criados em /var/lib/docker mas nao possuem nome

- Bind
	- desc:
		- vincula um determinado diretorio ou arquivo do host dentro do container.
		- esses volumes sao armazenados dentro de /var/lib/docker
```docker
docker run --volume=/hostdir:/containerdir mysql
```
- Named
	- desc:
		- volumes criados manualmente com o comando volume create, gerenciado pelo docker engine
```docker
docker volume create mysql_data
docker run -v mysql_data:/containerdir mysql
```

- Mount 
	- desc:
		- utiliza/cria um volume do tipo bind/named/dockerfile 
	- vol_nome:
		- imagem para criar o container, se o mesmo nao existir
	- param:
		- --mount type=bind,src=/hostdir,dst=/containerdir,ro: faz a montagem do volume especificando o tipo, a fonte e a pasta destino, ro = read only
		- --mount type=volume,src=volumeName,dst=/containerdir : faz a montagem do volue especificando o volume criado com $docker volume create, na pasta destino
```docker 
docker run -dti [param] [vol_nome]
```

- $docker volume 
	- desc:
		- cria e gerencia um volume usando bind, volume, named 
	- param:
		- create [vol_nome]: cria um volume
		- rm [vol_nome]: remove o volume especificado
		- ls [path]: lista os volumes
		- prune : deleta todos os volumes que nao estao em uso
```
docker volume [param]
```

## Dockerfile
- desc:
	- usado para scriptar instalacoes de fora de um container
- Dockerfile Commands:
	- FROM: de onde esta vindo, imagem docker sendo executada 
	- RUN: executa a linha a seguir
	- COPY: copia um arquivo do host para o container 
	- CMD: executa um arquivo especificado
	- ENV: variavel de ambiente
	- ADD: copia um arquivo compactado(apenas .tar) para o container e o descompacta.
	- WORKDIR: cd para o diretorio especificado dentro do container
- img: imagem docker usada,
- cmd: commandos que podem ser executadas dentro do container, e.g em um container ubunto: apt-get install -y apache2
```arquivo: dockerfile
FROM [img]
WORKDIR [dst_path]
RUN [cmd]
COPY [file_path_origin] [file_path_dst]
CMD [file_path]
```

```arquivo dockerfile para apache 
FROM debian
RUN apt-get updaate && apt-get install -y apache2 && apt-get clean

ENV APACHE_LOCK_DIR=
ENV_APACHE_PID_FILE=
ENV APACHE_RUN_USER=
ENV APACHE_RUN_GROUP=
ENV APACHE_LOG_DIR=

ADD [file] [dst_dir]

LABEL description = "apache webserver 1.0"

VOLUME [volume_hostdir]

EXPOSE [port]   #espoe a porta. e.g 80

ENTRYPOINT ["/usr/sbin/apachectl"]

CMD ["-D", "FOREGROUND"]    #especifica que NAO deve ser executado em background
```

## Docker Composer
> permite a execucao automatizada de um container.
- [ALERT] DO NOT USE TAB AS IDENTATIONS, IT WILL CAUSE ERROR [ALERT]

- ports:
	- mysql: 3306:3306
	- mongoDB: 27017:27017
	
- Criando um 'compose.yaml' para o mongoDB:
```
services:
	db:
		image: mongo 
		container_name: db 
		restart: always
		environment:
			- MONGO_INITDB_ROOT_USERNAME=JustFox
			- MONGO_INITDB_ROOT_PASSWORD=JustFox
		ports:
			- "27017:27017"
		volumes:
			- /docker/data/mongoDB:var/lib/mongoDB
		networks: minha-rede
	networks:
		minha-rede:
			driver: bridge
```

- $docker compose up:
	- desc: 
		- Inicia todos os servicos definidos no compose.yaml
	- param:
		- -d: roda o container em background
```docker 
docker compose up [param]
```

- $docker compose down:
	desc:
		- Interrompe  remove servicoes ativos
```docker
docker compose down
```

- $docker compose logs:
	- desc:
		- TODO
```docker 
docker compose logs
```

- docker compose ps:
	- desc:
		- Lista todos os processos do docker compose:
```docker
docker compose ps
```
