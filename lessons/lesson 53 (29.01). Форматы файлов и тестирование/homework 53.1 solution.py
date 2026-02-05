import csv
import json

def analyze_sales(filename):
    дата_отчета = '2024-10-02'
    # дата_отчета = input("Введите дату для отчетности (формат YYYY-MM-DD): ")

    products = dict()
    stores = dict()
    date_found = False

    with open(filename, 'r', encoding='utf-8') as file:
        reader = list(csv.reader(file))
        for row in reader[1:]:
            date, store, product, price, quantity = row
            if дата_отчета != date:
               continue

            print(row)
            date_found = True
            if store in stores:
                stores[store] += int(quantity) * float(price)
            else:
                stores[store] = int(quantity) * float(price)

            if product in products:
                products[product] += int(quantity)
            else:
                products[product] = int(quantity)

    if date_found:
        max_store_name = max(stores.keys(), key=lambda x: stores[x])
        выручка = stores[max_store_name]
    
        print('Наибольшие продажи за ', дата_отчета, ": ", max_store_name, " с объемом продаж ", выручка, sep="")

        with open('report.json', 'w') as file:
            json.dump(products, file, indent=4, ensure_ascii=False)
    else:
        print("Данные за указанную дату не найдены.")

analyze_sales('primer.csv')
