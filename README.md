# Sign Language Translator
Take a picture, put it into the Glitch AI, put the json file you get through wow.py
The image that you will get will look something like this
![sign language a](annotated_media-a[1].png)

It should be initialized as `wow.py <json_file_name.json>`
The corresponding letter in the English Alphabet will be printed on the console.

We used the relative distances between joint points to elimntate the possible translations. 
For example
  - if index and middle fingers are crossed, we have r
  - if all the fingers other than the thumb are straight and pointed up, we have b
  - and so on (w/ three fingers, different 'levels', etc)

#### Order of elimination:
r, o,

b,

f, w, k

u, v, 

l, d , z, y, i , j

h, p, g, q

t, c, x, n, m, a, e, s

