let changeImage = document.getElementById("puppyImage");
let likeiconi = document.getElementById("likeIcon");
let likebuttonb = document.getElementById("likeButton");
let isImageLiked = false

function onClickLikeButton() {
    if (isImageLiked === false) {
        changeImage.src = "https://d1tgh8fmlzexmh.cloudfront.net/ccbp-dynamic-webapps/white-puppy-liked-img.png";
        likeiconi.style.color = "#0967d2";
        likebuttonb.style.backgroundColor = "#0967d2";
        likebuttonb.style.color = "#ffffff";
        isImageLiked = true;
    } else {
        changeImage.src = "https://d1tgh8fmlzexmh.cloudfront.net/ccbp-dynamic-webapps/white-puppy-img.png";
        likeiconi.style.color = "#cbd2d9";
        likebuttonb.style.backgroundColor = "#cbd2d9";
        likebuttonb.style.color = "#9aa5b1";
        isImageLiked = false;
    }
}