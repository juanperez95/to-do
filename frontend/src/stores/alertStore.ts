import { defineStore } from 'pinia'
import Swal from 'sweetalert2'

export const useAlertStore = defineStore('alertas',()=>{
    // Funcion para mostrar un mensaje de alerta
    const mostrarAlerta = (titulo: string, texto: string, icono: string, color: string, isToast:boolean = false, tiempo:Boolean = false) => {
        Swal.fire({
            title: titulo,
            text: texto,
            icon: icono,
            confirmButtonColor: color,
            confirmButtonText: 'Aceptar',
            toast: isToast,
            position: isToast ? 'bottom-end' : 'center',
            timer: !tiempo ? 4000 : 10000, //Indicar que si el tiempo es definido solo son 10 segundos de mensaje
        })
    }

    return {mostrarAlerta}
})