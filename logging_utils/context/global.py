# -*- coding: utf-8 -*-
""" Module providing compatibility layer with build-in logging module """
import logging
from . import LoggerContextual
from .stack import ContextStack

DEFAULT_CONTEXT_STACK = ContextStack()

def getLogger(*args, **kwargs):
    return LoggerContextual(
        DEFAULT_CONTEXT_STACK,
        logging.getLogger(*args, **kwargs)
    )
