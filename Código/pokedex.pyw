from tkinter import *
from tkinter import ttk
from poke_data import pokelist, get_pokemon_data

# Variables de color:
rojo_poke = "#ef3f36"

# Creacion y configuracion de la raiz:
raiz = Tk()                                                                                           
raiz.title("POKEDEX")
raiz.resizable(False,False)

# Creacion y configuracion del Frame:
frame_ventana_principal = Frame(raiz, width=1100, height=600, bg=rojo_poke)
frame_ventana_principal.pack()

#! ------------------------------------ IMAGE ------------------------------------

label_img = Label(frame_ventana_principal, bg=rojo_poke)
label_img.place(x=730, y=40)

#!  ----------------------------------- TYPE ------------------------------------
label_type = Label(frame_ventana_principal, bg=rojo_poke, fg= "white", text="Type:", font=("Verdana", 15) ).place(x=38, y=150)
type = StringVar()
output_type = Entry(frame_ventana_principal, textvariable = type, justify=CENTER, width=17, relief="ridge", state="readonly")
output_type.place(x=110, y=156)

#! ----------------------------------- ABILITIES -----------------------------------
label_abilities = Label(frame_ventana_principal, bg=rojo_poke, fg= "white", text="Abilities:", font=("Verdana", 15)).place(x=38, y=200)
abilities = StringVar()
output_abilities = Entry(frame_ventana_principal, textvariable = abilities, justify=CENTER, width=50, relief="ridge", state="readonly")
output_abilities.place(x=140, y=206)

#! ----------------------------------- HEIGHT -----------------------------------
label_height = Label(frame_ventana_principal, bg=rojo_poke, fg= "white", text="Height:", font=("Verdana", 15) ).place(x=38, y=250)
height = StringVar()
output_height = Entry(frame_ventana_principal, textvariable = height, justify=CENTER, width=10, relief="ridge", state="readonly")
output_height.place(x=120, y=256)

#! ----------------------------------- WEIGHT -----------------------------------
label_weight = Label(frame_ventana_principal, bg=rojo_poke, fg= "white", text="Weight:", font=("Verdana", 15) ).place(x=250, y=250)
weight = StringVar()
output_weight = Entry(frame_ventana_principal, textvariable = weight, justify=CENTER, width=10, relief="ridge", state="readonly")
output_weight.place(x=340, y=256)

#! ----------------------------------- SPECIES -----------------------------------
label_species = Label(frame_ventana_principal, bg=rojo_poke, fg= "white", text="Species:", font=("Verdana", 15) ).place(x=650, y=350)
species = StringVar()
output_species = Entry(frame_ventana_principal, textvariable = species, justify=CENTER, width=45, relief="ridge", state="readonly")
output_species.place(x=750, y=356)

#! ----------------------------------- DESCRIPTION -----------------------------------

label_description = Label(frame_ventana_principal, bg=rojo_poke, fg= "white", text="Description:", font=("Verdana", 15) ).place(x=650, y=400)
output_description = Text(frame_ventana_principal, width=50, height=5, relief="ridge") 
output_description.place(x=660, y=436)

#! ----------------------------------- STATS -----------------------------------
label_stats_titulo = Label(frame_ventana_principal, text="Base stats:", bg=rojo_poke, fg= "white", font=("Verdana", 15) ).place(x=70, y=350)

label_hp = Label(frame_ventana_principal, bg=rojo_poke, fg= "white", text="HP:", font=("Verdana", 12) ).place(x=40, y=400)
hp = StringVar()
output_hp = Entry(frame_ventana_principal, textvariable = hp, justify=CENTER, width=10, relief="ridge", state="readonly")
output_hp.place(x=90, y=400)

label_attack = Label(frame_ventana_principal, bg=rojo_poke, fg= "white", text="Attack:", font=("Verdana", 12) ).place(x=210, y=400)
attack = StringVar()
output_attack = Entry(frame_ventana_principal, textvariable = attack, justify=CENTER, width=10, relief="ridge", state="readonly")
output_attack.place(x=280, y=400)

label_defense = Label(frame_ventana_principal, bg=rojo_poke, fg= "white", text="Defense:", font=("Verdana", 12) ).place(x=390, y=400)
defense = StringVar()
output_defense = Entry(frame_ventana_principal, textvariable = defense, justify=CENTER, width=10, relief="ridge", state="readonly")
output_defense.place(x=480, y=400)

label_speed = Label(frame_ventana_principal, bg=rojo_poke, fg= "white", text="Speed:", font=("Verdana", 12) ).place(x=24, y=460)
speed = StringVar()
output_speed = Entry(frame_ventana_principal, textvariable = speed, justify=CENTER, width=10, relief="ridge", state="readonly")
output_speed.place(x=90, y=460)

