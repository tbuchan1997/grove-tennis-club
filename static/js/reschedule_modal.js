// Function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Cancel Modal
const cancelModal = document.getElementById("cancelModal");
const cancelButtons = document.querySelectorAll(".cancel-button");
const confirmCancelButton = document.getElementById("confirmCancelButton");
const cancelCancelButton = document.getElementById("cancelCancelButton")
let bookingIdToCancel = null;

if (cancelCancelButton) {
    cancelCancelButton.addEventListener('click', () => {
      cancelModal.style.display = "none";
    });
  }

cancelButtons.forEach(button => {
    button.addEventListener('click', (event) => {
        event.preventDefault();
        bookingIdToCancel = button.dataset.bookingId;
        cancelModal.style.display = "block";
    });
});

if (confirmCancelButton) {
    confirmCancelButton.addEventListener('click', () => {
        if (bookingIdToCancel) {
            fetch(`/cancel_booking/${bookingIdToCancel}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
            })
            .then(response => {
                if (response.ok) {
                    window.location.reload();
                } else {
                    console.error("Error cancelling booking:", response.status);
                    alert("An error occurred while cancelling the booking.");
                }
            })
            .catch(error => {
                console.error("Error cancelling booking:", error);
                alert("An error occurred while cancelling the booking.");
            });
        }
        cancelModal.style.display = "none";
    });
}

if (cancelCancelButton) {
    cancelCancelButton.addEventListener('click', () => {
        cancelModal.style.display = "none";
    })
}

// Reschedule Modal
const rescheduleModal = document.getElementById("rescheduleModal");
const rescheduleButtons = document.querySelectorAll(".reschedule-button");
const rescheduleCloseButton = rescheduleModal.querySelector(".close-button");

rescheduleButtons.forEach(button => {
    button.addEventListener('click', () => {
        rescheduleModal.style.display = "block";
    });
});

rescheduleCloseButton.addEventListener('click', () => {
    rescheduleModal.style.display = "none";
});

window.onclick = function(event) {
    if (event.target == rescheduleModal) {
        rescheduleModal.style.display = "none";
    }
};

const dateForm = document.querySelector("#rescheduleModal form"); // Select the form inside the modal

dateForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
    // Here you can handle what happens after the user selects a date
    const selectedDate = document.getElementById('date').value;
    console.log("Selected date:", selectedDate);
    // You can now update the availability data here if needed
    // For now, let's just log the selected date and keep the modal open
});

// Close modals when clicking outside
window.onclick = function(event) {
    if (event.target == cancelModal) {
        cancelModal.style.display = "none";
    }
    if (event.target == rescheduleModal) {
        rescheduleModal.style.display = "none";
    }
};

