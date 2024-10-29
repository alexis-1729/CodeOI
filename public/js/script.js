function toggleMenu(){
    console.log('click');
    const menu = document.getElementById('menuCurso');
     const button = document.getElementById('buttonMenu');

     const activo = button.getAttribute('aria-expanded') === 'true';
     button.setAttribute('aria-expanded', !activo);
    //  menu.classList.toggle('hidden');

    if(!activo){
        menu.classList.remove('hidden', 'opacity-0', 'translate-y-1', 'ease-in', 'duration-150');
        menu.classList.add('opacity-100', 'translate-y-0', 'ease-out', 'duration-300');
    }else{
        menu.classList.remove('opacity-100', 'translate-y-0', 'ease-out', 'duration-300');
        menu.classList.add('opacity-0', 'translate-y-1', 'ease-in', 'duration-150');
        // Espera a que termine la animación para ocultar el menú
        setTimeout(() => {
            menu.classList.add('hidden');
        }, 200); 
    }     


}