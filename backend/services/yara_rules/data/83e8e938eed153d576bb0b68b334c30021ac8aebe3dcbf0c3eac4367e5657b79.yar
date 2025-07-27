rule auto_rule_20250726134947_8880 {
  strings:
    $o0 = "_cinit" wide ascii nocase
    $o1 = "byte_469D80" wide ascii nocase
    $o2 = "_fptrap" wide ascii nocase
    $o3 = "dword_469D7C" wide ascii nocase
    $o4 = "objects" wide ascii nocase
  condition:
    4 of ($o*)
}