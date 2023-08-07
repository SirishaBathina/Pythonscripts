import sys
if len(sys.argv) != 3:
    print("Usage: python script_name.py <string_variable> <float_variable>")
    sys.exit(1)
string_variable = sys.argv[1]
float_variable = float(sys.argv[2])


formatted_string = "String variable: {}, Float variable: {:.2f}".format(string_variable, float_variable)
