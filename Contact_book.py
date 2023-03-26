#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 15:05:16 2023

@author: itixa
"""

class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact):
        self.contacts.append(contact)
    
    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"{name} has been removed from the contact book.")
                return
        print(f"{name} was not found in the contact book.")
    
    def display_contacts(self):
        if not self.contacts:
            print("The contact book is empty.")
            return
        for contact in self.contacts:
            print(f"Name: {contact.name}")
            print(f"Phone Number: {contact.phone_number}")
            print(f"Email: {contact.email}")
    
    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                return
        print(f"{name} was not found in the contact book.")
