def encrypt(message, shift):
    """
    Encripta el mensaje dado usando el cifrado de Julio César.

    :param message: El mensaje a encriptar.
    :param shift: El desplazamiento utilizado para el cifrado.
    :return: El mensaje encriptado.
    """
    encrypted_message = ''
    for char in message:
        if char.isalpha():
            # Obtiene el índice de la letra actual en el alfabeto
            char_index = ord(char.lower()) - 97

            # Aplica el desplazamiento y asegura que esté dentro del rango de letras
            shifted_index = (char_index + shift) % 26

            # Obtiene la letra encriptada y la agrega al mensaje encriptado
            encrypted_char = chr(shifted_index + 97)
            encrypted_message += encrypted_char.upper() if char.isupper() else encrypted_char
        else:
            # La letra no es parte del alfabeto, simplemente la agrega al mensaje encriptado
            encrypted_message += char

    return encrypted_message


# Ejemplo de uso
mensaje = input("Ingrese el mensaje a encriptar:  ")
desplazamiento = int(input("ingresa cuanto se va a desplazar: "))
mensaje_encriptado = encrypt(mensaje, desplazamiento)
print("Mensaje encriptado:", mensaje_encriptado)
