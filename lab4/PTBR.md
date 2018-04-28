# Docker: ECR

## O que é?

O Amazon Elastic Container Registry (ECR) é um serviço para armazenar as imagens dos seus containers do Docker totalmente gerenciado, assim como o [Docker Hub](https://hub.docker.com/). Caso queira saber mais [clique aqui](https://aws.amazon.com/pt/ecr/).

## Criando um Repositório

Bom para armazenarmos nossas imagens no ECR, precismos criar um repositório, execute o comando:

```bash
aws ecr create-repository --repository-name python-lab
```

Esse comando irá criar um repositório e retornará um json com algumas informações:

```json
{
    "repository": {
        "registryId": "012345678", 
        "repositoryName": "python-lab", 
        "repositoryArn": "arn:aws:ecr:<Região>:<ID da Conta>:repository/python-app", 
        "createdAt": 1524836721.0, 
        "repositoryUri": "<ID da Conta>.dkr.ecr.<Região>.amazonaws.com/python-app"
    }
}
```

Agora para conectarmos nosso Docker com ECR precismos que a AWS gere uma conta temporária pra nós, para isso digite:

```bash
aws ecr get-login --no-include-email --region <Região>
```

Ao executar esse comando a aws-cli irá criar um acesso temporário e a saída é um comando para conectarmos o Docker ao ECR:

```bash
docker login -u AWS -p eyJwYXlsb2FkIjoiRjJ6V2ptbkkzVVNVYlloUTJYeHNl....= https://<ID da Conta>.dkr.ecr.<Região>.amazonaws.com
```

Copie esse comando e execute, deverá aparecer algo assim:

```bash
WARNING! Using --password via the CLI is insecure. Use --password-stdin.
Login Succeeded
```

Para realizar login no Docker Hub, execute o comando:

```bash
docker login
```

E digitar suas credenciais, quer saber mais sobre o docker login [clique aqui](https://docs.docker.com/engine/reference/commandline/login/).

## Comandos

Para executar os passos a baixo é necessário ter executado alguns passos do lab1, caso você não fez ainda [clique aqui](../lab1/PTBR.md#build).

### Tag

Com sua imagem pronta, precisamos criar uma nova `TAG` para ela, as TAG são como wões atribuidas as imagens e também o nome do repositório para onde iremos enviar. Para subirmos uma imagem para o Docker Hub, por exemplo, precismos criar uma imagem assim:

```
<usuario do docker hub>/<imagem>:<tag>
```

Então ficaria assim:

```
joao/python-app:latest
```

O Docker por padrão entende que ele deve enviar essa imagem para o Docker Hub do usuário João, para informarmos o Docker que ele precisa enviar para outro Repositório precisamos criar assim:

```bash
<ID da Conta>.dkr.ecr.<Região>.amazonaws.com/<imagem>:<tag>
```

Agora que sabemos como devemos criar a nossa imagem, copie o `repositoryUri` de quando criamos nosso repositório e execute:

```bash
docker tag python-lab:latest <ID da Conta>.dkr.ecr.<Região>.amazonaws.com/python-lab:latest
```

Ou você pode criar a imagem com a TAG e Repositório desejados no momento de realizar o build:

```bash
docker image build -t <ID da Conta>.dkr.ecr.<Região>.amazonaws.com/python-lab .
```

Caso queira ver as imagens com as TAG e Respositórios diferentes, digite:

```bash
docker image ls
```

Para saber mais sobre o comando tag, [clique aqui](https://docs.docker.com/engine/reference/commandline/tag/).

### Push

Para enviar a nossa imagem para o ECR depois de colocarmos as configurações desejadas, execute:

```bash
docker push <ID da Conta>.dkr.ecr.<Região>.amazonaws.com/python-lab:latest
```

O resultado será algo como esse:

```bash
The push refers to repository [<ID da Conta>.dkr.ecr.<Região>.amazonaws.com/python-lab]
77e23640b533: Layer already exists 
757d7bb101da: Layer already exists 
3358360aedad: Pushed 
latest: digest: sha256:d903fe3076f89ad76afe1cbd0e476d9692d79b3835895b5b3541654c85422bf1 size: 948
```

Caso queira ver as TAG que estão armazenadas no repositório digite:

```bash
aws ecr list-images --repository-name python-lab
```

[Clique aqui](https://docs.docker.com/engine/reference/commandline/push/) para saber mais sobre.

### Pull

Para baixarmos uma imagem existe o comando pull:

```bash
docker pull <ID da Conta>.dkr.ecr.<Região>.amazonaws.com/python-lab:latest
```

Para ver mais coisas sobre o comando, [clique aqui](https://docs.docker.com/engine/reference/commandline/pull/).