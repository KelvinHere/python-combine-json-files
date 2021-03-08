# JSON merge

Created to merge products data in seperate json files where the data has a SKU attached to the data.  This data is then assembled into a valid post request to add the product to a database.

The script opens files, loops through and matches skus, and assembles the data into a valid entry for a database.

This is currently hard coded to its intended application and will need to be modified for different JSON structures / outputs.