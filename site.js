document.addEventListener("DOMContentLoaded", function () {
  const cursor = document.getElementById("cursor");
  const bubble = document.getElementById("cursor-inner");

  // follow mouse with transform translate (GPU-accelerated)
  document.addEventListener("mousemove", (e) => {
    cursor.style.transform = `translate(${e.clientX - 12}px, ${
      e.clientY - 12
    }px)`;
  });

  // enlarge when hovering a link or image in a link
  document.addEventListener("mouseover", (e) => {
    if (e.target.closest("a") || e.target.closest(".project")) {
      bubble.style.transform = "scale(1.6)";
    }
  });
  document.addEventListener("mouseout", (e) => {
    const related = e.relatedTarget;
    if (!related || (!related.closest("a") && !related.closest(".project"))) {
      bubble.style.transform = "scale(1)";
    }
  });
});
