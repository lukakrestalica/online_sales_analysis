# Online sales analysis

Luka Krestalica — završni projekat: GitHub i Python.

## Pokretanje

Potreban je Python 3.10 ili noviji. Nema dodatnih biblioteka.

```sh
git clone https://github.com/lukakrestalica/online_sales_analysis.git
cd online_sales_analysis
python main.py
```

Program kreira inventar, nasumično bira tri različita dostupna proizvoda,
dodaje po jedan komad u korpu i ispisuje stavke i ukupan iznos u EUR.
Izbor se menja između pokretanja. Konačni main.py namerno ne ispisuje
inventar, prema fazi 7 zadatka; metode za prikaz inventara ostaju dostupne.

## Klase

- `Product` čuva `name`, `price` i `quantity`. `display_info()` prikazuje
  podatke, a `update_quantity(n)` postavlja novu količinu. Cena je Decimal
  sa dve decimale; negativne i nevažeće vrednosti se odbijaju.
- `ProductManager` čuva listu `products`. `add_product()` dodaje proizvod,
  `display_products()` prikazuje inventar, `total_value()` računa zbir
  cena puta količina, a `display_total_value()` ga ispisuje.
  `remove_product(name)` uklanja po nazivu bez razlikovanja velikih i malih
  slova i vraća True/False. Dupli nazivi nisu dozvoljeni.
- `Cart` čuva listu `cart_items`. `add_product(product, quantity=1)` dodaje
  željenu količinu, `total_value()` računa naplatu, a `display_contents()`
  prikazuje korpu. Stavke su kopije proizvoda: količina u korpi nije cela
  zaliha inventara. Ponavljanje proizvoda sabira količine uz proveru zalihe.
  Primer nema checkout niti trajno smanjenje zaliha; inventar ostaje neizmenjen.

Primer korišćenja inventara:

```python
from product import Product
from product_manager import ProductManager

manager = ProductManager()
product = Product("Knjiga", "12.50", 4)
manager.add_product(product)
product.update_quantity(6)
manager.display_products()
manager.display_total_value()  # 75.00 EUR
manager.remove_product("Knjiga")
```

## Git razvoj

1. Prazan GitHub repozitorijum je kloniran; lokalno su podešeni ime,
   GitHub noreply email i Credential Manager.
2. Prvi commit dodaje Product, ProductManager i main.
3. Grana `add-product-removal` dodaje uklanjanje po imenu. Spojena je
   merge commitom bez konflikta, jer nije bilo konkurentnih izmena.
4. Grana `add-cart-functionality` dodaje korpu i nasumičan izbor proizvoda.
5. Na main promenjeni su nazivi i količine proizvoda i uklonjen ispis inventara.
6. Git je automatski spojio i granu za korpu, bez konflikta. Provereno je
   da rezultat zadržava nove nazive/količine, uklanja ispis inventara i čuva korpu.
   Ručno rešavanje konflikta nije bilo potrebno (zadatak ga traži ako nastane).
7. Dodati su .gitignore, dokumentacija i link naloga.

```sh
git log --oneline --graph --all
git status
git check-ignore -v config.json screenshots/example.png
```

## Lokalni fajlovi

`config.json` sadrži samo testne vrednosti iz zadatka i ne koristi se u programu.
Nije praćen niti uključen u Git istoriju. `.gitignore` isključuje i PNG/JPG/JPEG
snimke i Python cache. ZIP za predaju dodatno sadrži testni config, snimke i
tekstualne dnevnike izvršenih komandi. Snimci dnevnika prikazuju stvarne izlaze
u Notepadu, a ne originalne terminalske prozore. `documentation/` je lokalno
isključen kroz `.git/info/exclude`; u ZIP-u je sačuvan radi pregleda koraka.
