from category import Category

category_1 = Category(name="Filme", description="Filmes em Geral")
category_2 = Category(name="Série", description="Séries em Geral")
category_3 = Category(name="Filme", description="Filmes em Geral")

print(category_1 == category_2)  # category_1.__eq__(category_2)
print(category_2 == category_3)  # category_2.__eq__(category_3)
print(category_1 == category_3)  # category_1.__eq__(category_3)
