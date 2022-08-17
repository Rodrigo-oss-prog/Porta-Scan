# varredura de Porta

Este código é um scaner de porta feito em Python.

### 📋 Pré-requisitos

É necessário ter o python instalado na sua máquina, caso use a IDE VS Code, instale a extenção Python.

### 🔧 Instalação

Instalação em uma máquina Linux que usa o instalador de pacotes APT

```
sudo apt-get install python3
sudo python3 --version
```
Para instalar o gerenciador de pacotes pip, digite no terminal, mas é opcional!

```
sudo apt-get install python3-pip

```

## ⚙️ Sobre a varredura de portas

Este exemplo de varredura de porta em python nos mostra a versátilidade da linguagem.


### 🔩 Analisando o código

Importei a biblioteca socket necessária para analisar a conexão da máquina com a rede.

```
import socket

```
Usei o endereço de loop back para a varredura neste código.

```
'127.0.0.1'

```
E analisado determinadas portas:

```
portas = [21, 23, 80, 8080, 443]

```

## 📦 Desenvolvimento

Sobre determinada linha que verás no código:

```
clientes = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

```
A variável clientes atribuímos socket que por sua vez receberá os parâmetros, socket.AF_INET e socket.SOCK_STREM. Esse indica a família de protocolo(IPv4) e este indica o modelo TCP/IP.

## 🛠️ Construído com

* [VS Code](https://www.python.org/) - IDE usado
 

## Para melhor detalhamento sobre sockets


* [Sobre Sockets](https://www.python.org/) - HOWTO sobre a Programação de Soquetes


## 📌 Versão


Usado [Python 3.10.4](https://www.python.org/) para consulta a documentação Python.


## ✒️ Autores


* **Um desenvolvedor** - Rodrigo-oss-prog.
 😊
