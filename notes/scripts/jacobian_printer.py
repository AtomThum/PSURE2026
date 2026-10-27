lower_vars = ["p_{1x}'", "p_{1y}'", "p_{2x}'", "p_{2y}'"]
upper_vars = ["S_x'", "S_y'", "D_x'", "D_y'"]

def print_jacobian(lower_vars: list[str], upper_vars: list[str]) -> None:
    if len(lower_vars) != len(upper_vars):
        raise ValueError("Lower variables and upper variables length do not match.")

    vars_length = len(lower_vars)
    for upper_var in upper_vars:
        for lower_var_index, lower_var in enumerate(lower_vars, start=1):
            end_string = " & " if lower_var_index != vars_length else " \\\\\n"
            print(f"\\pdv{{{upper_var}}}{{{lower_var}}}", end=end_string)

print_jacobian(lower_vars, upper_vars)
