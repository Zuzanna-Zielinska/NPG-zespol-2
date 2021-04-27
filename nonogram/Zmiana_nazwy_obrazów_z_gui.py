import save_and_load as sv

p = sv.load_list_from_file('Stworzone_z_gui.pkl')
print(p[0].matrix)
#sv.rename(0, "Parasolka", 'Stworzone_z_gui.pkl')
print(p[0].name)
