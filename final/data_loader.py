import pandas as pd

def load_and_preprocess(csv_path):
    df = pd.read_csv(csv_path)
    
    def row_to_text(row):
        parts = []
        for col, val in row.items():
            if pd.notnull(val):
                parts.append(f"The {col} is {val}")
        # Join all column-value pairs as a natural sentence
        text = ". ".join(parts) + "."
        return text
    
    texts = df.apply(row_to_text, axis=1).tolist()
    return texts
