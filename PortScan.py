import socket
# Esta biblioteca fara a ligação com o sistema operacional 
# onde lida com as conexões de Rede

portas = [21, 23, 80, 8080, 443]

# .connect é o método que fara a conexão
# .send é o método que deves ser conlocado, pois é necessário
# enviar uma mensagem para o servidor

for port in portas:
    clientes = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # tempo de execução da solicitação
    clientes.settimeout(0.1)

    # .connect_ex pode ser usado para enviar algo, automaticamente
    # para o servidor e assim não precisamos atribuir o cliente.recv a uma 
    # variável

    código = clientes.connect_ex(('127.0.0.1', port))

    # OR
    # clientes.send('Método para estudo!!!\n\n\n')
    # resposta = clientes.recv(2048)
    # print(port, código)

    if código == 0:
        print('Porta: ',port, 'OPEN')
    else:
        print('Porta: ',port, 'CLOSE')


    
