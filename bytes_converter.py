class BytesConverter():
    def get_megabytes(self, size: int) -> str:
        return str(round(size / 1000, 1)) + 'Mb'

if __name__ == '__main__':
    converter = BytesConverter()
    print(converter.get_megabytes(263352))