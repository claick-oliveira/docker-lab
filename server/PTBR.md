# Preparando o Servidor

## Overview

Este guia contém labaratórios e exercícios para mostrar um pouco sobre o Docker e outras ferramentas que fazem parte desse universo como: Como realizar a instalação, comandos, docker-compose, Swarm, ECS e Kubernetes.

#### Passo a Passo

Acesse sua conta AWS e após na barra de pesquisa digite EC2 e clique na primeira opção:

<img src="../images/ec2.png" alt="EC2"/>

Clique em "Launch Instance"

<img src="../images/launch.png" alt="Launch Instance"/>

Selecione a imagem "Amazon Linux 2 LTS Candidate 2 AMI"

<img src="../images/amazonlinux.png" alt="Amazon Linux"/>

Escolha o tipo "t2.micro" e clique em "Next: Configure Instance Details"

<img src="../images/instancetype.png" alt="Instance Type"/>

Habilite o "Auto-assign Public IP" e clique em "Next: Add Storage"

<img src="../images/publicip.png" alt="Public IP"/>

Altere o tamanho do disco de 8 GiB para 15 GiB e clique em "Next: Add Tags"

<img src="../images/storage.png" alt="Storage"/>

Clique em Add Tag e adicione uma Tag chamada "Name" e com o "Valor" docker-lab e clique em "Next: Configure Security Groups" 

<img src="../images/tags.png" alt="Tags"/>