document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.btn-edit-save').forEach(button => {
        button.addEventListener('click', function() {
            const field = this.dataset.field;
            const input = document.getElementById(field);
            toggleEditSave(this, input);
        });
    });
});


// Function to toggle between editing and saving
function toggleEditSave(button, input) {
    // const field = input.getAttribute('id');
    if(button.textContent === 'Edit'){
        input.readOnly = false;
        button.textContent = 'Save';
        input.focus();
    } else if(button.textContent === 'Save') {
        const value = input.value;
        input.readOnly = true;
        button.textContent = 'Edit';
        // sendUpdate(field, value);
        sendUpdate(input.id, value); // Use input.id instead of field
    }
}

function sendUpdate(field, value) {
    fetch('/auth/update_user_info', {
        method: 'POST',
        body: JSON.stringify({ 'field': field, 'value': value }),
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => response.json())
    .then(data => {
        if(data.success) {
            showToast('Information updated successfully!');
            const button = document.getElementById(`button-${field}`);
            button.textContent = 'Edit'; // Reset the button to 'Edit' state
        } else {
            showToast(`Failed to update information: ${data.toast.message}`, 'danger');
        }
    }).catch(error => {
        console.error('Error:', error);
    });
}

// showToast function to display Bootstrap toast messages
function showToast(message, type='success') {
    const toastContainer = document.getElementById('toastContainer');

    const toastTemplate = document.getElementById('toastTemplate').cloneNode(true);
    toastTemplate.id = '';
    toastTemplate.classList.remove('hide');

    // Set message content and category
    const toastHeaderClass = (type === 'danger') ? 'bg-danger text-white' : 'bg-success text-white';
    toastTemplate.querySelector('.toast-header').className += ` ${toastHeaderClass}`;
    toastTemplate.querySelector('.toast-body').textContent = message;

    // Append the cloned template to the DOM
    toastContainer.appendChild(toastTemplate);

    // Show the toast
    const toast = new bootstrap.Toast(toastTemplate);
    toast.show();

}


