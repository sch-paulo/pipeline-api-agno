import requests
import os
from datetime import datetime
from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from tinydb import TinyDB
from dotenv import load_dotenv
import time

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_KEY')

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class BitcoinDados(Base):
    __tablename__ = 'bitcoin_dados'

    id = Column(Integer, primary_key=True)
    valor = Column(Float)
    criptomoeda = Column(String(10))
    moeda = Column(String(10))
    timestamp = Column(DateTime)

Base.metadata.create_all(engine)

def extract():
    url = 'https://api.coinbase.com/v2/prices/spot'
    response = requests.get(url)
    return response.json()

def transform(dados_json):
    valor = float(dados_json['data']['amount'])
    criptomoeda = dados_json['data']['base']
    moeda = dados_json['data']['currency']
    dados_tratados = BitcoinDados(
        valor = valor,
        criptomoeda = criptomoeda,
        moeda = moeda,
        timestamp = datetime.now().isoformat()
    )
    return dados_tratados

def load_sqlalchemy(dados_tratados):
    with Session() as session:
        session.add(dados_tratados)
        session.commit()
        print('Dados salvos no PostgreSQL')


if __name__ == '__main__':
    while True:
        dados_json = extract()
        dados_tratados = transform(dados_json)
        load_sqlalchemy(dados_tratados)
        time.sleep(5)