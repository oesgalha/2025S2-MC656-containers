# Exercício 3

Distribuição.

## Publique uma imagem no GitHub

O GitHub tem um registry de imagens (ghcr.io) que permite subir imagens
públicas gratuitamente.

Publique a imagem que você gerou no primeiro exercício.

## Autentique no registry do GitHub

Crie um token (classic) para autenticar no GitHub:

https://github.com/settings/tokens/new

Dê um nome qualquer, escolha uma data de expiração curta e selecione os
seguintes escopos:
- `read:packages` para poder baixar imagens e metadados
- `write:packages` para poder subir imagens e metadados
- `delete:packages` para poder deletar imagens

Agora coloque o valor do token numa variável de ambiente:
```
export CR_PAT=YOUR_TOKEN
```

E faça o login com `docker` no registry da GitHub:
```
echo $CR_PAT | docker login ghcr.io -u <USERNAME> --password-stdin
```

Substitua <USERNAME> pelo seu usuário.

Referência:

https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#authenticating-with-a-personal-access-token-classic

## Crie uma nova etiqueta e empurre a imagem para o registry

Volte no diretório do exercício 1 e faça novamente uma build usando outro
valor para a etiqueta, com referência ao registry do GitHub:

```
docker build -t ghcr.io/<USERNAME>/mc656ex1 .
```

Se quiser testar a imagem antes de subir:
```
docker run --rm ghcr.io/<USERNAME>/mc656ex1
```

Agora empurre a imagem para o registry:
```
docker push ghcr.io/<USERNAME>/mc656ex1
```

Se você se autenticou corretamente, a imagem agora está publicada no registry
de imagens da GitHub.

Você pode vê-la em:
`https://github.com/users/<USERNAME>/packages/container/package/mc656ex1`

## Confirme a distribuição

Agora vá nas configurações do pacote e mude a visiblidade do pacote de privado
para público:
`https://github.com/users/<USERNAME>/packages/container/mc656ex1/settings`

Agora tente usar o seu container em outro computador com:
```
docker run --rm ghcr.io/<USERNAME>/mc656ex1
```

Use seu laptop (se tiver docker) ou peça para a pessoa ao lado testar a sua imagem.
