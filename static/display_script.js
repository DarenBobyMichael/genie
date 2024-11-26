document.addEventListener("DOMContentLoaded", function () {
    const textarea = document.getElementById("prompt_answer");
    if (textarea) {
        // Function to adjust the height dynamically
        const adjustHeight = () => {
            textarea.style.height = "auto"; // Reset height to auto to shrink if needed
            textarea.style.height = textarea.scrollHeight + "px"; // Adjust to the full content height
        };

        // Adjust height initially
        adjustHeight();

        // Optional: Add listener if content may change dynamically
        textarea.addEventListener("input", adjustHeight);
    }
});
