class Mancala():

    is_new = True

    def __init__(self, pots, stones):

        self.number_of_pots = pots
        self.number_of_stones = stones
        self.stores = [0,0]
        self.player1 = [stones] * pots
        self.player2 = [stones] * pots
        self.gameState = self.generateGameBoard(self)

    def generateGameBoard(self):

        return [self.player1, self.player2, self.stores]


    # def condition(self, name):
    #     """This function returns the condition of the Car instance. Googley
    #     docstring.
    #
    #     Args:
    #        name (str):  Some test argument.
    #
    #     Returns:
    #        str.  The return code::
    #
    #           "New" -- The car is new.
    #           "Used" -- The car is used.
    #     """
    #     if self.is_new:
    #         return "New"
    #     else:
    #         return "Used"
    #
    # def drive(self, distance):
    #     """This function drives the Car and adds to the mileage. This is a
    #     numpydoc docstring.
    #
    #     Parameters
    #     ----------
    #     distance : int
    #         This is the distance travelled by the car and will be added to the
    #         current mileage.
    #
    #     Returns
    #     -------
    #     None
    #
    #     Raises
    #     ------
    #     BadException
    #         Because you shouldn't have done that.
    #
    #     Notes
    #     -----
    #     Notes about the implementation algorithm (if needed).
    #
    #     This can have multiple paragraphs.
    #
    #     You may include some math:
    #
    #     .. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}
    #
    #     And even use a greek symbol like :math:`omega` inline.
    #
    #     """
    #     self.is_new = False
    #     self.mileage += distance
    #
    # def description(self, name):
    #     """This function prints the description of the car instance.
    #
    #     :param name: Some test argument.
    #     :type name: str.
    #     :returns:  str -- the return code.
    #     :raises: AttributeError, KeyError
    #
    #     """
    #     print("This %s was made in %s. It is %s and its condition is %s."
    #           % (self.model, self.year, self.colour, self.condition('test')))
