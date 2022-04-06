# Esteganografia em áudio

Esteganografia é a técnica utilizada para esconder mensagens dentro de arquivos, foi desenvolvida para a troca de mensagens de forma segura entre as partes.

É possível combinar esteganografia com criptografia, criando assim uma segunda barreira de segurança.

Existem vários tipos de esteganografia, imagem, texto, video, e neste caso, esteganografia em áudio. Dentro da esteganografia em áudio, existem várias técnicas.

Este código implementa a técnica LSB (least significant bit).

## Execução

Para executar este programa, existem duas possibilidade, o modo interativo ou por linha de comanda.

## Áudio de exemplo

Neste repositório se encontra um arquivo chamado `audio.wav` que contém um trecho da música `Quarto 12` da `Banda Passarela`. Todo os direitos são reservados a banda.

### Menu interativo

Para executar em modo interativo, basta executar o arquivo sem passar nenhum argumento:
```bash
python3 steganography.py
```

O programa exibirá 3 opções:

#### 1) Codificar

Nesta opção, o programa requisita o nome do arquivo `wav` para ser utilizado na codificação e a mensagem a ser escondida no arquivo. O resultado vai ser um arquivo `wav` do mesmo nome, porém, com `output-` no prefixo.

#### 2) Decodificar

Nesta opção, o programa requisita o nome do arquivo `wav` para extrair a mensagem codificada. Caso não encontre a string de separação (injetada pelo próprio algoritmo), o retorna uma mensagem de falha, caso contrário, exibe a mensagem encontrada.

#### 0) Sair

Para o looping e encerra o programa.

### Linha de comanda

Para executar como linha de comando, basta executar o arquivo e informar os argumentos.

#### Codificar

Para executar a codificação, é necessário passar 3 argumentos, a ação, o nome do arquivo `wav` e a mensagem. O resultado vai ser um arquivo `wav` do mesmo nome, porém, com `output-` no prefixo.

```bash
python3 steganography.py encode audio.wav "Pela command line"
```
Também é possível informar um nome para o arquivo de saída, neste caso, deve ser informado o nome no argumento posterior ao do nome de arquivo de entrada. O resultado vai ser um arquivo `wav` com o nome informado.

```bash
python3 steganography.py encode audio.wav saida.wav "Pela command line"
```

#### Decodificar

Para executar a decodificação, é necessário passar 2 argumentos, a ação e o nome do arquivo `wav`. O resultado vai ser a mensagem encontrada.

```bash
python3 steganography.py decode output-audio.wav
```