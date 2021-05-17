import save_and_load as sv

p = sv.load_list_from_file('Stworzone_z_gui.pkl')
print(len(p))

n = 3 #id obrazka

print(p[n].matrix)
sv.rename(n, "Serce", 'Stworzone_z_gui.pkl')
print(p[n].name)
