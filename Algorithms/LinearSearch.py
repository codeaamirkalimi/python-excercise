class LinearSearch:
    def __init__(self, arr, size, key):
        self.arr = arr
        self.size = size
        self.key = key

    def search(self):
        for i in range(self.size):
            if self.arr[i] == self.key:
                return True
        return False


if __name__ == "__main__":
    pageNum = [86, 91, 34, 50, 0]
    key = 4
    linearSearch = LinearSearch(pageNum, len(pageNum), key)
    if linearSearch.search():
        print("Search Found")
    else:
        print("Not Found")
