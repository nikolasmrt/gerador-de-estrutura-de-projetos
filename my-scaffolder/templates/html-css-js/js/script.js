// js/script.js
document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('myButton');

    if (button) {
        button.addEventListener('click', () => {
            alert('Botão clicado! Este é um script JavaScript básico do projeto {{ project_name }}.');
            console.log('Projeto: {{ project_name }}');
            console.log('Autor: {{ author }}');
        });
    }

    console.log('Script.js carregado para o site: {{ site_title }}');
});