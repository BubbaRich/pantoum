import pantoum

pt = pantoum.pantoum()
for ii in range(8):
    line = input(f"Please input line#{ii + 1} of 8: ")
    pt.add_line(ii + 1, line)
    pt.print_pantoum()
