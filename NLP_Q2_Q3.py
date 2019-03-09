import numpy as np


class Dictionary:
    
    def __init__(self, lst):
        self.conn = {word: set() for word in lst}
        for i, word1 in enumerate(lst):
            for word2 in lst[i+1:]:
                if self.check(word1, word2):
                    self.conn[word1].add(word2)
                    self.conn[word2].add(word1)
                
    @staticmethod
    def check(word1, word2):
        if len(word1) == len(word2):
            check = 0
            for k, char in enumerate(word1):
                if char == word2[k]:
                    if k == len(word1) - 1:
                        return True
                    continue
                if abs(ord(char) - ord(word2[k])) >= 10:
                    break
                check += 1
                if check > 1:
                    break
                if k == len(word1) - 1:
                    return True
        return False
    
    def distance(self, start, end):
        start_set = set()
        end_set = {start}
        result = 0
        while start_set != end_set:
            third_set = end_set.copy()
            for word in third_set - start_set:
                if self.check(word, end):
                    return result + 1
                if word == start:
                    for w in self.conn:
                        if self.check(word, w):
                            end_set.add(w)
                else:
                    end_set = end_set.union(self.conn[word])
            start_set = third_set
            result += 1
        return np.inf

    def __str__(self):
        return str(self.conn)


class SparseMatrixException(Exception):
    pass


class SparseMatrix:
    
    def __init__(self, num_rows, num_cols, values):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.values = values
    
    def __eq__(self, other):
        return self.num_rows == other.num_rows and self.num_cols == other.num_cols and self.values == other.values
    
    def __add__(self, other):
        if not (self.num_rows == other.num_rows and self.num_cols == other.num_cols):
            return SparseMatrixException('two matrices cannot be summed')
        for key in other.values:
            self.values[key] = self.values.get(key, 0) + other.values[key]
        for key in self.values.copy():
            if self.values[key] == 0:
                self.values.pop(key)
        return self
    
    def __sub__(self, other):
        if not (self.num_rows == other.num_rows and self.num_cols == other.num_cols):
            return SparseMatrixException('two matrices cannot be subtracted')
        for key in other.values:
            self.values[key] = self.values.get(key, 0) - other.values[key]
        for key in self.values.copy():
            if self.values[key] == 0:
                self.values.pop(key)
        return self
    
    def __mul__(self, other):
        if isinstance(other, SparseMatrix):
            if self.num_cols != other.num_rows:
                return SparseMatrixException('two matrices cannot be multiplied')
            new = SparseMatrix(self.num_rows, other.num_cols, {})
            for key1 in self.values:
                for key2 in other.values:
                    if key1[1] == key2[0]:
                        new.values[(key1[0], key2[1])] = new.values.get((key1[0], key2[1]), 0) + \
                                   self.values[key1] * other.values[key2]
            for key in new.values.copy():
                if new.values[key] == 0:
                    new.values.pop(key)
            return new
        else:
            for key in self.values:
                self.values[key] *= other
            return self
    
    def __str__(self):
        return str(self.values)


# Q2

print(Dictionary(['hot', 'dot', 'dog', 'lot', 'log']).distance('hit', 'cog'))

print(Dictionary(['hot', 'dot', 'don', 'dog', 'lot', 'log']).distance('hit', 'cog'))

print(Dictionary(['hot', 'cot', 'con', 'lot', 'log']).distance('hit', 'cog'))

# Q3

print(SparseMatrix(2, 2, {(0, 0): 1}) + SparseMatrix(2, 2, {(0, 0): 1, (1, 1): 1}) == \
      SparseMatrix(2, 2, {(0, 0): 2, (1, 1): 1}))

print(SparseMatrix(2, 2, {(0, 0): 1}) - SparseMatrix(2, 2, {(0, 0): 1, (1, 1): 1}) == \
      SparseMatrix(2, 2, {(1, 1): -1}))

print(SparseMatrix(2, 3, {(0, 0): 1}) * SparseMatrix(3, 2, {(0, 0): 1, (0, 1): 1}) == \
      SparseMatrix(2, 2, {(0, 0): 1, (0, 1): 1}))

print(SparseMatrix(2, 2, {(0, 0): 1}) * 2 == SparseMatrix(2, 2, {(0, 0): 2}))

print(SparseMatrix(2, 3, {(0, 0): 1}) * SparseMatrix(4, 2, {(0, 0): 1, (0, 1): 1}))



### test commit
