import { defineStore } from 'pinia'
import axios from 'axios';

export const useUserStore = defineStore('user', {
    state: () => ({
        user: {
            username: '',
            first_name: '',
            last_name: '',
            email: '',
            password: '',
            password_confirmation: '',
        },
        respuesta: null,
    }),
    actions: {
        async crearUsuario(){
            try{
                const respuesta = await axios.post('http://localhost:8000/api/v1/users/',this.user);
                this.respuesta = respuesta.data;
            }
            catch(error){
                console.log(error);
            }
        }
    }
});