# -*- coding: utf-8 -*-
""" Provide the Vegreferanse class """
from .util import _fetch_data

class Vegreferanse(object):
    """ Class for working with road refferences.
    ¨TODO: trenger jeg "meta"?
    Endepunktet Veg, er ikke sentralt i denne klassen. Da det kun kan brukes
    for punkter, og ikke strekninger.
    Trenger jeg denne klassen? For stedfesting i datafangst brukes lenke.
    Dog den kan jeg hente herifa..

    ønsket funksjonalitet :
    Start - fra veg Endepunktet
    slutt - fra veg Endepunktet
    lengde - slutt - start
     """
    def __init__(self, nvdb, vegreferanse, meta=None):
        super(Vegreferanse, self).__init__()
        self.vegreferanse = vegreferanse
        self.nvdb = nvdb
        self.data = meta
        if self.vegreferanse.find('-'):
            self.strekning = True
        else:
            self.strekning = False

    @property
    def start(self):
        """
        return the start of a Vegreferanse range
        """
        if not self.data:
            self.data = _fetch_data(self.nvdb, 'veg', payload={'vegreferanse':self.vegreferanse})
        start = self.vegreferanse.split('-')[0]

        return self.data['vegreferanse']
    
    
        
    @property
    def veglenke(self):
        """
        :Attribute type: Dict
        :keys: ['id', 'kortform', 'posisjon']
        """
        if not self.data:
            self.data = _fetch_data(self.nvdb, 'veg', payload={'vegreferanse':self.vegreferanse})
        return self.data['veglenke']
    
    @property
    def geometri(self):
        """
        :Attribute type: Well known text
        """
        if not self.data:
            self.data = _fetch_data(self.nvdb, 'veg', payload={'vegreferanse':self.vegreferanse})
        return self.data['geometri']['wkt']
    
    def __str__(self):
        return '{}'.format(self.vegreferanse)
