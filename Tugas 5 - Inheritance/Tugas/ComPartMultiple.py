class processor():
    def __init__(self, jenisProcessor) -> None:
        self.processor = jenisProcessor

class penyimpananSementara():
    def __init__(self, ram) -> None:
        self.ram = ram

class penyimpanan():
    def __init__(self, storage) -> None:
        self.storage = storage

class computerPart(processor, penyimpananSementara, penyimpanan):
    def __init__(self, jenisProcessor, ram, storage) -> None:
        processor.__init__(self, jenisProcessor)
        penyimpananSementara.__init__(self, ram)
        penyimpanan.__init__(self, storage)

com = computerPart('i7 11400K 4.5Ghz', 'DDR4 16GB','HDD Samsung 1 TB')
print(f'Laptop dengan processor {com.processor}, dengan dilengkapi RAM {com.ram} serta penyimpanan {com.storage}')