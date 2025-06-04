import os


def build_athena_uri() -> str:
    """Return the Athena connection URI built from environment variables."""
    region = os.environ.get("AWS_REGION")
    s3_location = os.environ.get("S3_LOCATION")
    user = os.environ.get("AWS_USER")
    password = os.environ.get("AWS_DB_PASSWORD")
    return (
        f"awsathena+rest://{user}:{password}@athena.{region}.amazonaws.com:443/"
        "caminho_para_o_banco_de_dados_especifico_no_Athena_que_você_"
        "deseja_acessar"
        f"?s3_staging_dir={s3_location}/athenaresults/&work_group=grupo_de_trabalho"
    )


def main() -> None:
    from dotenv import load_dotenv
    from sqlalchemy import create_engine
    from langchain.utilities import SQLDatabase
    from langchain.agents import create_sql_agent
    from langchain.agents.agent_toolkits import SQLDatabaseToolkit
    from langchain.agents.agent_types import AgentType
    from langchain.chat_models import AzureChatOpenAI

    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()

    # Verifica se as variáveis de ambiente essenciais estão definidas
    required_vars = [
        "AZURE_OPENAI_API_KEY",
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_DEPLOYMENT_NAME",
        "AWS_REGION",
        "S3_LOCATION",
        "AWS_USER",
        "AWS_DB_PASSWORD",
    ]
    missing = [var for var in required_vars if not os.getenv(var)]
    if missing:
        raise EnvironmentError(
            "Variáveis de ambiente ausentes: " + ", ".join(missing)
        )

    # Configuração do Azure OpenAI
    os.environ["AZURE_OPENAI_API_KEY"] = os.getenv("AZURE_OPENAI_API_KEY")
    os.environ["AZURE_OPENAI_ENDPOINT"] = os.getenv("AZURE_OPENAI_ENDPOINT")

    # Cria URI de conexão
    athena_db_uri = build_athena_uri()

    # Conexão com o Athena
    athena_engine = create_engine(athena_db_uri, echo=True)
    athena_db_connection = SQLDatabase(athena_engine)

    # Inicialização do modelo de linguagem Azure OpenAI
    llm = AzureChatOpenAI(
        azure_deployment=os.getenv("AZURE_DEPLOYMENT_NAME"),
        openai_api_version="2023-05-15",
    )

    # Inicialização do toolkit
    toolkit = SQLDatabaseToolkit(db=athena_db_connection, llm=llm)

    # Criação do agente SQL
    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )

    # Processar consulta em linguagem natural e gerar SQL
    natural_language_query = input("Digite sua consulta em linguagem natural: ")
    sql_query = agent_executor.run(natural_language_query)
    print(f"Sua consulta SQL é: {sql_query}")


if __name__ == "__main__":
    main()
