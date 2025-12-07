import mysql.connector as mysql
import pandas as pd
import numpy as np

class SQLLoader:
    def __init__(self, config):
        self.config = config

    def prepare_for_sql(self, data, kpis):
        all_dfs = list(data.values()) + list(kpis.values())

        melted_list = []
        for df in all_dfs:
            if df is not None and not df.empty:
                melted = df.melt(
                    id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'],
                    var_name='Year',
                    value_name='Value'
                )
                melted_list.append(melted)
        if not melted_list:
          print("No data to load.")
          return None
        full_df = pd.concat(melted_list, ignore_index=True)

        full_df["Year"] = pd.to_numeric(full_df["Year"], errors="coerce")
        full_df = full_df.dropna(subset=["Year"])
        full_df.replace([np.inf, -np.inf], np.nan, inplace=True)
        full_df = full_df.where(pd.notnull(full_df), None)
        full_df = full_df.astype(object)
        full_df = full_df.where(pd.notnull(full_df), None)
        return full_df

    def insert_dimensions(self, cur, full_df):
        dims = {
            "countries": full_df[["Country Code", "Country Name"]].drop_duplicates().values.tolist(),
            "indicators": full_df[["Indicator Code", "Indicator Name"]].drop_duplicates().values.tolist(),
            "years": full_df[["Year"]].drop_duplicates().values.tolist(),
        }

        cur.executemany(
            "INSERT IGNORE INTO countries (country_code, country_name) VALUES (%s, %s)",
            dims["countries"]
        )
        cur.executemany(
            "INSERT IGNORE INTO indicators (indicator_code, indicator_name) VALUES (%s, %s)",
            dims["indicators"]
        )
        cur.executemany(
            "INSERT IGNORE INTO years (year) VALUES (%s)",
            dims["years"]
        )

    def insert_facts(self, cur, full_df):
        facts = full_df[
            ["Country Code", "Year", "Indicator Code", "Value"]
        ].values.tolist()

        cur.executemany(
            "INSERT INTO fact_measures (country_code, year, indicator_code, value) VALUES (%s, %s, %s, %s)",
            facts
        )

    def load_to_sql(self, data, kpis):
        full_df = self.prepare_for_sql(data, kpis)

        try:
            con = mysql.connect(**self.config)
            cur = con.cursor()

            self.insert_dimensions(cur, full_df)
            self.insert_facts(cur, full_df)

            con.commit()
            print("Data Load Successful!")

        except mysql.Error as err:
            print("Database Error:", err)

        finally:
            if 'con' in locals() and con.is_connected():
                con.close()
                print("Connection closed.")
