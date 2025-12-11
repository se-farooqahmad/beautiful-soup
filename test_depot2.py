import json
import re
import csv
import requests
from bs4 import BeautifulSoup

fieldnames = [
    'Category',
    'Brand',
    'Model',
    'Product Name',
    'Product Link',
    'Description',
    'Specification',
]

# Open the file in a context manager to ensure proper closing
with open('handtools.csv', 'w', newline='', encoding='utf-8') as write_file:
    writer = csv.DictWriter(write_file, fieldnames=fieldnames)
    writer.writeheader()

    def extract_specifications(spec_data):
        result = []
        for group in spec_data:
            spec_title = group.get("specTitle", "")
            specifications = group.get("specifications", [])
            result.append(f"{spec_title}:")
            for spec in specifications:
                spec_name = spec.get("specName", "")
                spec_value = spec.get("specValue", "")
                result.append(f"  - {spec_name}: {spec_value}")
            result.append("")
        return "\n".join(result)

    def parse_product(soup):
        try:
            # Extract breadcrumb data
            breadcrumb_script = soup.select_one('#thd-helmet__script--breadcrumbStructureData')
            product_data = json.loads(breadcrumb_script.string) if breadcrumb_script else {}
            product_url = product_data.get('url', '')
            breadcrumbs = product_data.get('breadcrumb', {}).get('itemListElement', [])
            category = " / ".join(
                breadcrumb["item"]["name"] 
                for breadcrumb in breadcrumbs 
                if breadcrumb["item"]["name"] not in ["Home", "Tools"]
            )

            # Extract product details
            product_script = soup.select_one('#thd-helmet__script--productStructureData')
            some_product_data = json.loads(product_script.string) if product_script else {}
            model = some_product_data.get('model', '')
            productID = some_product_data.get('productID', '')
            brand = some_product_data.get('brand', {}).get('name', '')

            # Placeholder for script with ROOT_QUERY
            script_tag = soup.find('script', text=re.compile("ROOT_QUERY"))
            script_text = re.search(r'({.*})', script_tag.string) if script_tag else None
            json_data = json.loads(script_text.group(1)) if script_text else {}
            data = json_data.get(f'base-catalog-{productID}', {})

            # Extract remaining details
            product_name = data.get('identifiers', {}).get('productLabel', '')
            partial_description = data.get('details', {}).get('description', '')
            highlights = data.get('details', {}).get('highlights', [])
            highlights = "\n".join(highlights) if isinstance(highlights, list) else str(highlights)
            descriptive_attributes = data.get('details', {}).get('descriptiveAttributes', [])
            remaining_description = "".join(attr['value'] for attr in descriptive_attributes)
            latter = f"Product Information, Internet # {productID} Model # {model}"

            description = f"{partial_description} Highlights {highlights} {remaining_description} {latter}"
            spec_data = data.get('specificationGroup', [])
            specifications_string = extract_specifications(spec_data)

            # Write to CSV
            writer.writerow({
                'Category': category,
                'Brand': brand,
                'Model': model,
                'Product Name': product_name,
                'Product Link': product_url,
                'Description': description,
                'Specification': specifications_string,
            })
        except Exception as e:
            print(f"Error parsing product: {e}")

    # Example URL
    url = 'https://www.homedepot.com/p/Husky-Mechanics-Tool-Set-270-Piece-H270MTSQ223/323565221'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    parse_product(soup)
