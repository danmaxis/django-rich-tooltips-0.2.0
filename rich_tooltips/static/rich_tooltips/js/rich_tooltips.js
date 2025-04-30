// Rich Tooltips Plugin JavaScript

document.addEventListener("DOMContentLoaded", function() {
    console.log("Rich Tooltips JS loaded and initializing.");

    let tooltipElement = null;
    let tooltipTimerElement = null; // Added for the timer
    let tooltipTimeout = null;
    let hideTimeout = null; // Timeout for hiding after leaving element/tooltip
    let isTooltipFixed = false;
    let currentTargetElement = null;
    const HOVER_DELAY_MS = 1000; // Configurable: 1 second delay to fix
    const HIDE_DELAY_MS = 200; // Short delay before hiding after mouseleave

    // --- Tooltip Container Management ---
    function getTooltipElement() {
        if (!tooltipElement) {
            tooltipElement = document.createElement("div");
            tooltipElement.className = "rich-tooltip-container";
            tooltipElement.style.display = "none"; // Start hidden
            tooltipElement.style.pointerEvents = "none"; // Initially non-interactive
            tooltipElement.style.position = "fixed"; // <--- Added/Changed this line
            tooltipElement.style.zIndex = 1000; // Make sure it's above other content

            // Create and append the timer element
            tooltipTimerElement = document.createElement("div");
            tooltipTimerElement.className = "rich-tooltip-timer";
            tooltipElement.appendChild(tooltipTimerElement);

            document.body.appendChild(tooltipElement);

            // Event listeners for the tooltip container itself
            tooltipElement.addEventListener("mouseenter", () => {
                if (isTooltipFixed) {
                    console.log("Mouse entered fixed tooltip.");
                    clearTimeout(hideTimeout);
                }
            });

            tooltipElement.addEventListener("mouseleave", () => {
                if (isTooltipFixed) {
                    console.log("Mouse left fixed tooltip.");
                    scheduleHideTooltip();
                }
            });
        }
        return tooltipElement;
    }

    // --- Tooltip Display Logic ---
    function showTooltip(event, content, targetElement) {
        const tooltip = getTooltipElement();
        currentTargetElement = targetElement;

        // Set content *before* timer to avoid layout shifts affecting timer position
        // Temporarily hide timer while setting content
        tooltipTimerElement.style.display = "none";
        tooltip.innerHTML = content; // Supports HTML content directly
        tooltip.appendChild(tooltipTimerElement); // Re-append timer after innerHTML overwrite

        tooltip.style.display = "block";
        tooltip.classList.remove("fixed");
        tooltip.classList.add("fixing"); // Show timer
        tooltipTimerElement.style.display = "block"; // Make timer visible
        tooltip.style.pointerEvents = "none";
        isTooltipFixed = false;

        updateTooltipPosition(event);

        clearTimeout(tooltipTimeout);
        clearTimeout(hideTimeout);

        tooltipTimeout = setTimeout(() => {
            if (tooltip.style.display === "block") {
                tooltip.classList.remove("fixing"); // Hide timer
                tooltipTimerElement.style.display = "none";
                tooltip.classList.add("fixed");
                tooltip.style.pointerEvents = "auto";
                isTooltipFixed = true;
                console.log("Tooltip fixed.");
                initializeTooltips(tooltip);
            }
        }, HOVER_DELAY_MS);
    }

    function scheduleHideTooltip() {
        clearTimeout(tooltipTimeout);
        clearTimeout(hideTimeout);
        // Also remove fixing class if hiding before fixed
        const tooltip = getTooltipElement();
        if (tooltip && !isTooltipFixed) {
             tooltip.classList.remove("fixing");
             tooltipTimerElement.style.display = "none";
        }
        hideTimeout = setTimeout(() => {
            hideTooltip();
        }, HIDE_DELAY_MS);
    }

    function hideTooltip() {
        clearTimeout(tooltipTimeout);
        clearTimeout(hideTimeout);
        const tooltip = getTooltipElement();
        if (tooltip) {
            tooltip.style.display = "none";
            tooltip.classList.remove("fixed");
            tooltip.classList.remove("fixing"); // Ensure fixing class is removed
            tooltipTimerElement.style.display = "none";
            tooltip.style.pointerEvents = "none";

            // Reset top and left styles on hide
            tooltip.style.top = "";
            tooltip.style.left = "";

            // Clear only non-timer children
            Array.from(tooltip.childNodes).forEach(node => {
                if (node !== tooltipTimerElement) {
                    tooltip.removeChild(node);
                }
            });
        }
        isTooltipFixed = false;
        currentTargetElement = null;
        console.log("Tooltip hidden.");
    }

    // --- Tooltip Positioning ---
    function updateTooltipPosition(event) {
        const tooltip = getTooltipElement();
        if (!tooltip || tooltip.style.display === "none" || isTooltipFixed) {
            return;
        }
    
        // Use clientX and clientY for fixed positioning relative to the viewport
        let x = event.clientX + 15; // Add a small offset to the right of the cursor
        let y = event.clientY + 15; // Add a small offset below the cursor
    
        const tooltipRect = tooltip.getBoundingClientRect();
        const viewportWidth = window.innerWidth;
        const viewportHeight = window.innerHeight;
    
        // Adjust if the tooltip goes beyond the right edge of the viewport
        if (x + tooltipRect.width > viewportWidth) {
            x = event.clientX - tooltipRect.width - 15; // Position to the left of the cursor
        }
    
        // Adjust if the tooltip goes beyond the bottom edge of the viewport
        if (y + tooltipRect.height > viewportHeight) {
            y = event.clientY - tooltipRect.height - 15; // Position above the cursor
        }
    
        // Ensure the tooltip doesn't go off the left edge of the viewport
        if (x < 0) {
            x = 15; // Position from the left edge with offset
        }
    
        // Ensure the tooltip doesn't go off the top edge of the viewport
        if (y < 0) {
             y = 15; // Position from the top edge with offset
        }

        // console.log("Event type:", event.type);
        // console.log("event.clientY:", event.clientY);
        // console.log("event.pageY:", event.pageY);
        // console.log("window.scrollY:", window.scrollY);
        // console.log("Calculated y:", y);
        // console.log("Tooltip element:", tooltip);
    
        // Set position using calculated viewport coordinates
        tooltip.style.left = `${x}px`;
        tooltip.style.top = `${y}px`;
    }

    // --- Event Handling and Initialization ---
    function initializeTooltips(parentElement = document.body) {
        const targetElements = parentElement.querySelectorAll("[data-tooltip-html]:not(.rich-tooltip-processed), [data-tooltip-markdown]:not(.rich-tooltip-processed)");

        console.log(`Initializing ${targetElements.length} tooltip triggers in`, parentElement);

        targetElements.forEach(element => {
            element.classList.add("rich-tooltip-processed");

            element.addEventListener("mouseenter", (event) => {
                const tooltip = getTooltipElement();
                if (isTooltipFixed && !tooltip.contains(element)) {
                    return;
                }

                let content = element.getAttribute("data-tooltip-html");
                const markdownContent = element.getAttribute("data-tooltip-markdown");

                if (!content && markdownContent) {
                    if (typeof marked !== "undefined") {
                         try {
                            // Ensure marked.parse returns a string
                            let parsedContent = marked.parse(markdownContent);
                            content = typeof parsedContent === "string" ? parsedContent : "Error: Parsed content is not a string.";
                         } catch (e) {
                            console.error("Error parsing Markdown:", e);
                            content = "Error parsing Markdown.";
                         }
                    } else {
                        content = `<i>Markdown library not loaded.</i><pre>${markdownContent}</pre>`;
                    }
                }

                if (content) {
                    showTooltip(event, content, element);
                }
            });

            element.addEventListener("mousemove", (event) => {
                if (!isTooltipFixed) {
                    updateTooltipPosition(event);
                }
            });

            element.addEventListener("mouseleave", () => {
                scheduleHideTooltip();
            });
        });
    }

    // Global click listener to hide fixed tooltips when clicking outside
    document.addEventListener("click", (event) => {
        const tooltip = getTooltipElement();
        if (isTooltipFixed && tooltip && !tooltip.contains(event.target) && event.target !== currentTargetElement && !currentTargetElement?.contains(event.target)) {
             console.log("Clicked outside fixed tooltip or its trigger.");
             hideTooltip();
        }
    });

    // Initial setup on page load
    getTooltipElement();
    initializeTooltips();

});
