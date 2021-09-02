import pandas as pd


def main():
    table = pd.DataFrame({"col1": "constant", "col2": range(20), "col3": "is really long, I think"})
    table[((table["col1"] == "constant") & (table["col2"] > 3) & (table["col2"] < 12)) | table["col3"].notnull()]
    table["col4"] = (table["col2"]
                + im_ugly_but_cant_be_formatted * 4)

if __name__ == '__main__':
    main()
