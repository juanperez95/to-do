import { defineStore } from 'pinia'
import Swal from 'sweetalert2'

export const useAlertStore = defineStore('alertas',()=>{
    // Funcion para mostrar un mensaje de alerta
    const mostrarAlerta = (titulo: string, texto: string, icono: string, color: string, isToast:boolean = false) => {
        Swal.fire({
            title: titulo,
            text: texto,
            icon: icono,
            showCancelButton: true,
            confirmButtonColor: color,
            confirmButtonText: 'Aceptar',
            toast: isToast,
            position: 'bottom-end',
            timer: 4000,
        })
    }

    return {mostrarAlerta}
})