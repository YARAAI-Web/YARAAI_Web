rule auto_rule_20250726072858_1245 {
  strings:
    $o0 = "x48F7u" wide ascii nocase
    $o1 = "uFlags" wide ascii nocase
    $o2 = "dword_42E50D" wide ascii nocase
    $o3 = "xF89C85B0" wide ascii nocase
    $o4 = "aD5nRq71sJtew" wide ascii nocase
  condition:
    4 of ($o*)
}