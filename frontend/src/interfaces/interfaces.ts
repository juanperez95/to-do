// Interface de usuario
export type Usuario = {
    username: string,
    first_name?: string,
    last_name?: string,
    email?: string,
    password: string,
}

// Interface para definir los datos de la propiedad
export type Login = {
    is_login?: Boolean,
    // Manejar diferente IDS para los modales
    id_modal:String
}