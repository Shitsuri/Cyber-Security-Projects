// Global variable to store the last scraped data for comparison
let lastScrapedData = [];

/**
 * Scrapes table data from the page and downloads it as CSV
 * This example targets a fictional bug tracker table with columns:
 * - ID (example-bug-id)
 * - Report Date (example-report-date)
 * - Reported By (example-reported-by)
 */
function scrapeTableData() {
    // Example: Select all cells in the ID column (adjust selectors for real use)
    let idElements = document.querySelectorAll('td.example-bug-id');
    // Example: Select all cells in the date column
    let dateElements = document.querySelectorAll('td.example-report-date');
    // Example: Select all reporter names (within specific cells)
    let reporterElements = document.querySelectorAll('td.example-reported-by .user-name');
    
    let data = [];
    
    // Verify we have matching numbers of elements in each column
    if (idElements.length === dateElements.length && 
        dateElements.length === reporterElements.length) {
        
        // Extract data from each row
        for (let i = 0; i < idElements.length; i++) {
            let bugId = idElements[i].textContent.trim();      // Get and clean bug ID
            let reportDate = dateElements[i].textContent.trim(); // Get and clean date
            let reporter = reporterElements[i].textContent.trim(); // Get and clean reporter

            // Add extracted data to our collection
            data.push({ bugId, reportDate, reporter });
        }

        // Convert the data to CSV format
        const csvData = convertToCSV(data);

        // Trigger download of the CSV file
        downloadCSV(csvData);
    } else {
        console.warn('Column counts do not match - data may be incomplete');
    }
}

/**
 * Converts an array of objects to CSV format
 * @param {Array} data - Array of objects containing table data
 * @returns {string} CSV formatted string
 */
function convertToCSV(data) {
    // Example CSV headers (modify according to your data structure)
    let csv = 'BugID,ReportDate,Reporter\n';  

    // Add each data row to the CSV
    data.forEach(item => {
        // Quote each field to handle potential commas in the data
        csv += `"${item.bugId}","${item.reportDate}","${item.reporter}"\n`;
    });

    return csv;
}

/**
 * Creates and triggers a download of the CSV file
 * @param {string} csvData - The CSV content to download
 * @param {string} [filename='example_data.csv'] - Optional filename
 */
function downloadCSV(csvData, filename = 'example_data.csv') {
    // Create a blob (file-like object) from the CSV data
    const blob = new Blob([csvData], { type: 'text/csv' });
    
    // Create a temporary anchor element to trigger download
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = filename;  // Use provided filename
    
    // Programmatically click the link to trigger download
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    
    // Clean up by revoking the object URL
    setTimeout(() => URL.revokeObjectURL(link.href), 100);
}

/**
 * Checks for new or updated data in the table periodically
 * Downloads new data if changes are detected
 * This example checks every 10 seconds (adjust as needed)
 */
function checkForNewData() {
    // Select the same elements as in scrapeTableData()
    let idElements = document.querySelectorAll('td.example-bug-id');
    let dateElements = document.querySelectorAll('td.example-report-date');
    let reporterElements = document.querySelectorAll('td.example-reported-by .user-name');
    
    let currentData = [];

    // Verify column counts match before processing
    if (idElements.length === dateElements.length && 
        dateElements.length === reporterElements.length) {
        
        // Extract current data from the table
        for (let i = 0; i < idElements.length; i++) {
            let bugId = idElements[i].textContent.trim();
            let reportDate = dateElements[i].textContent.trim();
            let reporter = reporterElements[i].textContent.trim();

            currentData.push({ bugId, reportDate, reporter });
        }

        // Compare with last scraped data
        if (JSON.stringify(currentData) !== JSON.stringify(lastScrapedData) && 
            currentData.length > 0) {
            
            console.log('New data detected - updating...');
            
            // Update last scraped data with current snapshot
            lastScrapedData = [...currentData]; 
            
            // Convert and download the new data
            const csvData = convertToCSV(currentData);
            downloadCSV(csvData, 'updated_example_data.csv');
        }
    }
}

// Example usage options:

// 1. Run once immediately
// scrapeTableData();

// 2. Set up periodic checking (example: every 10 seconds)
const scrapeInterval = setInterval(checkForNewData, 10000);

// To stop the interval when needed:
// clearInterval(scrapeInterval);