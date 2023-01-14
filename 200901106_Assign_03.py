import xml.etree.ElementTree as ET

tree = ET.parse("compiler.xml")
root = tree.getroot()
for book in root.findall('book'):
    book_id = book.get('id')
    author_name = book.find('author').text
    title = book.find('title').text
    genre = book.find('genre').text
    price = book.find('price').text
    publish_date = book.find('publish_date').text
    description = book.find('description').text
    #print the extracted data
    print(f'Book Id: {book_id}')
    print(f'Author Name: {author_name}')
    print(f'Title: {title}')
    print(f'Genre: {genre}')
    print(f'Price: {price}')
    print(f'Publish Date: {publish_date}')
    print(f'Description: {description}')
