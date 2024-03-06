document.addEventListener('DOMContentLoaded', () => {
    const registrationForm = document.getElementById('registration-form');
    if (registrationForm) {
        registrationForm.addEventListener('submit', function (event) {
            event.preventDefault();

            const formData = new FormData(this);

            const actionUrl = registrationForm.getAttribute('action');
            fetch(actionUrl, {
                method: 'POST',
                body: new URLSearchParams(formData),
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            }).then(response => response.json())
            .then(data => {
                showToast(data.toast.message, data.toast.type);

                if (!data.success) {
                    Object.keys(data.form_data).forEach(key => {
                        const input = document.getElementsByName(key)[0];
                        if(input) {
                            input.value = data.form_data[key];
                        }
                    });
                }
            }).catch(error => {
                console.error('Error:', error);
                showToast('An unexpected error occurred.', 'danger');
            });
        });
    }
});