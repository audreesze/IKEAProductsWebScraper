import url_tools
import re

#URLs for various pages as strings
couch_url = "https://www.ikea.com/us/en/catalog/categories/departments/living_room/39130/"
samplecouch = "https://www.ikea.com/us/en/catalog/products/S19150508/"



#Soupify from URL
all_couches_soup = url_tools.get_soup_from_url(couch_url)
sample_couch_soup = url_tools.get_soup_from_url(samplecouch)

#extracting the data, sample...
#gets all of the product titles and
products = all_couches_soup.findAll("div", class_="threeColumn product ")
for p in products:
    title = p.find("span", class_="productTitle").text
    short_description = p.find("span", class_="productDesp").text
    print(title,": ", short_description, "Colors: ", sep = "")

url_tools.get_cache_file_name(couch_url)
