# -*- coding: utf-8 -*-

# Kanji Coach for Anki
# Copyright (C) 2017-Present  Dorian DAUDIER
#
# This module implements functions to retrieve stroke order diagrams or
# animations.

import sqlite3 as db
from zipfile import ZipFile

from .. import kanjax_db, kanjax_zip, gifs_zip
from .exceptions import DatabaseError, StrokeFileNotFound

__all__ = ['get_img']

def get_img(kanji, database):
    """Returns the image (in byte format) corresponding to the stroke order
    for writing a kanji.

    Arguments:
      - kanji: the corresponding kanji which we return the stroke order media
      - database ('gif' | 'kanjax' | 'field={fieldname}'): the designated
      database in which to look for.
    """
    pass

def get_gif(kanji):
    """Returns a gif animation (in byte format) of the stroke order of the
    given kanji using the 'gif' database."""
    # Get the image file in kanjax.zip and return it as a byte object
    with ZipFile(gifs_zip, 'r') as myzip:
        # A zipped file is automatically read in byte mode
        with myzip.open(kanji + '.gif', 'r') as f:
            return f.read()

def get_kanjax(kanji):
    """Returns a png image (in byte format) showing the stroke order of the
    given kanji using the 'kanjax' database."""
    # In Kanjax database, retrieve the filename containing the stroke order
    try:
        conn = db.connect(kanjax_db)
        cur = conn.cursor()
        cur.execute("SELECT strokes FROM KanjiIinfo WHERE kanji=?", kanji)
        filename = cur.fetchone()
    except:
        raise DatabaseError(
            "Error while trying to connect with kanjax database")
    finally:
        conn.close()

    # If no result could be found despite valid request to the database
    if not filename:
        raise StrokeFileNotFound("Couldn't find strokes for " + kanji)

    # Get the image file in kanjax.zip and return it as a byte object
    with ZipFile(kanjax_zip, 'r') as myzip:
        # A zipped file is automatically read in byte mode
        with myzip.open(filename[0], 'r') as f:
            return f.read()

def get_from_field(kanji):
    """Returns a media file (in byte format) showing the stroke order of the
    given kanji using Anki fields."""
    pass
