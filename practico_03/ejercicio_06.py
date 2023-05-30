"""Magic Methods"""

from __future__ import annotations
from typing import List


class Article:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Article('{self.name}')"

    def __eq__(self, other: Article) -> bool:
        if isinstance(other, Article):
            return self.name == other.name
        return False

    def __hash__(self) -> int:
        return hash(self.name)


class ShoppingCart:
    def __init__(self, articles: List[Article] = None) -> None:
        if articles is None:
            self.articles = []
        else:
            self.articles = articles

    def __str__(self) -> str:
        return str([str(article) for article in self.articles])

    def __repr__(self) -> str:
        return f"ShoppingCart({repr(self.articles)})"

    def __eq__(self, other: ShoppingCart) -> bool:
        if isinstance(other, ShoppingCart):
            return set(self.articles) == set(other.articles)
        return False

    def add(self, article: Article) -> ShoppingCart:
        self.articles.append(article)
        return self

    def remove(self, remove_article: Article) -> ShoppingCart:
        self.articles = [article for article in self.articles if article != remove_article]
        return self

    def __add__(self, other: ShoppingCart) -> ShoppingCart:
        if isinstance(other, ShoppingCart):
            return ShoppingCart(self.articles + other.articles)
        return NotImplemented


# NO MODIFICAR - INICIO

manzana = Article("Manzana")
pera = Article("Pera")
tv = Article("Television")

# Test de conversión a String
assert str(ShoppingCart().add(manzana).add(pera)) == "['Manzana', 'Pera']"

# Test de reproducibilidad
carrito = ShoppingCart().add(manzana).add(pera)
assert carrito == eval(repr(carrito))

# Test de igualdad
assert ShoppingCart().add(manzana) == ShoppingCart().add(manzana)

# Test de remover objeto
assert ShoppingCart().add(tv).add(pera).remove(tv) == ShoppingCart().add(pera)

# Test de igualdad con distinto orden
assert ShoppingCart().add(tv).add(pera) == ShoppingCart().add(pera).add(tv)

# Test de suma
combinado = ShoppingCart().add(manzana) + ShoppingCart().add(pera)
assert combinado == ShoppingCart().add(manzana).add(pera)

# NO MODIFICAR - FIN
