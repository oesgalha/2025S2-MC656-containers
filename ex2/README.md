# Exercício 2

Aplicação com dependências.

## Empacote uma aplicação Python

Esta pasta contem dois arquivos:
- requirements.txt : dependências do projeto
- not_a_quine.py : script Python

O script depende das bibliotecas listadas no arquivo de dependências.

Seu objetivo é criar uma imagem de container com a etiqueta `mc656ex2` que
executa o script.

Para isso fazer isso, consulte as instruções da imagem oficial:

https://hub.docker.com/_/python/#how-to-use-this-image

Quando a imagem estiver pronta, você pode rodar um container baseado nela com
o comando:
```
docker run --rm mc656ex2
```

Para ver o efeito de _syntax highlight_ rode com a opção `-t`:
```
docker run --rm -t mc656ex2
```

A opção `-t` aloca um pseudo-tty. Isso informa à biblioteca `rich` que o
processo está rodando em um terminal e portanto ela colore a saída do programa.

## Otimize o tamanho da imagem

Para ver o tamanho da imagem gerada, use o comando:
```
docker image ls
```

Para filtrar a saída e ver apenas essa imagem:
```
docker image ls | grep mc656ex2
```

A última coluna mostra o tamanho da imagem em disco.

Uma forma rápida de minimizar o tamanho usado por uma imagem é escolher uma
base mais leve, que tenha apenas o necessário para executar sua aplicação.

No Docker hub, olhe para as opções de tags da imagem Python:
https://hub.docker.com/_/python/tags

Procure tags para usar a versão 3.13, observe o tamanho delas e escolha uma
base que consuma pouco espaço em disco.

Muda a tag da base do seu Dockerfile e construa uma nova versão da sua imagem.

Confirme se a aplicação continua funcionando do mesmo jeito e consulte o novo
tamanho da imagem.
