import pandas as pd


def save_to_excel(data: list[dict], filename: str = "products.xlsx"):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Saved: {filename}, rows: {len(df)}")
