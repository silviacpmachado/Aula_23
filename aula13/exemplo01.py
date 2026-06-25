import pandas as pd
import polars as pl
from datetime import datetime # biblioteca q trabalha  c/ tempo.
# https://portaldatransparencia.gov.br/download-de-dados/novo-bolsa-familia

# Lendo Bolsa Família
try:
    ENDERECO_DADOS = r'../dados/'

    hora_inicial = datetime.now()
    print('Carregando...')

    # Pandas - 0:00:19.188735
    # df_janeiro = pd.read_csv(ENDERECO_DADOS + '202601_NovoBolsaFamilia.csv', sep=';', encoding='iso-8859-1')
    # Polars - 0:00:06.049624
    df_janeiro = pl.read_csv(ENDERECO_DADOS + '202601_NovoBolsaFamilia.csv', separator=';', encoding='iso-8859-1')




    print(df_janeiro.head())

    hora_final = datetime.now()

    print(f'Tempo de Execução: {hora_final - hora_inicial}')
   
except Exception as e:
    print(f'Erro ao processar as informações: {e}')