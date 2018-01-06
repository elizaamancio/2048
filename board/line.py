from board.field import Field

class Line:
    def __init__(self, beam):
        self.beam = [Field(x) for x in beam]

    def squeeze(self):
        nonzero_beam = []
        zero_beam = []
        zero_field = Field(0)

        for field in self.beam:
            if field == zero_field:
                zero_beam.append(field)
                continue

            if len(nonzero_beam) > 0 and field == nonzero_beam[-1]:
                nonzero_beam[-1].squeeze()
                zero_beam.append(zero_field)
                continue

            if field != zero_field:
                nonzero_beam.append(field)


        self.beam = nonzero_beam + zero_beam


