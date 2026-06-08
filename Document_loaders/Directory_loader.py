from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path='C:\myproj\Langchain-Basic-Projects\Document_loaders\Books',
    glob = '*.pdf',
    loader_cls= PyPDFLoader
)

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)