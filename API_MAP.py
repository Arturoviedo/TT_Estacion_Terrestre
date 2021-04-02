# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 11:52:37 2021

@author: cruov
"""


import requests
import smtplib

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="AIzaSyDs1IbevQyqEZlkzB5yldU-zP1V9hoBEWU")
location = geolocator.geocode("175 5th Avenue NYC")
print(location.address)

print((location.latitude, location.longitude))

print(location.raw)
