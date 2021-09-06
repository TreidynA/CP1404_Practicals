NAME_TO_CODE = {"aquamarine1": "#7fffd4", "brown4": "#8b2323", "chartreuse3": "#66cd00", "Coral": "#ff7f50",
                "darkgoldenrod": "#b8860b", "darkorchid": "#9932cc", "dodgerblue4": "#104e8b", "floralwhite": "#fffaf0",
                "darlviolet": "#9400d3", "deepslategray": "#2f4f4f"}

print(NAME_TO_CODE)

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    if colour_name in NAME_TO_CODE:
        print(colour_name, "is", NAME_TO_CODE[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()