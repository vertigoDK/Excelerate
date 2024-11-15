import pandas as pd
from app.services.llm.base_llm import BaseLLM

class ExcelHandler:
    def __init__(self):
        self.llm = BaseLLM()

    def read_excel(self, file_path: str):
        try:
            excel_data = pd.read_excel(file_path)
            return excel_data.to_string(index=False)
        except Exception as e:
            print(f"Error reading Excel file: {e}")
            return None

