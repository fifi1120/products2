
while True:
    name = input ("请输入商品名称：")
    if name == "q": #quit逃出回圈!!
        break
    price = input ("请输入商品价格：")
    p = [name, price]
    products.append(p)
print(products)
