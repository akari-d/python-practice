import csv
import random

product_info = {
    "コーヒー": ["Drink", 450, 1],
    "ホットサンド" : ["food", 800, 3],
    "ベーグル":["food", 300, 4],
    "ココア":["Drink", 250, 2],
    "キッシュ": ["food", 700, 5],
    "ドーナツ": ["food", 300, 6]
}

# CSVファイルを作成し、データを書き込む

with open('input.csv', 'w', newline='', encoding= "utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["商品ID", "商品名", "価格", "カテゴリー" ,"在庫数"])

    for _ in range(100):
        stock_quantity = random.randint(10, 51)
        p, info = random.choice(list(product_info.items()))
        product= p
        amount = info[1]
        category = info[0]
        product_id = info[2]
        writer.writerow([product_id, product, amount, category, stock_quantity])

print("CSVファイルが生成されました。")
