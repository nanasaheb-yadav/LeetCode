import os


output = """
    <ul class="tree">
    {}
    </ul>
"""

with open("Drive.txt", 'w', encoding="utf-8") as file:
    path = "D:\Python\GIT Projects\\"
    ls = []
    for dirpath, dirnames, filenames in os.walk(path):
        directory_level = dirpath.replace(path, "")
        directory_level = directory_level.count(os.sep)
        indent = " " * 4

        str = """<li><a href="#">{}{}/</li>""".format(indent*directory_level, os.path.basename(dirpath))
        print(str)
        print("{}{}/".format(indent*directory_level, os.path.basename(dirpath)))
        #file.write("{}{}/".format(indent*directory_level, os.path.basename(dirpath)))
        for f in filenames:
            pass
            #file.write("{}{}".format(indent*(directory_level+1), f))
            print("{}{}".format(indent*(directory_level+1), f))
#print(output)