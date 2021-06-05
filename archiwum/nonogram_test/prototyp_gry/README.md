Folder z grą w najbardziej aktualnym wydaniu\
W razie problemów ze ścieżką należy sprawdzić czy 'working directory' jest poprawnie ustawione\
(łatwo to sprawdzić poprzez kod import os; print(os.getcwd()))\
\
ZMIANY 26.04:\
save_and_load - dodałem jedną funkcję na samym końcu, zmieniłem funkcję zmieniającą na solved - teraz przyjmuje typ na który ma zmienić a nie zmienia automatycznie na True\
main - implementacja pliku save_and_load, dostosowanie wysokości okna do monitorów o rodzielczości HD, na razie bez zachowania proporcji - elementy mogą nie mieścić się na ekranie\
Aby zagrać w nonogramy o id 0, 2, 3 należy zmienić zmienną size_of_nonogram na 2 (zamiast 15)
