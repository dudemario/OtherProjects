maze =[1,
    [1,
        [3,
            [3],
            [11]
        ],
        [7]
    ],
    [8,
        [2],
        [1,
            [11,
                [9,
                    [3,
                        [3],
                        [4]
                    ],
                    [10,
                        [5],
                        [1,
                            [1,
                                [3,
                                    [4,
                                        [1,
                                            [3,
                                                [1],
                                                [4]
                                            ],
                                            [1]
                                        ],
                                        [1,
                                            [4,
                                                [5
                                                    [5],
                                                    [7]
                                                ],
                                                [3]
                                            ],
                                            ["end"]
                                        ]
                                    ],
                                    [3
                                        [1],
                                        [4]
                                    ]
                                ],
                                [2
                                    [6
                                        [10],
                                        [4]
                                    ],
                                    [6
                                        [4],
                                        [1]
                                    ]
                                ]
                            ],
                            [1]
                        ]
                    ]
                ], 
                [5
                    [6
                        [6
                            [4],
                            [1]
                        ],
                        [2
                            [1
                                [1],
                                [1
                                    [10
                                        [8],
                                        [3
                                            [3],
                                            [4]
                                        ]
                                    ],
                                    [5]
                                ]
                            ],
                            [3
                                [4, 
                                    [1,
                                        [3,
                                            [1],
                                            [4]
                                        ],
                                        [1]
                                    ],
                                    [1
                                        [4,
                                            [5,
                                                [5],
                                                [7]
                                            ],
                                            [3]
                                        ],
                                        [0, "end"]
                                    ]
                                ],
                                [3
                                    [1],
                                    [4]
                                ]
                            ]
                        ]
                    ],
                    [10]
                ]
            ],
            [1]
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
                stack.push(i, length)
                search(maze[i], stack),
        if flag:
            stack.reverse()
            return stack
        else:
            return "No end"


def search(maze, stack):
    global flag
    if not flag:
        if len(maze) == 1:
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

'''
'''

