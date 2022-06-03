# PolyGlot
Simple wxPython app for studying vocabulary across multiple languages at once

The goal for this project was to create a simple app that is also useful in order to get experience creating GUIs in Python. 
The user interface was created using wxPython. The automatic translations for the words is carried out by calling the Google Translate
services provided through the GoogleTrans Python package. These translation aren't perfect because the context isn't always inferred correctly, so
manual insertion is sometimes required. 

## Who is the app for?

The app is for anyone wanting to study large amounts of vocabulary all at once in any number of languages. There are many great apps for grammar and pronounciation, but I needed an app that let's you study vocabulary as fast as you can and not one phrase or word at a time. It's helpful for anyone
who needs to learn or review several languages and would like to be able to do so in parallel.

## Using the app

The layout is minimal with a tree control on the left hand side where the sections for your vocabulary are displayed. The central grid is an excel-like
data grid with the languages at the header of each column. By default, upon entering a word into the grid, Google translate will automatically fill in the entire row with the translations for each language you currently have. This feature can be disabled to manually enter your own translations. Most of the functions are carried out through buttons and text boxes on the right hand side as of now. You are able to add or remove a language, add new sections for vocabulary, sort or randomize the word order, hide and show certain languages without deleting the content, and automatically fill all empty cells for a single language at once. 
