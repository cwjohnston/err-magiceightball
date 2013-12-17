# This is a magic eight ball Err plugin
# Answers lifted from http://en.wikipedia.org/wiki/Magic_8-Ball

from errbot import BotPlugin, botcmd
import random


class MagicEightBall(BotPlugin):
    """A magic eight ball plugin"""
    min_err_version = '1.6.0'  # Optional, but recommended
    max_err_version = '2.0.0'  # Optional, but recommended

    # Passing split_args_with=None will cause arguments to be split on any kind
    # of whitespace, just like Python's split() does
    @botcmd(split_args_with=None)
    def eightball(self, mess, args):
        """Provides guaranteed answers to your yes-no questions"""

        if len(args) > 0:
            answers = [ "It is certain",
            "It is decidedly so",
            "Without a doubt",
            "Yes definitely",
            "You may rely on it",
            "As I see it, yes",
            "Most likely",
            "Outlook good",
            "Yes",
            "Signs point to yes",
            "Reply hazy try again",
            "Ask again later",
            "Better not tell you now",
            "Cannot predict now",
            "Concentrate and ask again",
            "Don't count on it",
            "My reply is no",
            "My sources say no",
            "Outlook not so good",
            "Very doubtful" ]

            return answers[random.randint(0, len(answers))-1]
        else:
            return "Please state a yes-no question"
