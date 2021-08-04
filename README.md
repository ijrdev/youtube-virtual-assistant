# Youtube Virtual Assistant

## Introdução

Já pensou em programar e poder mudar, pausar e executar a música tocada no youtube a vontade? E ainda mais, por voz?
O Youtube Virtual Assistant é uma aplicação simples, com instruções básicas para fornecer essa comodidade.

## Considerações

Aplicação criada com o intuito de conhecer algumas bibliotecas e colocar em prática o aprendizado referente a linguagem Python.
Fica a gosto qualquer adaptação/alteração para se adequar da forma que precisa ou acha mais conveniente para utilização.

## Pré-Requisitos

 [![](https://img.shields.io/badge/python-v3.8.10-blue)](https://www.python.org/downloads/release/python-3810/) [![](https://img.shields.io/badge/pip-v20.0.2-blue)](https://pypi.org/project/pip/20.0.2/#history) [![](https://img.shields.io/badge/pipenv-v2021.5.29-blue)](https://pypi.org/project/pipenv/2021.5.29/)

- Ter um microfone;
- Instalar o Port Áudio; 
	- Linux/Ubuntu (`sudo apt-get install portaudio19-dev`);
	- Para as demais distribuições do Linux ou Windows será necessário verificar como realizar a instalação apropriada;

## Instalação

Após atender todos os pré-requisitos, deve-se acessar a pasta raiz e rodar o comando: `pipenv install`. Irá ser criado um ambiente virtual onde será instalado todas as dependências da aplicação. Feito isso, está tudo pronto para ser executado.

**OBS:** Não esquecer de apontar a execução da aplicação para o Python do ambiente virtual e não da máquina local.

## Comandos

Após inicializar a aplicação, alguns comandos devem ser seguidos para realizar as ações disponíveis.

**OBS:** Ruídos e barulhos podem prejudicar o entendimento do programa no decorrer das chamadas dos comandos. É recomendado que ao realizar algum comando, seja claro e direto, além de falar perto do microfone.

### START

Para começar a ouvir algo ou realizar a troca da música, basta iniciar o áudio com a frase pré-definida, seguindo com o que deseja escutar. Quanto mais detalhista for, melhor será a escolha da música, pois sempre será pego a primeira opção.

> **Comece a tocar** Alcel Valença Anunciação.

### PAUSE, PLAY e STOP

Os seguintes comandos são executados de forma direta sem precisar realizar complemento, bastando apenas chamá-los.

> **PAUSE -** Pausar a música.
> **PLAY -** Tocar a música.
> **STOP -** Parar a música (Irá encerrá a exeção da aplicação).