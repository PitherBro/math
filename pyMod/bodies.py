class HtmlTable:
    def __init__(self, data=[{
"number": 0,
"#steps": 0,
"list": []
},
]):
        self.data = data
        self.rows = len(data)-1
        self.cols = len(data[0]) if data else 0

    def generate_html(self):
        html = "<table>"
        for row in range(self.rows):
            html += "<tr>"
            for col in range(self.cols):
                obj = dict(self.data[row])
                objKeys = obj.keys()
                currentKey = obj[objKeys[col]]

                print(col)
                html += f"<td id='{row},{col}'>{obj[currentKey]}</td>"
            html += "</tr>"
        html += "</table>"
        return html

    def add_row(self, row_data, index=None):
        if index is None:
            self.data.append(row_data)
        else:
            self.data.insert(index, row_data)
        self.rows += 1

    def add_column(self, col_data, index=None):
        for i in range(len(col_data)):
            if index is None:
                self.data[i].append(col_data[i])
            else:
                self.data[i].insert(index, col_data[i])
        self.cols += 1

# Example usage
data = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [9, 10, 11],
]

table = HtmlTable()

# Add a row with index 2
#table.add_row([12, 13, 14], index=2)

# Add a column with index 2
#table.add_column([2, 5, 8, 11], index=2)

# Generate HTML for the updated table
html_table = table.generate_html()
print(html_table) # or write to a file, or render on a webpage
