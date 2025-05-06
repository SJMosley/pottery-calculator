import cmd
from pottery_calc_helper import inner_inch_dimensions_to_all_values, quick_test, long_test, output

class PotteryCLI(cmd.Cmd):
    prompt = "🏺>>"
    intro = "Welcome to the clay chart for anything!"

    # def do_hello(self, line):
    #     """Print a greeting."""
    #     print("Hello, World!")

    def do_quit(self, line):
        """Exit the CLI."""
        return True

    def do_slipcast_mold(self, line):
        """Usage: desired <width> <height> [shrinkage=0.12] [wall_thickness=0.25]"""
        try:
            args = line.split()
            if len(args) < 2:
                print("Error: You must provide at least width and height.")
                return

            diameter = float(args[0])
            height = float(args[1])
            shrinkage = 0.12
            wall_thickness = .25

            for arg in args[2:]:
                if arg.startswith("shrinkage="):
                    shrinkage = float(arg.split("=")[1])
                elif arg.startswith("wall_thickness="):
                    wall_thickness = float(arg.split("=")[1])

            values = inner_inch_dimensions_to_all_values(shrinkage, diameter, height, wall_thickness)
            applied_twice = inner_inch_dimensions_to_all_values(values["shrinkage"], values["t_i_diameter"], values["t_i_height"], values["wall_thickness"])
            output(applied_twice)
            # print(f"width: {diameter}")
            # print(f"height: {height}")
            # print(f"wall_thickness: {wall_thickness}")
            # print(f"shrinkage: {shrinkage}")
        except (IndexError, ValueError) as e:
            print("Error parsing arguments. Usage: desired <width> <height> [shrinkage=0.12] [wall_thickness=0.25]")
            print(f"Details: {e}")

    def do_desired(self, line):
        """Usage: desired <width> <height> [shrinkage=0.12] [wall_thickness=0.25]"""
        try:
            args = line.split()
            if len(args) < 2:
                print("Error: You must provide at least width and height.")
                return

            diameter = float(args[0])
            height = float(args[1])
            shrinkage = 0.12
            wall_thickness = .25

            for arg in args[2:]:
                if arg.startswith("shrinkage="):
                    shrinkage = float(arg.split("=")[1])
                elif arg.startswith("wall_thickness="):
                    wall_thickness = float(arg.split("=")[1])

            values = inner_inch_dimensions_to_all_values(shrinkage, diameter, height, wall_thickness)
            output(values)
            # print(f"width: {diameter}")
            # print(f"height: {height}")
            # print(f"wall_thickness: {wall_thickness}")
            # print(f"shrinkage: {shrinkage}")
        except (IndexError, ValueError) as e:
            print("Error parsing arguments. Usage: desired <width> <height> [shrinkage=0.12] [wall_thickness=0.25]")
            print(f"Details: {e}")

    # def do_desired(self, width, height, shrinkage=0.12, wall_thickness=.25):


if __name__ == '__main__':
    PotteryCLI().cmdloop()
