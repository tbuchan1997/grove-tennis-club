const modal = document.getElementById("bookingModal");
const modalBody = document.getElementById("modal-body")
const availabilityInput = document.getElementById("modal-availability");
const bookButtons = document.querySelectorAll(".book-button");
const closeButton = document.getElementsByClassName("close-button")[0];

bookButtons.forEach(button => {
    button.onclick = function(event) {
        event.preventDefault()
        modal.style.display = "block";
        availabilityInput.value = this.dataset.availability;
        modalBody.innerHTML = `
        <p>Court: ${this.dataset.court}</p>
        <p>Time: ${this.dataset.time}</p>
        <p>Are you sure you want to book this slot?</p>`
    }
});

closeButton.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}