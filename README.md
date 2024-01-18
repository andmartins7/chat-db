# CHAT-DB - Converse com o seu Banco de Dados

![image](https://github.com/andmartins7/chat-db/assets/128826621/d979d3a7-b79b-477b-94b7-7c99694e3c2c)


# Descrição do Projeto
Este projeto é uma aplicação Python que demonstra a integração de várias tecnologias, incluindo AWS Athena, Azure OpenAI, e o uso de um agente SQL para processar consultas em linguagem natural e convertê-las em SQL. A aplicação utiliza variáveis de ambiente para gerenciar informações sensíveis e oferece uma interface para executar consultas em linguagem natural que são traduzidas em consultas SQL.

# Funcionalidades
- **Carregamento de Variáveis de Ambiente:** Utiliza a biblioteca dotenv para carregar variáveis de ambiente de um arquivo .env. Isso ajuda a manter as credenciais e chaves de API seguras e fora do código-fonte.

- **Configuração do Azure OpenAI:** Define variáveis de ambiente específicas para o Azure OpenAI, incluindo a chave da API e o endpoint, necessários para a autenticação e comunicação com os serviços Azure OpenAI.

- **Conexão com AWS Athena:** Cria uma conexão com um banco de dados AWS Athena utilizando informações de usuário, senha, região AWS e localização S3, tudo obtido de forma segura através de variáveis de ambiente.

- **Inicialização do Modelo de Linguagem Azure OpenAI:** Configura e inicializa o modelo de linguagem Azure OpenAI, que será utilizado para processar consultas em linguagem natural.

- **Toolkit de Banco de Dados SQL:** Cria um toolkit de banco de dados SQL que facilita a interação com o banco de dados Athena.

- **Criação de Agente SQL:** Inicializa um agente SQL que utiliza o modelo de linguagem Azure OpenAI e o toolkit de banco de dados para processar consultas em linguagem natural e convertê-las em SQL.

- **Interface de Consulta:** Permite ao usuário digitar consultas em linguagem natural, que são processadas pelo agente SQL e convertidas em consultas SQL. As consultas convertidas são então exibidas ao usuário.

# Como Usar
1- **Configuração do Ambiente:** Certifique-se de que todas as dependências estão instaladas e que o arquivo .env contém todas as credenciais e variáveis de configuração necessárias.

2- **Execução do Script:** Execute o script Python. Isso iniciará a aplicação.

3- **Digite Consultas em Linguagem Natural:** Após a inicialização, a aplicação pedirá que você digite uma consulta em linguagem natural. Por exemplo, você pode digitar "Mostre-me as vendas do último trimestre".

4- **Visualização da Consulta SQL:** Após digitar a consulta, o agente SQL processará seu pedido e exibirá a consulta SQL correspondente baseada na sua entrada em linguagem natural.

5- **Processamento Adicional (Opcional):** Você pode usar a consulta SQL gerada para realizar operações adicionais no banco de dados AWS Athena, conforme necessário.

# Pré-requisitos
- Python 3.x
- Bibliotecas Python: sqlalchemy, dotenv, entre outras necessárias para o funcionamento do projeto.
- Acesso ao AWS Athena com credenciais válidas.
- Acesso ao Azure OpenAI com chave de API válida.
- Um arquivo .env configurado com todas as variáveis de ambiente necessárias.
