from colorama import Fore, init
from sys import stdout
#pantoum is 4-tuple of stanzas
#stanza is list of 4 lines
#line is a string

#process to initiate:
#enter first stanza (one line at a time) (abab "rhyme")
#after each line is entered, offer to copy to location B
#map:
#stanza[0][0] -> stanza[3][3] or stanza[3][1]
#stanza[0][1] -> stanza[1][0]
#stanza[0][2] -> stanza[3][1] or stanza[3][3]
#stanza[0][3] -> stanza[1][2]

#stanza[1][1] -> stanza[2][0]
#stanza[1][3] -> stanza[2][2]

#stanza[2][1] -> stanza[3][0]
#stanza[2][3] -> stanza[3][2]

#Keep original 8 lines in separate store of originalLines (list of 8 lines)
#when you edit any of original 8 lines, offer to copy to destination

#first constructor builds empty pantoum

class pantoum:
    '''This is a program to assist composing in the pantoum form. 8 original
       lines fill out a 16-line structure.  Individual repetitions can be
       adjusted.'''

    def __init__(self, first_line_last=True):
        '''Create empty Pantoum and initial entry structure'''
        init(autoreset=True)
        self.first_line_last = first_line_last
        stanza = []
        self.title = ""
        self.raw_lines = []
        for ii in range(4):
            stanza.append(4 * [""])
        self.stanza = tuple(stanza)
        for ii in range(8):
            self.raw_lines.append("")
        #build the copy map here, using 0-index and
        #the first_line_last boolean
        LINE_MAP = (((0, 0), (3, 3), 1),
                    ((0, 1), (1, 0), 2),
                    ((0, 2), (3, 1), 1),
                    ((0, 3), (1, 2), 2),
                    ((1, 1), (2, 0), 3),
                    ((1, 3), (2, 2), 3),
                    ((2, 1), (3, 0), 4),
                    ((2, 3), (3, 2), 4))
        LINE_MAP_REVERSED = (((0, 0), (3, 1), 1),
                             ((0, 1), (1, 0), 2),
                             ((0, 2), (3, 3), 1),
                             ((0, 3), (1, 2), 2),
                             ((1, 1), (2, 0), 3),
                             ((1, 3), (2, 2), 3),
                             ((2, 1), (3, 0), 4),
                             ((2, 3), (3, 2), 4))
        if self.first_line_last:
            self.line_map = LINE_MAP
        else:
            self.line_map = LINE_MAP_REVERSED
        #build color map
        self.color_map = {}
        for element in self.line_map:
            self.color_map[element[0]] = element[2]
            self.color_map[element[1]] = element[2]
        self.color_code = {1:Fore.CYAN,
                           2:Fore.RED,
                           3:Fore.GREEN,
                           4:Fore.MAGENTA}


    def print_col(self, color_num, line, outfile=stdout):
        print(self.color_code[color_num] + line, file=outfile, flush=True)

    def print_pantoum(self, outfile=stdout):
        '''pretty print pantoum in 4 colors (each pair of rhyming lines
           and copies)'''
        for stanza_num in range(4):
            for line_num in range(4):
                self.print_col(self.color_map[(stanza_num, line_num)], self.stanza[stanza_num][line_num], outfile)
                #print(self.color_map[(stanza_num, line_num)], self.stanza[stanza_num][line_num])
            print(file=outfile)
        #print(f"raw_lines = {self.raw_lines}")
        #print(f"stanzas = {self.stanza}")
    
    def line_empty(self, line_to_test):
        try:
            return self.stanza[line_to_test[0] - 1][line_to_test[1] - 1] == ''
        except TypeError:
            print("line number not a tuple of ints")
        try:
            return self.raw_lines[line_to_test - 1] == ''
        except TypeError:
            print("line number also not int")
            raise

    def add_line(self, line_num, line):
        '''Usage: add_line(line_num [1-8], lineText)'''
        #also copies line to stanzas, lines
        try: 
            if self.line_empty(line_num):
                self.raw_lines[line_num - 1] = line
                line_map = self.line_map[line_num - 1]
                self.stanza[line_map[0][0]][line_map[0][1]] = line
                self.stanza[line_map[1][0]][line_map[1][1]] = line
        except:
            print("add_line exception")
            #raise ValueError(f"cannot add_line to line_num: {line_num}")
            raise

    def edit_line(self, coordinate, new_line):
        pass

#edit_line function takes coordinates (stanza, line)
# and inserts new string at that spot
#        '''Usage: add_line( tuple (1, 2), string line) insert line at first stanza, 2nd line'''



