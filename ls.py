class list(list):

    def replace(self, from_, to_, max_replaces=1, from_end=False):

        if from_end:
            self.reverse()

        for i in range(0, max_replaces):
            index = self.index(from_)
            self[index] = to_

        if from_end:
            return self.reverse()
        return self

    def stringify(self):
        st = ''
        for i in self:
            st += str(i)
        return st

    def __iter__(self):
        return super(list, self).__iter__()

    def map(self, function, *args, **kwargs):
        for e in self:
            function(e, *args, **kwargs)
