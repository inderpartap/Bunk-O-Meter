var fs = require("fs");
var node_xj = require("xls-to-json");

node_xj({
    input: "report.xlsx", // input xls 
    output: "output.json", // output json 
    sheet: "Sheet 1" // specific sheetname 
}, function (err, result) {
    if (err) {
        console.error(err);
    } else {
        var unique = [];
        result.forEach(function (element) {
            // remove number from faculty name
            element.FACULTY = element.FACULTY.split(" - ").pop();
            unique.push({
                "CODE": element.CODE,
                "TITLE": element.TITLE
            });
        }, this);

        // overwirte the output file
        fs.writeFile(__dirname + "/../data/all_data.json", JSON.stringify(result));

        // remove repeating courses
        unique = unique.filter((element, index, self) => self.findIndex(t => t.CODE === element.CODE && t.TITLE === element.TITLE) === index);

        fs.writeFile(__dirname + "/../data/unique_courses.json", JSON.stringify(unique));
    }
});