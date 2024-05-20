class CustomIterator:
    def __init__(self, sequence):
        self._index = 0
        self._sequence = sequence

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._sequence):
            raise StopIteration
        else:
            item = self._sequence[self._index]
            self._index += 1
            return item


obj = CustomIterator([10,20,30,40,50])

for i in obj:
    print(i)