document.addEventListener("DOMContentLoaded", function () {
  function debounce(fn, delay) {
    let timer;
    return function (...args) {
      clearTimeout(timer);
      timer = setTimeout(() => fn.apply(this, args), delay);
    };
  }

  function setupAutoSuggest(inputId, suggestionId, endpoint) {
    const input = document.getElementById(inputId);
    const sugg = document.getElementById(suggestionId);

    input.addEventListener("input", debounce(function () {
      const fullInput = this.value.trim();
      const parts = fullInput.split(",");
      const lastPart = parts[parts.length - 1].trim();  // 👈 comma ke baad wala word

      if (lastPart.length < 1) {
        sugg.innerHTML = "";
        sugg.style.display = "none";
        return;
      }

      fetch(`/suggest/${endpoint}/?q=${encodeURIComponent(lastPart)}`)

        .then(res => res.json())
        .then(data => {
          const items = data.suggestions || [];
          if (items.length === 0) {
            sugg.innerHTML = "";
            sugg.style.display = "none";
            return;
          }
          sugg.innerHTML = items
            .map(item => `<li>${item}</li>`)
            .join("");
          sugg.style.display = "block";
        });
    }, 200));

    sugg.addEventListener("mousedown", function (e) {
      if (e.target.tagName === "LI") {
        const currentVal = input.value;
        const parts = currentVal.split(",");
        parts[parts.length - 1] = e.target.textContent;  // Replace last keyword
        input.value = parts.map(p => p.trim()).join(", ") + ", ";  // Rebuild string
        sugg.innerHTML = "";
        sugg.style.display = "none";

      }
    });
  }

  setupAutoSuggest("job_title", "job_suggestions", "titles");
  setupAutoSuggest("location", "location_suggestions", "locations");
});
