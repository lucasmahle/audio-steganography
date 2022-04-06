import sys
import wave

EOS_VALUE = '###ENDOFSTRING###'

def validate_file_extension(file_name):
  return 'wav' == file_name.split('.')[-1]

def encode(file_name, output_file_name, content, enable_message):
  if not validate_file_extension(file_name):
    print('Argumento inválido')
    print('O arquivo de entrada deve ser do tipo wav')
    return

  if not validate_file_extension(output_file_name):
    print('Argumento inválido')
    print('O arquivo de saída deve ser do tipo wav')
    return

  if enable_message:
    print('\nOperação iniciada')

  # Abre o arquivo de áudio a receber a codificação
  audio = wave.open(file_name, mode='rb')

  # Quantidade de frames do áudio
  frames_number = audio.getnframes()
  if enable_message:
    print('\nTotal de frames: ', frames_number)

  # Obtém lista de bytes dos frames do áudio
  frame_bytes = bytearray(list(audio.readframes(frames_number)))

  # Prepara conteúdo a ser ocultado
  if enable_message:
    print('\nConteúdo a ser ocultado: ', content)
  string = content + EOS_VALUE

  # Completa a strign com caractere # até preencher o comprimento do áudio
  bytes_frames_quantity = len(frame_bytes)
  bytes_string_quantity = len(string) * 8 * 8
  filled_bytes_quantity = bytes_frames_quantity - bytes_string_quantity
  string = string + int(filled_bytes_quantity / 8) * '#'
  
  # Para cada letra da string, obtém o valor unicode do caractere
  # Obtém a string equivalente ao valor binário do valor
  # Remove a notação de 'valor binário' (0b)
  # Preenche com 0 à esquerda até completar 8 dígitos
  # O resultado é uma lista única com todos os binários sequenciados
  bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))

  # Para cada valor (int) do frame original
  for i, bit in enumerate(bits):
    new_frame = frame_bytes[i]
    
    # Opera bit a bit com comparação AND com 254
    # Forçando o bit menos significativo ficar com 0
    new_frame = new_frame & 254
    # Opera bit a bit com comparação OR com bit da mensagem
    # Essa comparação escreve o valor do bit no frame
    new_frame = new_frame | bit

    # Reescreve no frame
    frame_bytes[i] = new_frame

  # Gera bytes dos novos frames
  frame_modified = bytes(frame_bytes)

  # Gera saída do áudio
  new_audio = wave.open(output_file_name, 'wb')
  new_audio.setparams(audio.getparams())
  new_audio.writeframes(frame_modified)

  new_audio.close()
  audio.close()

  if enable_message:
    print('\nOperação concluída com sucesso')

def decode(file_name, enable_message):
  if not validate_file_extension(file_name):
    print('Argumento inválido')
    print('O arquivo de entrada deve ser do tipo wav')
    return

  if enable_message:
    print('\nOperação iniciada')

  # Abre o arquivo a ser decodificado
  audio = wave.open(file_name, mode='rb')


  # Quantidade de frames do áudio
  frames_number = audio.getnframes()
  if enable_message:
    print('\nTotal de frames: ', frames_number)

  # Obtém lista de bytes dos frames do áudio
  frame_bytes = bytearray(list(audio.readframes(frames_number)))
  bytes_frames_quantity = len(frame_bytes)
  audio.close()

  # Para cada valor binário dos frames
  # Opera bit a bit com comparação AND com 1
  extracted = [frame_bytes[i] & 1 for i in range(bytes_frames_quantity)]

  character_list = []
  # Para cada 8 bits
  for i in range(0, len(extracted), 8):
    # Extrai 8 números vinários
    bin_value = extracted[i:i+8]
    # Converte para string
    bin_value_srt = ''.join(map(str, bin_value))
    
    # Obter o valor decimal do mesmo
    int_value = int(bin_value_srt,2)
    
    # Obter o caractere unicode
    character = chr(int_value)
    character_list.append(character)

  # Arquivo de áudio em string
  string = ''.join(character_list)

  # Verificar se string é válida
  if string.find(EOS_VALUE)  < 0:
    print('\nNão foi encontrado nenhuma mensagem no arquivo')
    return

  # Quebra a string a partir do valor pré definido
  decoded = string.split(EOS_VALUE)[0]
  if enable_message:
    print('Mensagem oculta: ' + decoded)
  else:
    print(decoded)
  
  if enable_message:
    print('\nOperação concluída com sucesso')

def menu():
  enable_message = True
  option = 1
  while option != 0:
    print('\nSelecione uma opção:')
    print('1) Codificar')
    print('2) Descodificar')
    print('0) Sair')

    option = int(input('\n-> '))

    if option == 1:
      file_name = input('Nome do arquivo wav: ')
      message = input('Mensagem: ')
      encode(file_name, 'output-' + file_name, message, enable_message)
    elif option == 2:
      file_name = input('Nome do arquivo wav: ')
      decode(file_name, enable_message)

def command_line(args, arg_count):
  enable_message = False
  option = args[1]
  file_name = args[2]

  if option == 'encode':
    output_file_name = ('output-' + file_name) if 4 == arg_count else args[3]
    message = args[3] if 4 == arg_count else args[4]
    encode(file_name, output_file_name, message, enable_message)
  elif option == 'decode':
    decode(file_name, enable_message)
  else:
    print('Método inválido, use encode ou decode')

if __name__ == '__main__':
  arg_count = len(sys.argv)
  
  if 1 == arg_count:
    menu()
  elif arg_count <= 5:
    command_line(sys.argv, arg_count)
  else:
    print(f'Comando inválido\n{sys.argv[0]} method file_name [output_file_name] message')