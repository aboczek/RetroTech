document.addEventListener("DOMContentLoaded", () => {
    setTimeout(() => {
        const msg = document.querySelector("#msg");
        if (msg) {
            msg.parentNode.removeChild(msg);
        }
    }, 3000);
});