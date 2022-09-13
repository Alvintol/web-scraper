from bs4 import BeautifulSoup

# Direct find
  # print(soup.body)
  # print(soup.head)
  # print(soup.title)

# Find - Returns an array
  # x = soup.find('div')
  # x = soup.findAll('div') | x = soup.find_all('div')
  
  # x = soup.find(id='section')
  # x = soup.find(class_='item') - must have _ after class since saved word
  # x = soup.find(attrs={'data-id': 'test'})
  
# Select - Similar to jQuery : Always returns a list
  # x = soup.select('#section1')
  # x = soup.select('.section1')
  # x = soup.select('#section1')[0] - No longer in list
  
# Returns inner text - no tags
  # x = soup.find(class_='item')get_text()
  
  # for x in soup.select('.item'): - prints individual text
    # print(x.get_text())
  
# Navigation - Be wary of line breaks | '\n'
  # x = soup.body.contents[1] - Immediate div
  # x = soup.body.contents[1].contents[1] - Child Div
  # x = soup.body.contents[1].contents[1].find_next_sibling() - Next Child | Sibling Div
  # x = soup.find(id='section-2').find_previous_sibling()
  # x = soup.find(id='section-2').find_parent()
  # x = soup.find('h3').find_next_sibling('p') - Specific div to find