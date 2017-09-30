# -*- coding: utf-8 -*-
#
# Kanji Coach for Anki
# Copyright (C) 2017-Present  Dorian DAUDIER
#
# This module implements functions to communicate with Kanjax database

import sqlite3 as db

from .exceptions import DatabaseError
from .. import kanjax_db

__all__ = ['get_strokes', 'get_keyword', 'get_description', 'get_kanji_from_keyword']

def get_strokes(kanji):
    """Returns the filename stored in the 'strokes' field for a given Kanji in
    kanjax database. None is returned if no result can be found."""
    return get_field('strokes', kanji)

def get_keyword(kanji):
    """Returns the keyword of a given kanji in kanjax database.
    None is returned if no result can be found."""
    return get_field('keyword', kanji)

def get_description(kanji):
    """Returns a description of the kanji's meaning in kanjax database.
    None is returned if no result can be found."""
    return get_field('desc', kanji)

def get_field(field, kanji):
    """Returns a field corresponding to a kanji in kanjax database.
    None is returned if no result can be found."""

    try:
        conn = db.connect(kanjax_db)
        cur = conn.cursor()
        cur.execute("SELECT %s FROM KanjiIinfo WHERE kanji=?" % field, (kanji,))
        res = cur.fetchone()
    except:
        raise DatabaseError(
            "Error while trying to connect with kanjax database")
    finally:
        conn.close()
    # if a result could be found, return it. None will be returned otherwise
    if res:
        return res[0]
    else:
        raise Exception("SELECT %s FROM KanjiIinfo WHERE kanji=%s failed" % (field, kanji))

def get_kanji_from_keyword(keyword):
    """Returns the kanji strored kanjax database matching a given meaning."""
    try:
        conn = db.connect(kanjax_db)
        cur = conn.cursor()
        cur.execute("SELECT kanji FROM KanjiIinfo WHERE keyword=?", (keyword,))
        res = cur.fetchone()
    except:
        raise DatabaseError(
            "Error while trying to connect with kanjax database")
    finally:
        conn.close()
    # if a result could be found, return it. None will be returned otherwise
    if res:
        return res[0]
