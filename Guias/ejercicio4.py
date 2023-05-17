# Elaborar un algoritmo que solicite al usuario su nombre y el nombre de otra
# persona. Luego, mostrar en pantalla un mensaje que indique si ambos nombres
# comienzan con la misma letra o si terminan con la misma letra, o si difieren tanto
# en la letra inicial como en la final. Por ejemplo, si los nombres ingresados son
# Belinda y Beatriz, se mostrara un mensaje que indique que ambos nombres comienzan con la misma letra. 
# Si los nombres son Leonardo y Gonzalo, se mostrara  un mensaje que indique que ambos nombres terminan 
# con la misma letra.

n1 = str(input("ingrese el primer nombre : "))
n2 = str(input("ingrese el segundo nombre : "))

if n2[0] == n1[0]:
    print("los dos nombres empiezan por la misma letra")
elif n2[-1] == n1[-1] :
    print("los nombres terminan por la misma letra")
    if n1[0] != n1 [0]:
        print("los nombres no coinciden en su letra inicial")
        if n1[-1] != n2[-1]:
            print("los nombres no coinciden en su ultima letra")
            