$('form input[type="file"]').change(event => {
    let files = event.target.files;
    if (files.lenght === 0) {
        console.log('Sem imagem para mostrar.')
    } else {
        if (files[0].type == "image/jpeg") {
            $('img').remove();
            let image = $('<img class="img-fluid">');
            image.attr('src', window.URL.createObjectURL(files[0]));
            $('figure').prepend(image);
        } else {
            alert('Formato não suportado!')
        }
    }
});
