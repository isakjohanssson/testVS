class Route:


    def __init__(self, position, possible_next_positons=None):
        self.position = position
        self.possible_next_positions = possible_next_positons

    def set_next_positions(self, possible_next_positions):
        self.possible_next_positions = possible_next_positions
        return
    
    def pop(self):
        self.possible_next_positions.pop(0)
        return


class ChessBoard:


    def __init__(self, start=(0,0)):
        self.routes = [(x,y) for x in range(8) for y in range(8)]
        self.steps = [
                        [-2,-1],
                        [-2,1],
                        [-1,-2],
                        [-1,2],
                        [1,-2],
                        [1,2],
                        [2,-1],
                        [2,1]
                        ]
        self.visited = [Route(start)]
        #korta ned nästa rad avsevärt, gärna kombinera med raden ovan.
        self.visited[-1].set_next_positions(self.get_ordered_next_positions(self.get_next_positions(start), self.get_number_of_possible_next_next_positions(self.get_next_positions(start))))
    
    def get_available_positions(self):
        return [route for route in self.routes if route not in [route.position for route in self.visited]]

    def get_next_positions(self, from_position=(0,0)):
        return [next_position for step in self.steps if (next_position:= (from_position[0]+step[0], from_position[1]+step[1])) in self.get_available_positions()]
    
    def get_number_of_possible_next_next_positions(self, next_positons):
        return [len(self.get_next_positions(steps_from_next_position)) for steps_from_next_position in next_positons]

    def get_ordered_next_positions(self, next_route_positions, number_of_possible_next_next_positions):
            #slå ihop med get_next_positions och strukturera om. Vore snyggare
            dummy_list = [[elem[0] for elem in next_route_positions],[elem[1] for elem in next_route_positions], number_of_possible_next_next_positions]
            dummy_list = [(next_route_positions[i][0], next_route_positions[i][1], number_of_possible_next_next_positions[i]) for i in range(len(number_of_possible_next_next_positions))]
            dummy_list.sort(key = lambda x:x[2])
            #dummy_list = [(elem[0], elem[1]) for elem in dummy_list]
            return [(elem[0], elem[1]) for elem in dummy_list]

    def do_next_step(self):
        #korta ned och flytta till fill_board
        if (route_position:= route[0] if (route:=self.visited[-1].possible_next_positions) else False):
            self.visited.append(Route(route_position))

            next_route_positions = self.get_next_positions(route_position)
            number_of_next_next_positions = self.get_number_of_possible_next_next_positions(next_route_positions)
            ordered_next_positions = self.get_ordered_next_positions(next_route_positions, number_of_next_next_positions)
            
            self.visited[-1].set_next_positions(ordered_next_positions)
            #Do further debugs here
            print('--------')
            print(self.visited[-1].position)
            print(self.visited[-1].possible_next_positions)
            print('Dessa rutor har besökts ', [elem.position for elem in self.visited])
            print('Dessa rutor är tillgängliga', self.get_available_positions())
            print('--------')
            #take a step back
        #borde inte ingå i denna funktion
        elif len(self.visited)<64:
            self.take_step_back()
        return

    def take_step_back(self):
        print('Not yet done')
        self.visited.pop()
        self.visited[-1].pop()
        return

    def fill_board(self):
        for i in range(1000):
            self.do_next_step()
        return



my_board = ChessBoard(start=(1,7))

my_board.fill_board()
print(len(my_board.visited))
