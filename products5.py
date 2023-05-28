import os
#讀取檔案
def read_file():
products = []
if os.path.isfile('products.csv'):檢查檔案在不再
    print('yeah!')
    with open ('products.csv', 'r', encoding='utf-8') as f:
    	for line in f:
    		if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
        print(products)
    else:
        print('找不到檔案')


#使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱')
        if name == 'q':
            break
        price = input('請輸入商品價格')
        price = int(price)
        products.append([name, price])
    print(products)
    return products

#印出所有商品紀錄
def print_products():
    for p in products:
        print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(): 
    with open('products.csv', 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')



products = read_file('products.csv')
products = user_input(products)
print_products(products)
write_file('products.csv', products)