# Usa como base a última versão estável e LTS do Ubuntu disponível
# no Docker hub
FROM ubuntu:noble-20250910

# Instala o pacote `cowsay`
RUN apt-get update && apt-get install -y cowsay

# Muda o diretório de "trabalho". Como essa pasta não existe ela será criada.
# Os comandos daqui para baixo são executados a partir desse diretório.
# Comandos para copiar arquivos, vão copiar arquivos nesse diretório.
WORKDIR /opt/app

# Copia o script "entrypoint.sh" do contexto do host para o WORKDIR da imagem
# de container.
COPY entrypoint.sh entrypoint.sh

# Define o entrypoint da imagem, ela sempre executará esse script.
ENTRYPOINT ["sh", "/opt/app/entrypoint.sh"]

# Define o parâmetro padrão do script definido no entrypoint.
CMD ["Estou em um container!"]
