def get_points_and_fold_coords(input_str: str):
    point_lines = input_str.split("\n\n")[0].split("\n")
    fold_lines = input_str.split("\n\n")[1].split("\n")

    return (
        [(int(x), int(y)) for x,y in (point.split(",") for point in point_lines)],
        [(name, int(xy)) for name,xy in (fold_line[fold_line.find("=") - 1:].split("=") for fold_line in fold_lines)]
        )

with open("input.in") as file:
    points, folds = get_points_and_fold_coords(file.read())

new_points = []

for fold in folds:
    for point in points:
        if fold[0] == "x":
            if point[0] > fold[1]:
                new_points.append((fold[1] - (point[0] - fold[1]), point[1]))
            else:
                new_points.append(point)
        elif fold[0] == "y":
            if point[1] > fold[1]:
                new_points.append((point[0], fold[1] - (point[1] - fold[1])))
            else:
                new_points.append(point)
    points = set(new_points)
            
new_points = set(new_points)

side_len = max([n for point in new_points for n in point])

paper = [["." for x in range(side_len)] for y in range(side_len)]

for y in range(side_len):
    for x in range(side_len):
        if (x, y) in new_points:
            paper[y][x] = "#"

with open("output.txt", "w") as file:
    for row in paper:
        file.write("".join(row) + "\n")