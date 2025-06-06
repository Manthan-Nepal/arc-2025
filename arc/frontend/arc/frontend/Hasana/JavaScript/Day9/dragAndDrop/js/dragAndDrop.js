class DragAndDrop {
    constructor() {
        this.draggedItem = null;
        this.dropBoxes = document.querySelectorAll(".drop-box");
        this.init();
    }

    init() {
        this.draggableItem = document.querySelector(".draggable-item");

        this.draggableItem.addEventListener("dragstart", (e) => {
            this.handleDragStart(e);
        });

        this.draggableItem.addEventListener("dragend", (e) => {
            this.handleDragEnd(e);
        });

        this.dropBoxes.forEach((box) => {
            box.addEventListener("dragover", (e) => this.handleDragOver(e));
            box.addEventListener("drop", (e) => {
                this.handleDrop(e, box);
            });

            box.addEventListener("dragenter", () => {
                box.classList.add("drop-box--drag-over");
            });

            box.addEventListener("dragleave", () => {
                box.classList.remove("drop-box--drag-over");
            });
        });
    }

    handleDragStart(e) {
        this.draggedItem = e.target;
        this.draggedItem.classList.add("draggable-item--dragging");
    }

    handleDragEnd(e) {
        this.draggedItem.classList.remove("draggable-item--dragging");
        this.draggedItem = null;
    }

    handleDragOver(e) {
        e.preventDefault(); // Needed for drop to work
    }

    handleDrop(e, dropBox) {
        e.preventDefault();
        if (!this.draggedItem) return;

        const previousBox = this.draggedItem.closest(".drop-box");

        //Instead of innerHTML = '', remove only placeholder
        const placeholder = dropBox.querySelector(".drop-box__placeholder");
        if (placeholder) placeholder.remove();

        // Create content container if needed
        let content = dropBox.querySelector(".drop-box__content");
        if (!content) {
            content = document.createElement("div");
            content.classList.add("drop-box__content");
            dropBox.appendChild(content);
        }

        // Append dragged item into a structured content container
        content.appendChild(this.draggedItem);

        // Styling and visual cleanup
        dropBox.classList.remove("drop-box--drag-over");
        dropBox.classList.add("drop-box--has-content");
        this.draggedItem.style.opacity = "1";
        this.draggedItem.style.transform = "rotate(0deg)";

        // Restore placeholder to previousBox without removing all innerHTML
        if (previousBox && previousBox !== dropBox) {
            previousBox.classList.remove("drop-box--has-content");

            //Clean previous content container only
            const oldContent = previousBox.querySelector(".drop-box__content");
            if (oldContent) oldContent.remove();

            // Restore placeholder safely
            const placeholderDiv = document.createElement("div");
            placeholderDiv.classList.add("drop-box__placeholder");
            placeholderDiv.textContent = "Drop items here";
            previousBox.appendChild(placeholderDiv);
        }
    }
}

document.addEventListener("DOMContentLoaded", () => {
    new DragAndDrop();
});
