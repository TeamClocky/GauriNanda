
let onHover = function(i) {
    const backgroundImages = ["url('static/images/Clocky_Page/black_clocky.jpg')", "url('static/images/Clocky_Page/Blue_clocky.jpg')", "url('static/images/Clocky_Page/Clocky_OverheadCol__5.jpg')"]
    document.body.style.backgroundImage = `${backgroundImages[i]}`;
}

let outHover = function(i) {
    // console.log("Off")
    document.body.backgroundImage = "none";
    // document.body.style.backgroundColor = "pink";
}
