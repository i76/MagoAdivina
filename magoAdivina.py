#!/usr/bin/env python
# coding: utf-8

# In[1]:


secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
number = int(input())
while number != 777:
    number = int(input("¡Ja, ja! ¡Estás atrapado en mi bucle!, introduce otro numero entero: "))
    
else:
    print("¡Bien hecho, muggle! Eres libre ahora")


# In[ ]:





# In[ ]:




