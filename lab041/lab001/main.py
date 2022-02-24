import toml

toml_string = """# This is a TOML document. Boom.

title = "TOML Example"
the-void = [[[[[]]]]]
mixed = [[1, +2], ["a", "b"], [1.0, 2.0]]
avogadro = 6.23e23

[owner]
organization = "GitHub"
bio = "GitHub Cofounder & CEOLikes tater tots and beer."
dob = 1979-05-27T07:32:00Z # First class dates? Why not?

[database]
server = "192.168.1.1"
ports = [ 8001, 8001, 8002 ]
connection_max = 5000
enabled = true
test = [["a"], ["b"], ["c"]]
"""

parsed_toml = toml.loads(toml_string)
print(parsed_toml)

print(parsed_toml['database']['server'])
