"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""

rows = 9
for i in range(rows):
    print( i )

    # spaces = '  ' * abs((4 -i))
    spaces =  ((4 -i))

    if(4-i) >= 0:
        stars = '* ' * (2 * i + 1)
    else:
        stars =  ((2 * (i-1) + 1) - 2)
        # stars = '* ' * ((2 * (i-1) + 1) - 2)

    print('spaces ' ,spaces)
    print('stars ' ,stars)
