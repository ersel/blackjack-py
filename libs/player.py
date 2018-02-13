class Player:
    def __init__(self, deposit):
        self.hands = []
        self.balance = deposit
        self.staked = 0
        self.insured = False

    def deposit(self, deposit):
        if(deposit > 0):
            self.balance += deposit
        else:
            raise ValueError('Deposit must be higher than 0')

    def stake(self, staked):
        if (staked < 1):
            raise ValueError('Stake must be higher than 0')

        if (staked <= self.balance):
            self.balance -= staked
            self.staked += staked
        else:
            raise ValueError('Insufficient balance of £{}, can not stake £{}'.format(self.balance, staked))

    def insure(self):
        if self.insured:
            raise ValueError('Already insured')

        insurance_cost = self.staked / 2
        if (insurance_cost <= self.balance):
            self.balance -= insurance_cost
            self.insured = True
        else:
            raise ValueError('Insufficent balance to insure')

    def hands_played(self):
        return False if False in [hand.is_finalized() for hand in self.hands] else True

    def get_hand_to_play(self):
        return [hand for hand in self.hands if not hand.is_finalized()][0]

