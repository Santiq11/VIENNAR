import urllib.request
import html
import json
import re

req = urllib.request.Request(
    'https://naturalwheysuplementos.com/producto/ashwagandha-pura/',
    headers={'User-Agent': 'Mozilla/5.0'}
)
content = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')

match = re.search(r'data-product_variations="([^"]+)"', content)
if match:
    data = json.loads(html.unescape(match.group(1)))
    print(f"Total variations: {len(data)}")
    for v in data:
        attr = v.get('attributes', {})
        price = v.get('display_price')
        reg_price = v.get('display_regular_price')
        sku = v.get('sku')
        print(f"Tamaño: {attr} | Precio minorista: ${price} ARS | Mayorista (-30%): ${price * 0.70:.2f} ARS | SKU: {sku}")
else:
    print("No variations attribute found directly, finding woocommerce prices:")
    prices = re.findall(r'woocommerce-Price-amount amount[^>]*><bdi>([^<]+)', content)
    for p in set(prices):
        print(p)
