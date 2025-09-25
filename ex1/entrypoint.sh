#/bin/bash

# Se o primeiro argumento do script for um arquivo
if [ -f "$1" ]; then
  # Executa o cowsay com o conteúdo do arquivo  
  cat "$1" | /usr/games/cowsay
else
  # Senão executa o cowsay com o argumento recebido
  /usr/games/cowsay $1
fi
