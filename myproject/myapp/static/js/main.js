// static/js/main.js

document.addEventListener('DOMContentLoaded', () => {

    // Functionality for the "Copy to Clipboard" buttons
    const allCopyButtons = document.querySelectorAll('.copy-btn');

    allCopyButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            const buttonEl = event.currentTarget;
            const preElement = buttonEl.previousElementSibling;
            
            if (preElement && preElement.tagName === 'PRE') {
                const textToCopy = preElement.innerText;
                
                navigator.clipboard.writeText(textToCopy).then(() => {
                    // Provide visual feedback to the user
                    const originalIcon = buttonEl.innerHTML;
                    buttonEl.innerHTML = '<i class="bi bi-check-lg"></i>';
                    buttonEl.classList.add('btn-success');

                    // Revert back to the original state after 2 seconds
                    setTimeout(() => {
                        buttonEl.innerHTML = originalIcon;
                        buttonEl.classList.remove('btn-success');
                    }, 2000);

                }).catch(err => {
                    console.error('Failed to copy text: ', err);
                    // You could add an error state here if you want
                });
            }
        });
    });

});