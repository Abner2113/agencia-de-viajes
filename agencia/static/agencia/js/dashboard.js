    const hora = new Date().getHours();

    document.getElementById('fechaHoy').textContent = new Date().toLocaleDateString('es-MX', {
        weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'
    });

    function abrirModal() {
        document.getElementById('modalReserva').style.display = 'block';
        document.body.style.overflow = 'hidden';
    }
    function cerrarModal() {
        document.getElementById('modalReserva').style.display = 'none';
        document.body.style.overflow = '';
    }
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') cerrarModal();
    });
 
    // Calendario
    let calendario; 
    function buildUrl() {
        const params = new URLSearchParams();
        const cliente = document.getElementById('filtroCliente').value.trim();
        const paquete = document.getElementById('filtroPaquete').value;
        const estado  = document.getElementById('filtroEstado').value;
        if (cliente) params.set('cliente', cliente);
        if (paquete) params.set('paquete', paquete);
        if (estado)  params.set('estado', estado);
        return RESERVAS_URL + (params.toString() ? '?' + params.toString() : '');
    }
 
    function aplicarFiltros() {
        calendario.removeAllEventSources();
        calendario.addEventSource(buildUrl());
    }
 
    function limpiarFiltros() {
        document.getElementById('filtroCliente').value = '';
        document.getElementById('filtroPaquete').value = '';
        document.getElementById('filtroEstado').value  = '';
        aplicarFiltros();
    }
 
    document.addEventListener('DOMContentLoaded', function () {
        const el = document.getElementById('calendario');
        if (!el) return;
 
        calendario = new FullCalendar.Calendar(el, {
            initialView: 'dayGridMonth',
            locale: 'es',
            height: 'auto',
            headerToolbar: {
                left:   'prev,next today',
                center: 'title',
                right:  'dayGridMonth,timeGridWeek,listMonth'
            },
            buttonText: { today: 'Hoy', month: 'Mes', week: 'Semana', list: 'Lista' },
            events: RESERVAS_URL,
            eventClick: function (info) {
                const p = info.event.extendedProps;
                document.getElementById('m-cliente').textContent  = p.cliente;
                document.getElementById('m-paquete').textContent  = p.paquete;
                document.getElementById('m-empleado').textContent = p.empleado;
                document.getElementById('m-fecha').textContent    = info.event.startStr;
                document.getElementById('m-precio').textContent   = '$' + p.precio;
                document.getElementById('m-metodo').textContent   = p.metodo;
                document.getElementById('m-estado').textContent   = p.estado;
                document.getElementById('m-editar').href          = p.editar_url;
                abrirModal();
            },
        });
        calendario.render();
    });
