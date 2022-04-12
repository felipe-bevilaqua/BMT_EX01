from xml.dom import minidom

#Read
with open("./CysticFibrosis2-20220328/data/cf79.xml",'r') as f: 
    doc = minidom.parse(f)

authors = doc.getElementsByTagName("AUTHOR")
author_list = [author.firstChild.data for author in authors]

unique_authors = list(set(author_list))
unique_authors.sort()

#Write
doc = minidom.Document()
data = doc.createElement('data')
doc.appendChild(data)

for author_name in unique_authors:
    author = doc.createElement('AUTHOR')
    author.setAttribute('name', author_name)
    data.appendChild(author)

with open('autores.xml','w') as file:
    doc.writexml(file, addindent=' ', newl='\n')    
