function getAscii(){
    let imageUrl = document.getElementById("url-input").value
    let width = document.getElementById("width-input").value
    let height = document.getElementById("height-input").value

    console.log(width)
    console.log(height)

    let url = `https://shrouded-lake-21821.herokuapp.com/generate?width=${ width }&height=${ height }&url=${ imageUrl }`
    let response = fetch(url);

    fetch(url)
    .then(response => response.text())
    .then(data => (
        document.getElementById("image-box").innerHTML = `<pre style="font-size: ${ 60/width }vw">${ data }</pre>` //
        ))
    .then(data => console.log(data))
    .catch(error => {
        // handle the error
    });
}