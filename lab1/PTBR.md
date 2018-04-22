# Docker: Overview

## O que é Docker?

Docker é uma plataforma que utiliza containers para "empacotar" softwares em pequenas unidades padronizadas desde o desenvolvimento, entrega e implantação.

## O que é um Container? E como funciona?

Um container é um ambiente isolado dos demais, para conseguir esse isolamento de recursos o kernel utiliza algumas coisas, as principais são:

* filesystems - namespaces (MNT)
* processos - namespaces (PID)
* network - namespcaes (NET)
* memória - cgroups
* cpu - cgroups
* IO - cgroups

<img src="../images/container-docker.png" alt="Container"/>

## O que é uma imagem?

Images Docker são compostas por sistemas de arquivos de camadas que ficam uma sobre as outras. Ela é a nossa base para construção de uma aplicação, ela pode ser desde a base do CentOS como também um CentOS com Apache, PHP e MySQL.

<img src="../images/image-docker.png" alt="Imagem"/>

## Componentes

Para utlizarmos o Docker precisamos entender qual o papel de alguns componentes. Os componentes são:

* docker-cli: É o cliente do docker que interpreta os comandos digitados pelo usuário e chama a API do Host Docker.
* Host Docker: É o servidor/máquina que rodará o Docker daemon e hospedará os containers.
* Docker Daemon: Responsável por receber os comandos enviados pela docker-cli e passar as instruções para o Kernel.
* Registry: Local para armazenar e versionar as imagens das aplicações.

<img src="../images/architecture-docker.svg" alt="Componentes"/>

## Máquinas Virtuais vs Containers

As máquinas virtuais são uma abstração de um hardware físico tornando um servidor em muitos outros. O Hypervisor permite rodar diversos servidores virtuais em uma unica máquina. Cada máquina virtual será um servidor completo tendo seu próprio sistemas de aruiqvos e hardwares virtuais (CPU, memória, redes e etc.).

<img src="../images/vm.png" alt="VM"/>

Os containers são uma abstração da camada de aplicação tendo os códigos e dependências juntos. Vários containers podem rodar na mesma máquina e compartilhar o Sistema Operacional e kernel com os demais containers, cada processo irá rodar isoladamente.

<img src="../images/container.png" alt="Containers"/>

## Benefícios

* Portabilidade: Você pode rodar o seu container em qualquer lugar que possua Docker instalado que terá o mesmo comportamento, do ambiente de Dev até Produção.

* Rollback: Após um problema ser identificado durante o deploy, ao rodar versões anteriores de imagens a recuperação será muito mais rápida e eficiente.

* Container Registry: Um local para centralizar todas as imagens, podendo ser público ou privado e mantendo histórico de versões das imagens.

* Runtime: Pode executar um ou milhares de contêineres em poucos segundos.

* Isolamento: Todos os containers em execução seram isolados dos demais processos e sistemas de arquivo do host e entre eles.