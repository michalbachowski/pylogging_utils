# encoding: utf-8
from __future__ import absolute_import

import logging

from ._version import __version__
from .context import LoggerContextual
from .context.stack import ContextStack
from .sentinel import SentinelBuilder

DEFAULT_CONTEXT_STACK = ContextStack()

def getLogger(*args, **kwargs):
    return LoggerContextual(
        DEFAULT_CONTEXT_STACK,
        logging.getLogger(*args, **kwargs)
    )

__all__ = ['__version__', 'getLogger', SentinelBuilder]
