class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
            from collections import deque 
            stud = deque(students)
            sand = deque(sandwiches)

            cnt = 0 
            left = 0
            while left < len(stud): 

                if stud[left] == sand[0]:
                    stud.popleft()
                    sand.popleft()

                elif sand[0] not in stud:
                    return len(stud)


                else: 
                    stud.append( stud.popleft())

            return 0 