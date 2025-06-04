import os
from app import build_athena_uri


def test_build_athena_uri(monkeypatch):
    monkeypatch.setenv("AWS_USER", "dummy_user")
    monkeypatch.setenv("AWS_DB_PASSWORD", "dummy_pass")
    monkeypatch.setenv("AWS_REGION", "us-east-1")
    monkeypatch.setenv("S3_LOCATION", "s3://bucket")

    expected = (
        "awsathena+rest://dummy_user:dummy_pass@athena.us-east-1.amazonaws.com:443/"
        "caminho_para_o_banco_de_dados_especifico_no_Athena_que_você_"
        "deseja_acessar?s3_staging_dir=s3://bucket/athenaresults/&work_group=grupo_de_trabalho"
    )

    assert build_athena_uri() == expected
