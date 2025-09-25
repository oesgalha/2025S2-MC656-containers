# Exercício 4

Múltiplos containers

## Suba o projeto

Para começar, suba a aplicação de exemplo. Ela é uma API Web feita em Python
com um endpoint que envia e-mails. Para fins de teste, usamos o serviço
`maildev`, que implementa um servidor SMTP e uma interface web para visualizar
os e-mails enviados.

O arquivo `compose.yml` usa o Docker Compose para subir tanto a API quanto o
serviço do `maildev` ao mesmo tempo, conectá-los numa mesma rede e expor as
portas relevantes para a sua máquina: a porta 8000 tem a API e a porta 1080 tem
a interface Web do `maildev`.

Para subir os containers, use:
```
docker compose up
```

Abra duas abas no browser:
- http://localhost:8000/docs
- http://localhost:1080

Envie um e-mail através da API, confirme que ele aparece na interface web do
simulador de servidor SMTP.

## Suba o projeto com sincronização de arquivos

O arquivo `compose.yml` está configurado para atualizar o código fonte do
container conforme você altera o código fonte. Teste essa funcionalidade
subindo os containers da seguinte forma:
```
docker compose watch
```

Faça alguma alteração no código fonte e veja ela imediatamente disponível no
browser. Mude a saída do endpoint "hello world" na raíz, por exemplo.

## Deixe o projeto pronto para outros ambientes

Observe que no Dockerfile o `CMD` usa o parâmetro `--reload`, que é recomendado
apenas para ambientes de desenvolvimento.

Além disso, no arquivo `main.py` o endereço e a porta do servidor SMTP estão
_hardcoded_ no código. Essa API funciona apenas nessa configuração.

Há um conjunto de práticas chamado metodologia dos 12 fatores com algumas
recomendações de como organizar aplicações web:
https://12factor.net/pt_br/

Um dos fatores recomenda o uso de _variáveis de ambiente_ para alterar
configurações da aplicação sem alterar o código fonte:
https://12factor.net/pt_br/config

Seu objetivo é fazer com que o `Dockerfile` gere uma imagem que possa ser usada
tanto em produção quanto em desenvolvimento. Ou seja, a imagem isolada não deve
usar o parâmetro `--reload` por padrão, apenas quando o serviço subir através
do docker compose. Além disso, o endpoint que envia e-mails deve se conectar
no servidor SMTP usando um endereço e porta que vieram de variáveis de ambiente
(ex: SMTP_HOST e SMTP_PORT).

Consulte a referência do arquivo YAML de configuração do docker compose:
- https://docs.docker.com/reference/compose-file/services/#command
- https://docs.docker.com/reference/compose-file/services/#environment
