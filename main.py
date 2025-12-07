from extraction import DataLoader
from transformation import Transformer
from loading import SQLLoader
from dbconfig import config

if __name__ == "__main__":
    loader = DataLoader("DATASETS")
    raw_data = loader.load_all()

    pipeline = Transformer(raw_data)
    pipeline.process_cleaning()
    kpis = pipeline.generate_kpis()

    sql_loader = SQLLoader(config)
    sql_loader.load_to_sql(pipeline.data, kpis)
