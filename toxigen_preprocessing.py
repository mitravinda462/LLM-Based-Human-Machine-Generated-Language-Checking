from datasets import load_dataset
import pandas as pd

ds = load_dataset("toxigen/toxigen-data", "annotated")
test_ds = pd.DataFrame(ds['test'])
data['label'] = data['label'].replace({1: 'toxic', 0: 'benign'})
# Rename columns to match the desired JSON structure
data.rename(columns={'text': 'claim'}, inplace=True)
data['label'] = data['label'].replace({'toxic': 'REFUTES', 'benign' : 'SUPPORTS'})
data.to_json('toxigen_claims.jsonl', orient='records', lines=True)
