#a)
with open("product.csv","r") as f:
    product_n_price = f.read()
    print(f.read())

#b) and d)
new_product = input("Enter a new product: ")
if new_product in product_n_price:
    print("duplicate product")
    
else:
    new_price = input("Enter a new product price: ")

    #c)
    with open("product.csv","a") as f:
        f.write(new_product + "," + new_price + "\n")
    print("new product added")

    #e)
    with open("product.csv","r") as f:
        pro_pri_list = f.read().split("\n")
    print(pro_pri_list)
    print("Product\t\tPrice")
    for item in pro_pri_list:
        items = item.split(",")
        product = items[0]
        price = items[-1]
        print(product,"\t\t",price)
