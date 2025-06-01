import { defineStore } from 'pinia'
import {ref} from 'vue'

export const useThemeStore = defineStore('theme', ()=>{
    
    // Variable con las clases de tema
    const theme = ref<string>("");

    // Cambiar tema
    const cambiarTheme = () => {
        if(localStorage.getItem("theme") === "dark"){
            localStorage.removeItem("theme");
            localStorage.setItem("theme", "light");
            theme.value = "";
        }else if(localStorage.getItem("theme") === "light"){
            localStorage.removeItem("theme");
            localStorage.setItem("theme", "dark");
            theme.value = "bg-black text-white";
        }else{
            
            // Crear el localStorage
            localStorage.setItem("theme", "dark");
        }
    }

    const validarTheme = () => {
        // Validar que tema tiene el localStorage
        if(localStorage.getItem("theme") === "dark"){
            theme.value = "bg-black text-white";
        }else if(localStorage.getItem("theme") === "light"){
            theme.value = "";
        }
    }

    

    return {theme, cambiarTheme, validarTheme}
})