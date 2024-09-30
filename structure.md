DECK = dict(все карты)

class Game_Instance
  Players: me, enemy
  

class Player
  hp
  mz
  class stack
  class hand
  class field

  def drawCard(self, stack, hand)

  def returnToStack(self, index):
    stack.push(DECK[field[index].name].copy())

  def playCard(indexFrom, indexTo):
  card = hand.get(indexFrom)
  match card.
    if field.getCard(index) == None:
      field.setCard(card, index)
    
  

class Stack
  stack = list()
  def push(card)
  def pop() -> card


class Hand
  cards = list()
  
  def get(index) -> card
  def remove(index)
  def push(card)
  

class Field
  cards = [card1, card2, card3, card4]

  def getCard(index)
  def setCard(card, index) #Если передать None то карта удалится
  

Class Card
  def Copy

class Event
  activation_condition
  exit_condition

  def куча_condition-ов:
  
