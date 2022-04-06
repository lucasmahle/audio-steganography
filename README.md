# Esteganografia em áudio

Esteganografia é a técnica utilizada para esconder mensagens dentro de arquivos, foi desenvolvida para a troca de mensagens de forma segura entre as partes.

É possível combinar esteganografia com criptografia, criando assim uma segunda barreira de segurança.

Existem vários tipos de esteganografia, imagem, texto, video, e neste caso, esteganografia em áudio. Dentro da esteganografia em áudio, existem várias técnicas.

Este código implementa a técnica LSB (least significant bit)


## Menu interativo


## Linha de comanda

```bash
python3 steganography.py encode audio.wav saida.wav "Pela command line"
```

```bash
python3 steganography.py encode audio.wav "Pela command line"
```

```bash
python3 steganography.py decode output-audio.wav
```