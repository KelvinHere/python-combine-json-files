import json
import time 

startTime = time.time()

# Open Files
with (open('prices.txt', encoding="utf8") as f_prices,
      open('products.txt', encoding="utf8") as f_descriptions,
      open('urls.txt', encoding="utf8") as f_urls):
    prices = json.load(f_prices)
    data = json.load(f_descriptions)
    urls = json.load(f_urls)

# Count items in prices file
count = 0
for item in prices['SONAS-PRODUCTS']:
    count += 1
print(f'Product price count = {count}')

# Count products in description file
count = 0
for item in data['details']:
    count += 1
print(f'Product description count = {count}')

# Count products in description file
count = 0
for item in urls['SONAS urls']:
    count += 1
print(f'Product URL count = {count}')

# Combine data
count = 0
new_json = []
for item in data['details']:
    # Add image filenames to item data
    for url in urls['SONAS urls']:
        if url['Sku'] == item['sku']:
            item['filename'] = url['Image Name']
            break
    for price in prices['SONAS-PRODUCTS']:
        if price['Sku'] == item['sku']:
            item['RRP Euro'] = price['RRP Euro']
            break

# Build JSON from combined data
new_json = []
for item in data['details']:
    # Create Base JSON structure
    new_item = {'details':
                    {'prodPriceInfo':[
                            {
                            "type":"Main+Price",
                            "subtype":"<br+/>",
                            "name":"<br+/>",
                            "price":item['RRP Euro']
                            }
                        ]
                    }
                }
    # Add description
    new_item['details']['prodDescription'] = item['description']
    # Add title
    new_item['details']['prodTitle'] = item['name']
    # Add price
    new_item['details']['prodPrice'] = item['RRP Euro']
    # Add stock
    new_item['details']['prodStock'] = 999
    # Add ranking
    new_item['details']['prodRanking'] = 1000
    # Add SKU
    new_item['details']['prodCode'] = item['sku']
    # Add plain text
    new_item['details']['prodPlainText'] = ""
    # Add category tags
    new_item['details']['prodTags'] = "NEED ACCESS FROM DMAC MEDIA"
    # Add files
    new_item['details']['prodFiles'] = []
    # Add file url
    new_item['details']['prodImages'] = [{"file": item['filename'],"main":1}]
    # Append to list
    new_json.append(new_item)

    # Log item
    count += 1
    print(f'Built JSON for product {count}')


# Create new file with JSON data
with open("new.txt", 'w', encoding="UTF-8") as new_file:
    new_file.write(json.dumps(new_json, indent=4))

print ('JSON Built in {0} seconds.'.format(time.time() - startTime))
