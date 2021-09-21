import pprint
from collections import defaultdict

#   LINK: https://en.wikipedia.org/wiki/Connected-component_labeling

def regions_EightConnected_TwoPass(values):
    """Blob detection using eight-connected-ness for a 2d list of 0/1 values"""
    linked = defaultdict(set)

    #   labels[row][col] = region number
    labels = [ [ 0 for col in range(len(values[0])) ] for row in range(len(values)) ]

    print("values:")
    pprint.pprint(values)

    #   First pass, assign labels to non-zero regions using the minimum surrounding label, storing which regions are linked
    region_label = 1
    for row in range(len(values)):
        for col in range(len(values[0])):

            #   skip background element
            if values[row][col] == 0:
                continue

            #   get labels of surrounding elements
            surrounding_labels = []
            for delta_row in range(-1,2):
                for delta_col in range(-1,2):
                    if delta_row == 0 and delta_col == 0:
                        continue
                    if row+delta_row < 0 or row+delta_row >= len(values):
                        continue
                    if col+delta_col < 0 or col+delta_col >= len(values[0]):
                        continue
                    if labels[row+delta_row][col+delta_col] != 0:
                        surrounding_labels.append(labels[row+delta_row][col+delta_col])

            if len(surrounding_labels) == 0:
                #   assign a new label
                labels[row][col] = region_label
                #   region is by definition adjacent to itself
                linked[region_label].add(region_label)
                region_label += 1
            else:
                #   assign smallest label found
                trial = min(surrounding_labels)
                if trial != 0:
                    labels[row][col] = trial

                #   add adjacent regions for current label
                for label in surrounding_labels:
                    for x in surrounding_labels:
                        linked[label].add(x) 

    print("linked:")
    pprint.pprint(linked)

    #   Second pass, consolidate labels, replace each label with the minimum label with which it is linked
    for row in range(len(values)):
        for col in range(len(values[0])):
            if values[row][col] != 0:
                labels[row][col] = min(linked[labels[row][col]])


    print("labels:")
    pprint.pprint(labels)

    #   regions[label] = coordinates of elements of each region
    regions = defaultdict(list)
    for row in range(len(values)):
        for col in range(len(values[0])):
            if values[row][col] == 0:
                continue
            regions[labels[row][col]].append( (row, col) )

    print("regions:")
    pprint.pprint(regions)

    regions_size = { k: len(v) for k, v in regions.items() }
    print("regions_size:")
    pprint.pprint(regions_size)




values = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0],]
regions_EightConnected_TwoPass(values)


