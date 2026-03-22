document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent default form submission

            const formData = new FormData(this);

            fetch('/auth/login', {
                method: 'POST',
                body: new URLSearchParams(formData),
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            })
            .then(response => {
                // Check if the response is JSON
                const contentType = response.headers.get('Content-Type');
                // if (!response.ok) {
                //     throw new Error('Network response was not ok.');
                // } else if (!contentType || !contentType.includes('application/json')) {
                //     throw new TypeError('Expected JSON response but received: ' + contentType);
                // }
                if (!response.ok && !contentType.includes('application/json')) {
                    throw new Error('Network response was not ok.');
                }
                return response.json();
            })
            .then(data => {
                if (data.success) {
                    window.location.href = data.redirect_url;
                } else {
                    showToast(data.toast.message, data.toast.type);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showToast('An error occurred during login.', 'danger');
            });
        });
    }
});