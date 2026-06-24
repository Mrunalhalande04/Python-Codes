#[1,[2,[3,[4]],5]] → [1,2,3,4,5]


class Flatten:

    def __init__(self, A):
        self.Arrr = A
        self.result = []

    def FlattenList(self, Arr):

        for item in Arr:

            if isinstance(item, list):
                self.FlattenList(item)
            else:
                self.result.append(item)


def main():

    dobj = Flatten([1, [2, [3, [4]], 5]])

    dobj.FlattenList(dobj.Arrr)

    print("Elements:")
    print(dobj.result)


if __name__ == "__main__":
    main()