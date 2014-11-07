DEFAULT_SCORE = 500


class Leagues():
    """
    Corresponds to: http://en.wikipedia.org/wiki/Elo_rating_system#United_States_Chess_Federation_ratings
    """
    BRONZE = 'Bronze'
    SILVER = 'Silver'
    GOLD = 'Gold'
    PLATINUM = 'Platinum'
    DIAMOND = 'Diamond'
    MASTER = 'Master'
    GRAND_MASTER = 'Grand Master'

    SILVER_THRESHOLD = 500
    GOLD_THRESHOLD = 800
    PLATINUM_THRESHOLD = 1200
    DIAMOND_THRESHOLD = 1600
    MASTER_THRESHOLD = 2000
    GRAND_MASTER_THRESHOLD = 2400


class Keys():
    WIN = 'win'
    RANDOM = 'random'
