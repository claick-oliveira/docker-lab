# Docker: Guia

## Overview

Este guia contém labaratórios e exercícios para mostrar um pouco sobre o Docker e outras ferramentas que fazem parte desse universo como: Como realizar a instalação, comandos, docker-compose, Swarm, ECS e Kubernetes.

### Requisítos:

Para realizar esses laboratórios, você irá precisar de:

* [Conta na AWS](https://aws.amazon.com/pt/premiumsupport/knowledge-center/create-and-activate-aws-account/);
* [Servidor Linux](./server/PTBR.md) ou [Cloud9](./cloud9/PTBR.md);

#### Preparando o ambiente

Esses laboratórios precisam de diversas ferramentas:

* **Docker [(veja como instalar)](https://docs.docker.com/install/)**
* docker-compose
* kubectl
* kops
* aws-cli

Após a instalação do Docker execute esse comando:

```shell
curl https://raw.githubusercontent.com/claick-oliveira/docker-lab/master/scripts/bootstrap.sh | bash
```

### Laboratórios

* **[Lab 1: Docker Overview](./lab1/PTBR.md)**

* **[Lab 2: Docker Compose](./lab2/PTBR.md)**

* **[Lab 3: Swarm Cluster](./lab3/PTBR.md)**

* **[Lab 4: ECS](./lab4/PTBR.md)**

* **[Lab 5: Kubernetes](./lab5/PTBR.md)**
