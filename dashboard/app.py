import streamlit as st
import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_KEY')

def read_data_postgres():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        query = 'SELECT * FROM bitcoin_dados ORDER BY timestamp DESC'
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f'Erro ao conectar no PostgreSQL: {e}')
        return pd.DataFrame()
    
def main():
    st.set_page_config(page_title='Dashboard de Preços do Bitcoin', layout='wide')
    st.title('Dashboard de Preços do Bitcoin')
    st.write('Este dashboard exibe os dados do preço do Bitcoin coletados periodicamente em um banco PostgreSQL')

    df = read_data_postgres()

    if not df.empty:
        st.subheader('Dados Recentes')
        st.dataframe(df)

        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values(by='timestamp')

        st.subheader('Evolução do Preço do Bitcoin')
        st.line_chart(data=df, x='timestamp', y='valor', use_container_width=True)

        st.subheader('Estatísticas Gerais')
        col1, col2, col3 = st.columns(3)
        col1.metric('Preço Atual', f'${df["valor"].iloc[-1]:,.2f}')
        col1.metric('Preço Máximo', f'${df["valor"].max():,.2f}')
        col1.metric('Preço Mínimo', f'${df["valor"].min():,.2f}')
    else:
        st.warning('Nenhum dado encontrado no banco de dados')

if __name__ == '__main__':
    main()