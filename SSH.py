import paramiko

#Menu
print("="*40)
print ('''
[1] Fazer conexão com um servidor SSH
''')
print("="*40)
menu = int ( input ('Escolha as opções: '))
#aninhamento

if menu==1:
    print ("#"*40)
    hostname = input ( 'Digite a Hostname do servidor: ')

    port = int ( input ('Porta: '))

    username = str ( input ('Digite seu nome de usuario: '))

    password = input ('Digite a sua senha: ')

    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #Fazendo a conexão com o SSH

    client.connect(hostname, port=port, username=username, password=password)
    
    client.close()

