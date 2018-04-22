# Preparando o Servidor

## Passo a Passo

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

Crie um novo Security Group chamado docker-lab para que assim possamos liberar a porta e SSH apenas para o seu IP de acesso, para isso selecione em "Source" a opção "MyIP" e clique em "Review and Launch"

<img src="../images/securitygroup.png" alt="Security Group"/>

Valide se todas as configurações estão corretas e clique em "Launch"

<img src="../images/review.png" alt="Tags"/>

Para acessar o servidor via SSH é preciso criar uma chave de SSH (caso você não tenha uma criada ainda), para criar selecione "Create a new key pair" e de um nome a essa chave exemplo "docker-lab" e clique em "Download Key Pair". Clique em "Launch Instance"

    Obs: Guarde bem essa chave, pois caso perca não será possível recupera-la e você não terá acesso ao servidor.

<img src="../images/ssh-key.png" alt="Tags"/>

Clique em "View Instance"

<img src="../images/launch-status.png" alt="Tags"/>

Agora que a máquina está ligada, só copiar o IP Público para acessa-la via SSH.

<img src="../images/instance-ip.png" alt="Tags"/>