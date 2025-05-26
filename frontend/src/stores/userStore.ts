import { defineStore } from 'pinia'
import axios from 'axios';
import {ref} from 'vue'

// Metodos para el uso de la api
type Metodo = "GET" | "POST" | "PUT" | "DELETE";



export const useUserStore = defineStore('user', ()=>{
    const datos = ref([]); // Eje para devolver los datos

    // Almacenar el token generado en django
    const access_token = ref<string|null>(null);


    // Funcion para obtener todos los usuarios
    const apiUsuarios = async (link?: string, metodo: Metodo|null = null, data?: object, token: string|null = null):Promise<any> => {

        try {

            // Cargar datos con lo de la peticion
            datos.value = await axios.request({
                url: link,
                method: metodo as string,
                data: data,
                headers: token !== null ? { Authorization: `Bearer ${token}` } : {},
                withCredentials: true,
            }).then(response => {
                return response.data
            }).catch(error => {
                return error
            });

            return datos.value;
            
        } catch (error) {
            console.log(error);
        }
        // Finalizar de pasar los datos a variable 
    }

    return {apiUsuarios, access_token}
})