const container = document.getElementById("widget-container");
const widgets = document.querySelectorAll('.widget');
let draggedItem = null;

widgets.forEach(widget => {
    widget.addEventListener('dragstart', () => {
        draggedItem = widget;
        widget.classList.add('dragging');
    });

    widget.addEventListener('dragend', () => {
        widget.classList.remove('dragging');
        draggedItem = null;
    });

    widget.addEventListener('dragover', (e) => {
        e.preventDefault(); // Allows drop
    });

    widget.addEventListener('drop', (e) => {
        e.preventDefault();
        if (draggedItem && draggedItem !== widget) {
            container.insertBefore(draggedItem, widget);
        }
    });
});
