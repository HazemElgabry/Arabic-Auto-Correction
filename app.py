import streamlit as st
from colorama import Fore, Back, Style
from ar_corrector.corrector import Corrector

def Correcting_Spelling(Corrubted_Text):
  corr = Corrector()

  Corrected_Text = corr.contextual_correct(Corrubted_Text)

  print("Our Corrubted Text: " + Corrubted_Text + "\n")
  print("Our Corrected Text: ", end="")

  Corrubted_Words = Corrubted_Text.split(" ")
  Corrected_Words = Corrected_Text.split(" ")
  Printed_text = ""

  for corrubted_word, corrected_word in zip(Corrubted_Words, Corrected_Words):
    if corrubted_word != corrected_word:
      Printed_text += ":red[" + corrected_word + "] "
      print(Fore.RED + corrected_word + " ", end="")
    else:
      Printed_text += corrected_word + " "
      print(corrected_word + " ", end="")
    print(Style.RESET_ALL, end="")
  
  return Printed_text


Corrubted_Text = st.text_input('Please Enter The Wrong Sentence')

if (Corrubted_Text != ""):
  corrected = Correcting_Spelling(Corrubted_Text)

  st.write('Corrected Text: ', corrected)
