# Baixando as Bibliotecas
from gtts import gTTS
from playsound import playsound

# Setando Linguagem e nome do arquivo MP3
audio = 'audio.mp3'
linguagem = 'pt-br'

# Digitando As informações necessárias 
assistente_nome = str(input('Qual nome você deseja dar para sua assistente ler?'))
msg = str(input(f'Digite uma frase para {assistente_nome} ler para você: '))

sp = gTTS(text=msg, lang=linguagem)

# Salvando e tocando o arquivo MP#
sp.save(audio)
playsound(audio)
