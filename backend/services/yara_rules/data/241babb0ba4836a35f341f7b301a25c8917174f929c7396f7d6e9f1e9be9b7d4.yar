rule auto_rule_20250726173913_1938 {
  strings:
    $o0 = "dword_41158C" wide ascii nocase
    $o1 = "_setenvp" wide ascii nocase
    $o2 = "_cinit" wide ascii nocase
    $o3 = "byte_407B50" wide ascii nocase
    $o4 = "_ctype" wide ascii nocase
  condition:
    4 of ($o*)
}