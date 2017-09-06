# -*- coding: utf-8 -*-

# Kanji Coach for Anki
# Copyright (C) 2017-Present  Dorian DAUDIER
#
# This module implements functions to retrieve stroke order diagrams or
# animations.

from . import kanjax_db, kanjax_zip, gifs_zip

__all__ = ['get_img']

class StrokeFileNotFound(Exception):
    pass

class StrokeDatabaseNotFound(Exception):
    pass

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
    pass

def get_kanjax(kanji):
    """Returns a png image (in byte format) showing the stroke order of the
    given kanji using the 'kanjax' database."""
    pass

def get_from_field(kanji):
    """Returns a media file (in byte format) showing the stroke order of the
    given kanji using Anki fields."""
    pass
