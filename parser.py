from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    file = open(fname,"r")
    cmds = file.readlines()
    i = 0
    while (i < len(cmds)):
        if (cmds[i] == "line\n"):
            cmds[i+1] = cmds[i+1].replace("\n", "")
            #print(cmds[i+1])
            args = cmds[i+1].split()
            add_edge( points, int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]))
            i+=2
        if (cmds[i] == "ident\n"):
            ident(transform)
            i+=1
        if (cmds[i] == "scale\n"):
            cmds[i+1] = cmds[i+1].replace("\n", "")
            args = cmds[i+1].split()
            m = make_scale(int(args[0]),int(args[1]),int(args[2]))
            matrix_mult(m,transform)
            i+=2
        if (cmds[i] == "move\n"):
            cmds[i+1] = cmds[i+1].replace("\n", "")
            args = cmds[i+1].split()
            m = make_translate(int(args[0]),int(args[1]),int(args[2]))
            matrix_mult(m,transform)
            i+=2
        if (cmds[i] == "rotate\n"):
            cmds[i+1] = cmds[i+1].replace("\n", "")
            args = cmds[i+1].split()
            if (args[0] == "x"):
                m = make_rotX(int(args[1]))
            if (args[0] == "y"):
                m = make_rotY(int(args[1]))
            if (args[0] == "z"):
                m = make_rotZ(int(args[1]))
            matrix_mult(m,transform)
            i+=2
        if (cmds[i] == "apply\n"):
            matrix_mult(transform,points)
            i+=1
        if (cmds[i] == "display\n"):
            clear_screen(screen)
            draw_lines( points, screen, color )
            i+=1
            display(screen)
        if (cmds[i] == "save\n"):
            cmds[i+1] = cmds[i+1].replace("\n", "")
            clear_screen(screen)
            draw_lines( points, screen, color )
            args = cmds[i+1].split()
            save_extension(screen,args[0])
            i+=2
        if (cmds[i] == "quit\n"):
            return
        '''print_matrix(points)
        print(len(cmds))
        print(i)'''
    pass
