function sendUpdate(field, value) {
    fetch('/auth/update_user_info', {
        method: 'POST',
        body: JSON.stringify({ 'field': field, 'value': value }),
        headers: {
            'Content-Type': 'application/json',
            // Assuming CSRF token is set in a cookie named 'csrf_token'
            'X-CSRFToken': getCookie('csrf_token') // Function to get cookie by name
        }
    })
    .then(response => response.json())
    .then(data => {
        if(data.success) {
            alert('Information updated successfully!');
            const button = document.getElementById(`button-${field}`);
            button.textContent = 'Edit'; // Reset the button to 'Edit' state
        } else {
            alert(`Failed to update information: ${data.message}`);
        }
    }).catch(error => {
        console.error('Error:', error);
    });
}

function toggleEditSave(button, input) {
    const field = input.getAttribute('id');
    if(button.textContent === 'Edit'){
        input.readOnly = false;
        button.textContent = 'Save';
        input.focus();
    } else {
        const value = input.value;
        sendUpdate(field, value);
    }
}

document.addEventListener('DOMContentLoaded', (event) => {
    document.querySelectorAll('.btn-edit-save').forEach(button => {
        button.addEventListener('click', function() {
            const field = this.dataset.field;
            const input = document.getElementById(field);
            toggleEditSave(this, input);
        });
    });
});

// Function to get a cookie by name
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