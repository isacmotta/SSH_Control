import os
import paramiko
import socket
#Menu
print("="*40)
print ('''
[1] Conexãp Rapida.
[2] Verificar Dispositivos na rede local.

''')
print("="*40)
seleção = int ( input ('Escolha as opções: '))
#aninhamento

#agora irei gerar um codigo complexo e que use menos linhas que esse

if seleção==1:
    print ("#"*40)
    print ('Conexão rapida.')

    #para uma conexão em ssh e necessario informar a host e a senha por isso
    print('[!] Use o endereço de host como servidorSSH.com ou outro.')
    host = (input('Endereço da Host: '))#Sera criado uma variavel para o nome da host

    print('[!] Nesta versão a senha só pode conter numeros')
    password= (input('Senha: '))#Senha da host..

    print('o nome de usuarios deve conter somente letras')
    username = str (input('Digite o Nome de usuario: '))

    portquest = int(input('Qual a sua porta SSH: '))
    port = portquest

    #agora sera criado uma conexão com as informações inseridas

    #instacia do cliente SSH
    ssh = paramiko.SSHClient()

    #Aqui sera carregada a chave da conexão

    ssh.load_system_host_keys()

    #conectar no servidor
    ssh.connect(host,port,username,password)

    commands = 15

    while i == 5:
        shell = (input('$'))

    #já inicia dando o comando 'ls' para mostrar os repositorios.
    stdin,stdout sdterr = ssh.exec_command('shell')
