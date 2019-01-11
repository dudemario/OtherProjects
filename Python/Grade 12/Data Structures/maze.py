maze =[
    [
        [
            [],
            []
        ],
        []
    ],
    [
        [],
        [
            [
                [
                    [],
                    []
                ],
                [
                    [],
                    [
                        [
                            [
                                [
                                    [
                                        [
                                            [],
                                            []
                                        ],
                                        []
                                    ],
                                    [
                                        [
                                            [
                                                [],
                                                []
                                            ],
                                            []
                                        ],
                                        ["end"]
                                    ]
                                ],
                                [
                                    [],
                                    []
                                ]
                            ],
                            [
                                [
                                    [],
                                    []
                                ],
                                [
                                    [],
                                    []
                                ]
                            ]
                        ],
                        []
                    ]
                ]
            ],
            []
        ]
    ]
]

from stack import stack as s
def solveMaze(maze):
    global flag
    flag = False
    if len(maze) != 0:
        stack = s()
        for i in xrange(len(maze)):
            if not flag:
                stack.push(i)
                search(maze[i], stack),
        if flag:
            stack.reverse()
            return stack
        else:
            return "No end"


def search(maze, stack):
    global flag
    if not flag:
        if len(maze) == 0:
            stack.pop()
            return 1
        for i in xrange(len(maze)):
            if not flag:
                if maze[i]== "end":
                    flag = True
                    return 2
                stack.push(i)
                search(maze[i], stack), 
        if not flag:
            stack.pop()
        return 0

path = solveMaze(maze)
print "Path: " + path.printStack()
p = maze
for i in xrange(path.length):
    p = p[path.pop().value]
print p[0]
