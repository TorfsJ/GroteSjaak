from input.formatter import XmlFormatter
from input.xml_reader import XmlReader

class InputService:

    def read_files(self, fileuris):
        files = []
        reader = XmlReader()
        for uri in fileuris:
            file = reader.readfile(uri)
            files.append(file)


    def create_collection(self, files):
        formatter = XmlFormatter()
        for file in files:
            formatter.converttothreads(file)
