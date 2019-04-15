import pandas as pd

uur = pd.datetime.now().hour

if uur > 17:
    print("Het is avond")
elif uur > 11:
    print("Het is middag")
else:
    print("Het is ochtend")
