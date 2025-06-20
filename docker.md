# Docker 

## Docker Composer
> permite a execucao automatizada de um sistema.
- [ALERT] DO NOT USE TAB AS IDENTATIONS, IT WILL CAUSE ERROR [ALERT]

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
			- /DEV/Docker/DB:/data/db
```

- Inicia todos os servicos definidos no compose.yaml:
```docker 
docker compose up -d
```

- Interrompe  remove servicoes ativos:
```docker
docker compose down
```

- faz algo:
```docker 
docker compose logs
```

- Lista todos os processos dockers:
```docker
docker compose ps
```

- entra no container criado usando bash
```docker
docker exec -it db bash
```

- se o container tiver um shell proprio recomenda-se usa-lo
```docker 
docker exec -it db mongosh -u JustFox -p JustFox
```