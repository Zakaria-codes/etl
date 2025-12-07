import pandas as pd
import numpy as np

class Transformer:
    def __init__(self, raw_data):
        self.data = raw_data
        self.kpis = {}

    def clean_dataframe(self, df):
        
        df = df.drop(columns=[c for c in df.columns if 'Unnamed' in c], errors='ignore')
        cleaned = df.dropna(axis=1, how="all")
        year_cols = sorted(cleaned.select_dtypes(include=['number']).columns)
        cleaned[year_cols] = cleaned[year_cols].interpolate(axis=1, limit_direction="both")
        return cleaned

    def process_cleaning(self):
        print("Starting data cleaning...")
        for key, df in self.data.items():
            self.data[key] = self.clean_dataframe(df)

    def calculate_ratio(self, num_key, denom_key, code, name, operation="divide"):
        if num_key not in self.data or denom_key not in self.data:
            print(f"Skipping {name}: Missing source data.")
            return

        df_num = self.data[num_key].set_index("Country Code")
        df_denom = self.data[denom_key].set_index("Country Code")
     
        cols = df_num.select_dtypes(include='number').columns.intersection(df_denom.select_dtypes(include='number').columns)

        if operation == "divide":
           
            res = df_num[cols] / df_denom[cols].replace(0, np.nan)
        elif operation == "multiply_percent":
            res = (df_num[cols] * df_denom[cols]) / 100
        
        
        res["Country Name"] = df_num["Country Name"]
        res["Country Code"] = res.index
        res["Indicator Name"] = name
        res["Indicator Code"] = code
        
        return res.reset_index(drop=True)

    def generate_kpis(self):
        print("Calculating KPIs...")
        self.kpis['gdp_capita'] = self.calculate_ratio(
            'gdp', 'population', "CALC.GDP.CAP", "GDP per Capita (USD)", "divide"
        )
        
        self.kpis['rural_pop'] = self.calculate_ratio(
            'population', 'rural', "CALC.POP.RURAL", "Rural Population (Total)", "multiply_percent"
        )
        
        self.kpis['elec_pop'] = self.calculate_ratio(
            'population', 'electricity', "CALC.POP.ELEC", "People with Electricity", "multiply_percent"
        )
        return self.kpis