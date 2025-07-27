from pathlib import Path
import json
from scripts.single_sample_classify import classify_from_json

with open("data/raw/malware/fea01760226c661437f992a077b9ebb8fff2d65ed1d591049e4cb5c8a0bb0dc0(1).json", 
          "r", encoding="utf-8") as f:
    js = json.load(f)

label, prob, _ = classify_from_json(js, Path("models/gnn/res_gcl/res_gcl.pt"))
print("malware sample",end=" ")
print(label, prob)

with open("data/raw/benign/e97fde1aa1260261577d81203a2a0b1b666e7774b44f42be89c84065d93e89e6.json", 
          "r", encoding="utf-8") as f:
    js = json.load(f)

label, prob, _ = classify_from_json(js, Path("models/gnn/res_gcl/res_gcl.pt"))
print("benign sample",end=" ")
print(label, prob)