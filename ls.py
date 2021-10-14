class list(list):

    def replace(self, from_, to_, max_replaces=1, from_end=False):

        if from_end:
            self.reverse()

        for i in range(0, max_replaces):
            index = self.index(from_)
            self[index] = to_

        if from_end:
            self.reverse()
            return self
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


class InfinityRange(object):

    def __init__(self, *args):

        config = {
            "first": 0,
            "second": 0,
            "count": 1,
            "step": 1,
            "start_from": None,
        }
        if len(args) == 1:
            config['second'] = args[0]
            self.start_from = self.first
        else:
            for key, value in zip(config.keys(), args):

                if value is None:
                    break
                config[key] = value
        for key, value in zip(config.keys(), config.values()):
            self.__dict__[key] = value

        if self.step == 0:
            raise ValueError('Step not be equal 0')

        if self.start_from is None:
            self.start_from = self.first
        self.progress_count = 0

    def __iter__(self):
        def height_zero():
            self.start_from -= self.step

            while True:

                self.start_from += self.step
                if self.progress_count == self.count:
                    return 'Stop'

                if self.start_from == self.second:
                    self.start_from = self.first

                elif self.start_from > self.second:
                    odds = self.start_from - self.second
                    self.start_from = self.first
                    self.start_from += odds

                self.progress_count += 1

                yield self.start_from

        def sub_zero():
            self.start_from -= self.step

            while True:

                self.start_from += self.step

                if self.progress_count == self.count:
                    return 'Stop'

                if self.start_from == self.first:
                    self.start_from = self.second

                elif self.start_from < self.first:
                    odds = self.start_from
                    self.start_from = self.second
                    self.start_from += odds

                self.progress_count += 1

                yield self.start_from

        ls = {True: height_zero,
              False: sub_zero}

        return ls[self.step > 0]()


ir = InfinityRange
