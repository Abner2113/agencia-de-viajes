    document.addEventListener('DOMContentLoaded', function() {
        const toggleButtons = document.querySelectorAll('.toggle-modulo');

        toggleButtons.forEach(button => {
            button.addEventListener('click', function() {
                const moduloNombre = this.getAttribute('data-modulo');
                const checkboxes = document.querySelectorAll(`.permiso-checkbox[data-modulo="${moduloNombre}"]`);
                const allChecked = Array.from(checkboxes).every(cb => cb.checked);

                checkboxes.forEach(checkbox => {
                    checkbox.checked = !allChecked;
                });

                if (allChecked) {
                    this.innerHTML = '<i class="bi bi-check2-square"></i> Seleccionar todo';
                } else {
                    this.innerHTML = '<i class="bi bi-square"></i> Deseleccionar todo';
                }
            });
        });

        const checkboxes = document.querySelectorAll('.permiso-checkbox');
        checkboxes.forEach(cb => {
            cb.addEventListener('change', function() {
                const label = this.closest('.form-check')?.querySelector('.form-check-label');
                if (this.checked) {
                    label?.classList.add('fw-semibold');
                    label?.style.setProperty('color', '#FF6B47');
                } else {
                    label?.classList.remove('fw-semibold');
                    label?.style.setProperty('color', '#1E293B');
                }
            });
            if (cb.checked) {
                const label = cb.closest('.form-check')?.querySelector('.form-check-label');
                label?.classList.add('fw-semibold');
                label?.style.setProperty('color', '#FF6B47');
            }
        });
    });
