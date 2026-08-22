function toggleMenu(){
    const nav = document.getElementById("nav");
    if(nav) nav.classList.toggle("open");
}
document.querySelectorAll("nav a").forEach(a => {
    a.addEventListener("click", () => {
        const nav = document.getElementById("nav");
        if(nav) nav.classList.remove("open");
    });
});
