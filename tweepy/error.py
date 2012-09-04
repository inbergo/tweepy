# Tweepy
# Copyright 2009-2010 Joshua Roesslein
# See LICENSE for details.

class TweepError(Exception):
    """Tweepy exception"""

    def __init__(self, reason, response=None):
        self.reason = unicode(reason)
        self.response = response
        self.original_reason = reason

    def __str__(self):
        return self.reason

class AccessDenied(TweepError):
    pass

class DoesNotExist(TweepError):
    pass

class LimitExceeded(TweepError):
    pass

class InvalidCredentials(TweepError):
    pass