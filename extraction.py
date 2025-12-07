import pandas as pd
import os

class DataLoader:
  
    def __init__(self, datasets_path="DATASETS"):
        self.base_path = datasets_path
        self.file_configs = {
            "electricity": ("electricity_access_percent.csv", "utf-8", 4),
            "gdp": ("gdp_data.csv", "utf-8", 4),
            "population": ("population_data.csv", "utf-8", 4),
            "rural": ("rural_population_percent.csv", "utf-8", 4),
            "mystery": ("mystery.csv", "utf-16", 0) 
        }
        self.data = {}

    def _load_single_file(self, name, config):
        filename, encoding, skip = config
        full_path = os.path.join(self.base_path, filename)
        
        try:
            print(f"Loading {name}...")
            df = pd.read_csv(full_path, skiprows=skip, encoding=encoding)
            return df
        except FileNotFoundError:
            print(f"Error: File {filename} not found in {self.base_path}.")
            return None
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            return None

    def load_all(self):
        for name, config in self.file_configs.items():
            df = self._load_single_file(name, config)
            if df is not None:
                self.data[name] = df
        print("Extraction complete.")
        return self.data