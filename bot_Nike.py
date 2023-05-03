import requests
from bs4 import BeautifulSoup


def make_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    response = requests.get(url, headers=headers)
    return response


def extract_product_info(url):
    response = make_request(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    product_name_elem = soup.find('h1', {'data-testid': 'product-name',
                                         'class': 'Typographystyled__StyledHeading-sc-1h4c8w0-1 hYSqbh ProductDetails-styled__Name-sc-492918d8-6 iDjoqE'})
    if product_name_elem:
        product_name = product_name_elem.text.strip()
    else:
        product_name = None
    price_elem = soup.find('span', class_='Typographystyled__StyledHeading-sc-1h4c8w0-1 lZFLg')
    if price_elem:
        price = price_elem.text.strip()
    else:
        price = None
    return product_name, price


produtos = {}

while True:
    url = input('Digite a URL do produto do site da Nike: ')
    product_name, price = extract_product_info(url)
    if product_name and price:
        print(f'Produto: {product_name}')
        print(f'Preço: {price}')
    else:
        print('Não foi possível extrair informações do produto.')

    cliente = input("Deseja adicionar o produto à sua lista? (Sim/Não) ")
    if cliente.lower() == "sim":
        produtos[product_name] = {'preco': price, 'url': url}
        print("Produto adicionado à sua lista!")

    else:
        print("Produto não adicionado à sua lista.")

    continuar = input("Deseja continuar? (Sim ou Não): ")
    if continuar.lower() == "sim":
        continue
    else:
        break


def print_produtos_adicionados(produtos):
    print("")
    print("Resumo da lista de produtos adicionados:")
    print("")
    for i, (produto, info) in enumerate(produtos.items()):
        print(f'Produto {i + 1}: {produto}\nPreço: {info["preco"]}\nURL: {info["url"]}\n')


print_produtos_adicionados(produtos)






