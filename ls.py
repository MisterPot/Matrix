class list(list):

    def replace(self, from_, to_, max_replaces=1, from_end=False):

        def fr_start():
            for i in range(0, max_replaces):
                index = self.index(from_)
                self[index] = to_
            return self

        def fr_end():
            self.reverse()
            types = [str, list, set, frozenset]

            if type(from_) in types:
                fr_rev = from_[::-1]
            else:
                fr_rev = from_

            if type(to_) in types:
                to_rev = to_[::-1]
            else:
                to_rev = to_

            for i in range(0, max_replaces):
                index = self.index(fr_rev)
                self[index] = to_rev

            return self.reverse()

        d = {False: fr_start,
             True: fr_end}
        return d[from_end]()

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
