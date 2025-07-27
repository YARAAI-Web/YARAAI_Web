rule auto_rule_20250726180251_8859 {
  strings:
    $o0 = "byte_469BC4" wide ascii nocase
    $o1 = "dword_46A0A8" wide ascii nocase
    $o2 = "x404730" wide ascii nocase
    $o3 = "dword_469BD0" wide ascii nocase
    $o4 = "_pFirstBlock" wide ascii nocase
  condition:
    4 of ($o*)
}