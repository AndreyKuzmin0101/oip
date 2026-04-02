document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.getElementById("modeToggle");
    const modeInput = document.getElementById("modeInput");
    const modeLabel = document.getElementById("modeLabel");

    function updateMode() {
        const mode = toggle.checked ? "lemmas" : "tokens";
        modeInput.value = mode;
        modeLabel.textContent = mode;
    }

    updateMode();

    toggle.addEventListener("change", updateMode);
});