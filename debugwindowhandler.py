from cmath import rect
import json
from tracemalloc import start
from graphics import GraphWin, Point, Rectangle, Text
import os

##CONSTS
cluster_resolution = 44

class Cluster():
    def __init__(self, anchor : Point, end : Point, display_number : int):
        self.anchor = anchor
        self.end = end
        self.display_number = display_number

    def out(self):
        return "(" + str(self.anchor.x) + "|" + str(self.anchor.y) + ")-(" + str(self.end.x) + "|" + str(self.end.y) + ")"

    def give_widget(self, obj):
        self.widget = obj


class DISPLAY():
    def __init__(self):
        with open(str(os.path.dirname(os.path.abspath(__file__))) + r"/displayarrangement.json", "r") as jfile:
            self.matrix = json.loads(jfile.read())["clusters"]
            height = len(self.matrix)
            width = 0
            for row in self.matrix:
                if len(row) > width:
                    width = len(row)
            print(str(height * cluster_resolution) + "x" + str(width * cluster_resolution))
        self.wallpaper = GraphWin("WallPaper", width=width * cluster_resolution, height=height * cluster_resolution)
        displaycount = 0
        self.clusters = []
        for i in range(height):
            self.clusters.append([None for i in range(width)])
        for row in range(len(self.matrix)):
            for element in range(len(self.matrix[row])):
                display_id = self.matrix[row][element]
                if display_id > displaycount:
                    displaycount = display_id
                if self.matrix[row][element] == -1:
                    pointAnchor = Point(x = element * cluster_resolution, y = row * cluster_resolution)
                    pointStretcher = Point(x = (element + 1) * cluster_resolution, y = (row + 1) * cluster_resolution)
                    self.clusters[row][element] = Cluster(anchor = pointAnchor, end = pointStretcher, display_number=self.matrix[row][element])
                    obj = Rectangle(p1 = pointAnchor, p2 = pointStretcher)
                    obj.setFill("black")
                    obj.draw(self.wallpaper)
                else:
                    pointAnchor = Point(x = element * cluster_resolution, y = row * cluster_resolution)
                    pointStretcher = Point(x = (element + 1) * cluster_resolution, y = (row + 1) * cluster_resolution)
                    obj = Rectangle(p1 = pointAnchor, p2 = pointStretcher)
                    obj.draw(self.wallpaper)
                    self.clusters[row][element] = Cluster(anchor = pointAnchor, end = pointStretcher, display_number=self.matrix[row][element])
                    txt = Text(p = Point((pointAnchor.x + pointStretcher.x) / 2, (pointAnchor.y + pointStretcher.y) / 2) , text = "(" + str(row) + "|" + str(element) + ")")
                    txt.draw(self.wallpaper)
        with open(str(os.path.dirname(os.path.abspath(__file__))) + r"/displayarrangement.json", "r") as jfile:
            for display_coordinates in json.loads(jfile.read())["displays"]:
                coordinate_one = display_coordinates[0]
                coordinate_two = display_coordinates[1]
                startingPoint = Point(x = coordinate_one[0] * cluster_resolution, y = coordinate_one[1] * cluster_resolution)
                endpoint = Point(x = (coordinate_two[0] + 1) * cluster_resolution, y = (coordinate_two[1] + 1) * cluster_resolution)
                rect = Rectangle(p1 = startingPoint, p2=endpoint)
                rect.setOutline("red")
                rect.draw(self.wallpaper)

        for row in range(len(self.clusters)):
            for element in range(len(self.clusters[row])):
                rect = Rectangle(p1 = self.clusters[row][element].anchor, p2 = self.clusters[row][element].end)
                rect.setFill("blue")
                rect.draw(self.wallpaper)

    def load_layout(self, name:str):
        with open(str(os.path.dirname(os.path.abspath(__file__))) + r"/layouts.json", "r") as jfile:
            layout = json.loads(jfile.read())[name]
            for widget in layout["widget-cluster-map"].keys():
                coords = layout["widget-cluster-map"][widget]
                rects_owned = int(len(coords) / 2)
                print(widget + " " + str(rects_owned))
                if rects_owned == 1:
                    start_cluster : Cluster = self.clusters[coords[0][0]][coords[0][1]]
                    print(start_cluster.out())
                    print(coords[1][0])
                    print(coords[1][1])
                    end_cluster : Cluster = self.clusters[coords[1][0]][coords[1][1]]
                    print(end_cluster.out())
                    bounds = Rectangle(p1 = start_cluster.anchor, p2 = end_cluster.end)
                    bounds.setFill("blue")
                    bounds.draw(self.wallpaper)
                    

                

        
