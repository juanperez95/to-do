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

// Interface para definir la tarea
export type Todo = {
    id?: String, // Se maneja id de django en formato UUID
    titulo: String,
    descripcion: String,
    fecha_creacion?: String,
    fecha_modificacion?: String,
    estado?: String,
    // Especificar si la tarea se completo
    cumplido?: Boolean,
}