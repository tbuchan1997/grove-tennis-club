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
const rescheduleButtons = document.querySelectorAll('.reschedule-button');

rescheduleButtons.forEach(button => {
    button.addEventListener('click', function() {
        const bookingId = this.dataset.bookingId;
        const rescheduleUrl = this.dataset.rescheduleUrl; // Assuming this is set using {% url %}

        window.location.href = `${rescheduleUrl}?reschedule_id=${bookingId}`;
    });
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