label_sp_attack = Label(frame_ventana_principal, bg=rojo_poke, fg= "white", text="Sp. Atk:", font=("Verdana", 12) ).place(x=200, y=460)
sp_attack = StringVar()
output_sp_attack = Entry(frame_ventana_principal, textvariable = sp_attack, justify=CENTER, width=10, relief="ridge", state="readonly")
output_sp_attack.place(x=280, y=460)

label_sp_def = Label(frame_ventana_principal, bg=rojo_poke, fg= "white", text="Sp. Def:", font=("Verdana", 12) ).place(x=390, y=460)
sp_def = StringVar()
output_sp_def = Entry(frame_ventana_principal, textvariable = sp_def, justify=CENTER, width=10, relief="ridge", state="readonly")
output_sp_def.place(x=480, y=460)

label_total = Label(frame_ventana_principal, bg=rojo_poke, fg= "white", text="Total:", font=("Verdana", 12) ).place(x=30, y=520)
total = StringVar()
output_total = Entry(frame_ventana_principal, textvariable = total, justify=CENTER, width=15, relief="ridge", state="readonly")
output_total.place(x=90, y=520)

#! --------------------------------- COMBOBOX ----------------------------

label_combo = Label(frame_ventana_principal, bg=rojo_poke, fg= "white", text="Pokémon:", font=("Verdana", 18) ).place(x=30, y=50)
opciones_combo = pokelist
combo_text = StringVar()
combobox = ttk.Combobox(frame_ventana_principal, textvariable=combo_text, cursor="hand2",justify=CENTER, values=opciones_combo, width=18, font=("Verdana",10))
combobox.place(x=170, y=60)

def filtrar_lista(*args):

   #Reseteo los outputs al cambiar el texto del combo:
   type.set("")
   hp.set("")
   attack.set("")
   defense.set("")
   speed.set("")
   sp_attack.set("")
   sp_def.set("")
   total.set("")
   abilities.set("")
   height.set("")
   weight.set("")
   species.set("")
   output_description.config(state= NORMAL)
   output_description.delete(1.0, END)
   output_description.config(state= DISABLED)
   label_img.config(image="")


   #Filtro de opciones:
   if combobox.get() == "" :
      # Si no hay nada escrito el combo y se apreta el boton de filtrar dejo la lista como viene por defecto:
      combobox["values"] = opciones_combo
      
   else:
      # Si se escribe algo en el combo y se apreta el boton filtrar filtro la lista de opciones:
      combobox["values"] = [ poke for poke in opciones_combo if combobox.get().capitalize() in poke]

# Asocio la accion de cambiar el texto del combo a la funcion "filtrar_lista":
combo_text.trace_add('write', filtrar_lista) 

def set_data_outputs(*args):

   pokemon_data = get_pokemon_data(opciones_combo.index(combobox.get())+1)

   # Seteo el output de tipo:
   type.set( pokemon_data["type"] )
   # Seteo el output de habilidades:
   abilities.set( pokemon_data["abilities"] )
   # Seteo el output de altura:
   height.set( pokemon_data["height"] )
   # Seteo el output de peso:
   weight.set( pokemon_data["weight"] )
   # Seteo el output de especie:
   species.set( pokemon_data["species"] )
   # Seteo el output de especie:
   output_description.config(state= NORMAL)
   output_description.insert(1.0, pokemon_data["description"])
   output_description.config(state= DISABLED)
   # Imagen poke:
   image = PhotoImage(data=pokemon_data["sprite"]).subsample(2)
   label_img.config(image=image)
   label_img.image = image
   # Seteo los outputs con las estadisticas base:
   hp.set( pokemon_data["base_stats"]["hp"] )
   attack.set( pokemon_data["base_stats"]["attack"] )
   defense.set( pokemon_data["base_stats"]["defense"] )
   sp_attack.set( pokemon_data["base_stats"]["sp_attack"] )
   sp_def.set( pokemon_data["base_stats"]["sp_defense"] )
   speed.set( pokemon_data["base_stats"]["speed"] )
   total.set( int(hp.get()) + int(attack.get()) + int(defense.get()) + int(speed.get()) + int(sp_attack.get()) + int(sp_def.get()))

   # Una vez que selecciona un pokemon con exito reseteo la lista del combo:
   combobox["values"] = opciones_combo

# Asocio el evento de seleccion de opcion en el combo a la funcion "set_data_outputs":
combobox.bind("<<ComboboxSelected>>", set_data_outputs)

#!-------------------------------------------------------------------------------------------------------------

# Mainloop:
raiz.mainloop()