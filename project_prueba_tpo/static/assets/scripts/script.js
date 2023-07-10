document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('formulario');

    form.addEventListener("submit", onformSubmit);
});


function onformSubmit(event){
    event.preventDefault();
    const data = new FormData(event.target);
    const name = data.get("name");
    const email = data.get("mail");
    const text  = data.get("msg");
    if(name.length == 0 || email.length ==0 ){
        alert('No has escrito nada en el usuario');
        return;
    }
    console.log(`Nombre: ${name}, correo electronico: ${email}, mensaje: ${text}`);
    alert('¡Has enviado el correo gracias por comunicarte!')
}

        // Clave de API de YouTube Data API v3
        const apiKey = 'AIzaSyD890kS_i4fbXhuMMsQhPSCAwH-Yr7s2Pc';

        // URL base de la API de YouTube Data API v3
        const baseUrl = 'https://www.googleapis.com/youtube/v3';

        // Función para buscar videos en YouTube
        function buscarVideos(event) {
            event.preventDefault();
            
            const query = document.getElementById('query').value;

            // URL de la API de YouTube Data API v3 para buscar videos
            const url = `${baseUrl}/search?part=snippet&q=${query}&maxResults=8&key=${apiKey}`;

            // Configuración de la solicitud HTTP
            const options = {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            };

            // Realizar la solicitud HTTP
            fetch(url, options)
                .then(response => response.json())
                .then(data => {
                    console.log('Respuesta de la API de YouTube:', data);
                    mostrarVideos(data.items);
                })
                .catch(error => {
                    console.error('Error al buscar videos:', error);
                    alert('Error al buscar videos en YouTube. Por favor, revisa la consola para obtener más detalles.');
                });
        }

        // Función para mostrar los videos en la página
        function mostrarVideos(videos) {
            const videosContainer = document.getElementById('videos');
            videosContainer.innerHTML = '';

            videos.forEach(video => {
                const videoTitle = video.snippet.title;
                const videoId = video.id.videoId;

                const videoElement = document.createElement('div');
                videoElement.innerHTML = `<h3 style=color:gold; margin:0;>${videoTitle}</h3>
                                          <iframe width="360" height="180" src="https://www.youtube.com/embed/${videoId}" frameborder="0" allowfullscreen></iframe>`;

                videosContainer.appendChild(videoElement);
            });
        }