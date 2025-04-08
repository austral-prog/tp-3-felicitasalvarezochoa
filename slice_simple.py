def slice_simple():
    texto = "Awesome"
    texto=texto.lower()
    print(texto[0:3:1])
    print(texto[2:5:1])
    print(texto[0:4]+texto[-3:])


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
