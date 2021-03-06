# https://rocket.chat/docs/developer-guides/rest-api/

from datetime import datetime as dt
from pprint import pprint
import secrets

from rocketcomm import RocketComm

#########
# TOOLS #
#########


def _is_correct_image(url):
    return True


def _is_benoipocalypse(date, benoipocalypse_start, benoipocalypse_stop):
    return False


def _is_troll(date, troll_start):
    return False


def _check_benoipocalypse(msg, benoit):
    return 0


def _add_image(normal_mode, name, date):
    return normal_mode


def _compute_normal_mode(scores, normal_mode):
    return scores

#########
# SCORE #
#########


def _compute_score(rocket, settings, scores, since=None):
    msgs = rocket.get_raw_msgs(self, settings, since)

    benoipocalypse_starts = rocket.check_special_string(settings, since, settings["Benoipocalypse_start"])
    benoipocalypse_stops = rocket.check_special_string(settings, since, settings["Benoipocalypse_stop"])
    troll_starts = rocket.check_special_string(settings, since, settings["DontFeedTheTroll"])

    normal_mode = {}

    for msg in msgs:
        # BENOIT
        if _is_benoipocalypse(msg["date"], benoipocalypse_starts, benoipocalypse_stops):
            removed_points = _check_benoipocalypse(msg["msg"], settings["Benoipocalypse_word"])
            # more processing TODO

        # Someone posted an image !
        if msg["url"] != "":
            if _is_correct_image(url): # That's benoit_jeune image
                if _is_troll(msg["date"], troll_starts): # that's OK, we just feed the troll
                    added_points = 1
                    # more processing TODO
                else:
                    normal_mode = _add_image(normal_mode, msg["name"], msg["date"])  # For now we just stack the valids messages

            else:  # Uh oh, wrong image, why not try #memes ?
                removed_points = 1
                # more processing TODO

    scores = _compute_normal_mode(scores, normal_mode)

    return scores

