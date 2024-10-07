function showGraph() {
    const selector = document.getElementById("graphSelector");
    const graphImage = document.getElementById("graphImage");
    const selectedValue = selector.value;

    if (selectedValue === "total_spend_by_category") {
        graphImage.src = "graphs/static/images/total_spend_by_category.png"; 
        graphImage.alt = "total_spend_by_category";
    } 
    else if (selectedValue === "max_spend_per_cat") {
        graphImage.src = "graphs/static/images/max_spend_per_cat.png"; 
        graphImage.alt = "max_spend_per_cat";
    } 
    else if (selectedValue === "cutomer_segmentation_wrt_purchase") {
        graphImage.src = "graphs/static/images/cutomer_segmentation_wrt_purchase.png"; 
        graphImage.alt = "cutomer_segmentation_wrt_purchase";
    } 
    else if (selectedValue === "discount_percentage_wrt_purchase") {
        graphImage.src = "graphs/static/images/discount_percentage_wrt_purchase.png"; 
        graphImage.alt = "discount_percentage_wrt_purchase";
    } 
    else if (selectedValue === "bp_purchase") {
        graphImage.src = "graphs/static/images/bp_purchase.png"; 
            graphImage.alt = "Graph 5";
    } 
    else if (selectedValue === "tot_max_pc1") {
        graphImage.src = "graphs/static/images/tot_max_pc1.png"; 
            graphImage.alt = "Graph 5";
    } 
    else if (selectedValue === "tot_max_pc2") {
        graphImage.src = "graphs/static/images/tot_max_pc2.png"; 
            graphImage.alt = "Graph 5";
    } 
    else if (selectedValue === "tot_max_pc3") {
        graphImage.src = "graphs/static/images/tot_max_pc3.png"; 
            graphImage.alt = "Graph 5";
    } 
    else if (selectedValue === "heat_corr") {
        graphImage.src = "graphs/static/images/heat_corr.png"; 
            graphImage.alt = "Graph 5";
    }
    else {
            graphImage.src = "graphs/static/images/bar-chart.gif";
            graphImage.alt = "Default image";
    }

    graphImage.style.display = selectedValue ? "block" : "none";
}

function toggleContent(element) {
    const details = element.nextElementSibling; // Get the next sibling (the details <ul>)
    if (details.style.display === "none" || details.style.display === "") {
        details.style.display = "block"; // Show details
        element.textContent = "Read Less"; // Change text
    } else {
        details.style.display = "none"; // Hide details
        element.textContent = "Read More"; // Change text back
    }
}