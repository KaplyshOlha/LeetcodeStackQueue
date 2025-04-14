class FreqStack(object):

    def __init__(self):
        self.stack = []
        self.freq = {}

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1

    def pop(self):
        """
        :rtype: int
        """
        if not self.stack:
            raise ValueError('Stack is empty.')

        max_freq = max(self.freq.values())

        for i in range(len(self.stack) - 1, -1, -1):
            val = self.stack[i]
            if self.freq[val] == max_freq:
                self.freq[val] -= 1
                if self.freq[val] == 0:
                    del self.freq[val]
                del self.stack[i]
                return val
