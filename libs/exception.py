"""
Module contenant des exceptions personnalisées pour le programme TryCount.

Ce module définit plusieurs classes d'exceptions qui peuvent être levées pour signaler des erreurs spécifiques.
"""

class ExceptionNotValidFile(Exception):
    """
    Exception levée lorsque le fichier n'est pas valide.
    """
    pass

class ExceptionNotValidParameter(Exception):
    """
    Exception levée lorsque les paramètres ne sont pas valides.
    """
    pass

class ExceptionNotInstance(Exception):
    """
    Exception levée lorsque l'instance n'est pas valide.
    """
    pass
