# Convert Excel sheet to JSON

## Usage

    npm install

`index.js` has the necessary script to convert excel to JSON.

    node index.js

*`data/all_data.json` and `data/all_data.json` will be modified as per the new excel*

### Note

- Make sure excel file name is `report.xlsx`

- The sheet name in the file MUST be `Sheet 1`

- Excel sheet should ONLY have the following columns headers (case sensitive):

    **CODE**

    **VENUE**

    **FACULTY**

    **CREDITS**

    **SLOT**

- The scipt may need to be modified depending upon the data in `report`.