from pytube import YouTube
import moviepy.editor as mp
import re
import os

link = input('Digite o link do video que será baixado: ')

local = input('Digite o diretório que deseja salvar: ')

yt = YouTube(link)

print('Baixando...')
ys = yt.streams.filter(only_audio=True).first().download(local)
print("Download completo!")