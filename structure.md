DECK = dict(все карты)

class Game_Instance
  Players: me, enemy
  

class Player
  hp
  mz
  class stack
  class hand
  class field

  def drawCard(self)
  def playCard(self, indexFrom, indexTo)
    
  

class Stack
  stack = list()
  def push(self, card)
  def pop(self) -> card


class Hand
  cards = list()
  
  def get(index) -> card
  def remove(index)
  def push(card)
  

class Field
  cards = [card1, card2, card3, card4]

  def getCard(self, index)
  def setCard(self, card, index) # С логикой, запрещающей перезапись карт
  def removeCard(self, index)
  

class Card
  def Copy(self) -> Card

class Unit(Card)

class Item(Card)

class Location(Card)

class Event(Card)


class Event
  activation_condition
  exit_condition

  def куча_condition-ов:
  
