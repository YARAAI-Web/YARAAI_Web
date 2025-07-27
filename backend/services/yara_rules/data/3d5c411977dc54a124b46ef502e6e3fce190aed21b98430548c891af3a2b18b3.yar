rule auto_rule_20250726144801_6767 {
  strings:
    $o0 = "dword_428E89" wide ascii nocase
    $o1 = "x687Du" wide ascii nocase
    $o2 = "x6807u" wide ascii nocase
    $o3 = "dword_428E45" wide ascii nocase
    $o4 = "x75108B1u" wide ascii nocase
  condition:
    4 of ($o*)
}