# test_import.py
from mlaist.inference import classify_image

res = classify_image("https://sdrimltdata.blob.core.windows.net/melanintrainingimages/mst/PXL_20220922_185757301.jpg")
print(f"mlaist.inference imported successfully! {res}")