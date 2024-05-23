class Contacto:

    def __init__(self, nombre, apellido, direccion, correo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__correo = correo
        self.__telefono = []
        self.__palabras = []

    def darNombre(self):
        return self.__nombre

    def darApellido(self):
        return self.__apellido

    def darDireccion(self):
        return self.__direccion

    def darCorreo(self):
        return self.__correo

    def darTelefonos(self):
        return self.__telefono

    def darPalabras(self):
        return self.__palabras

    def cambiarDireccion(self, direccion):
        self.darDireccion == direccion

    def cambiarCorreo(self, correo):
        self.darCorreo == correo

    def agregarTelefono(self, telefono):
        if telefono not in self.__telefono:
            self.__telefono.append(telefono)

    def eliminarTelefono(self, telefonoEliminar):
        if telefonoEliminar in self.__telefono:
            self.__telefono.remove(telefonoEliminar)

    def agregarPalabra(self, palabra):
        if palabra not in self.__palabras:
            self.__palabras.append(palabra)

    def eliminarPalabra(self, palabraEliminar):
        if palabraEliminar in self.__palabras:
            self.__palabras.remove(palabraEliminar)

    def contienePalabraClave(self, palabra):
        palabra = False
        if palabra in self.__palabras:
            palabra = True

        return palabra