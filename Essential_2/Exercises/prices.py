products = {"ψωμί": 1.50,
            "γάλα": 2.00,
            "κουλούρι": 0.50,
            "αυγό": 0.10}

product = input("Enter the product you want: ")

print(products.get(product, "We have no such product"))

