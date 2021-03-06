# -*- coding: utf-8 -*-

# Kanji Coach for Anki
# Copyright (C) 2017-Present  Dorian DAUDIER
#
# This module implements functions to retrieve stroke order diagrams or
# animations.

from zipfile import ZipFile

from .. import kanjax_zip, gifs_zip
from .exceptions import StrokeFileNotFound
from .kanjax_api import get_strokes

__all__ = ['get_img']

def get_img(kanji, database):
    """Returns the image (in byte format) corresponding to the stroke order
    for writing a kanji.

    Arguments:
      - kanji: the corresponding kanji which we return the stroke order media
      - database ('gif' | 'kanjax' | 'field={fieldname}'): the designated
      database in which to look for.
    """
    if database == 'gif':
        return get_gif(kanji)
    if database == 'kanjax':
        try:
            return get_kanjax(kanji)
        except StrokeFileNotFound:
            pass
    if database[:6] == 'field=':
        return get_from_field(kanji)

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
    filename = get_strokes(kanji).encode()  #converts unicode name to string

    # Get the image file in kanjax.zip and return it as a byte object
    # A zipped file is automatically read in byte mode
    with ZipFile(kanjax_zip, 'r') as myzip:
        # Raise exception if no result could be found in the database or if it
        # doesn't match an actual file.
        if (not filename) or (filename[0] not in myzip.namelist()):
            raise StrokeFileNotFound("Couldn't find strokes for " + kanji)
        with myzip.open(filename[0], 'r') as f:
            return f.read()

def get_from_field(kanji):
    """Returns a media file (in byte format) showing the stroke order of the
    given kanji using Anki fields."""
    pass
