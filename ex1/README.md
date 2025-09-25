# Exercício 1

Dockerfile com CLI simples.

## Construa e teste o container

Para construir esse container execute:
```
docker build -t mc656ex1 .
```

O comando acima vai usar o arquivo Dockerfile no diretório atual para construir
uma imagem e colocar a etiqueta `mc656ex1`. O `.` no final da linha de comando
indica que o _contexto_ usado pelo Docker para gerar a imagem é o mesmo
diretório em que este comando foi executado.

Agora rode um container baseado na imagem gerada para testar o resultado:
```
docker run --rm mc656ex1
```

A opção `--rm` deleta o container no fim de sua execução. Por padrão, o Docker
vai manter em disco os containers executados, para que você possa
inspecioná-los depois. É comum executar containers com `--rm` para execuções
pontuais em que não é necessário revisitar o container após a execução.

Se tudo deu certo, você deve ver a seguinte saída:
```
 ________________________
< Estou em um container! >
 ------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

## Faça uma pequena alteração

Leia o código fonte comentado nos arquivos `Dockerfile` e `entrypoint.sh`.

Seu objetivo é mudar o comportamento padrão da imagem para o `cowsay` imprimir
o conteúdo de um arquivo ao invés de uma string hard-coded no Dockerfile.

Adicione um arquivo de texto (ex: "mensagem.txt") com algum texto e faça o 
comando `cowsay` imprimir o conteúdo desse texto. O conteúdo do texto pode ser
qualquer coisa, se não quiser escrever algo use algum gerador de lorem ipsum.

Ou seja, após gerar uma nova imagem com as suas alterações, executar um
`docker run --rm mc656ex1` deve imprimir o conteúdo de um arquivo que você
copiou para dentro da imagem do container.
