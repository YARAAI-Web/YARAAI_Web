rule auto_rule_20250726163459_1659 {
  strings:
    $o0 = "dword_4362A8" wide ascii nocase
    $o1 = "dword_436348" wide ascii nocase
    $o2 = "xF89C8527" wide ascii nocase
  condition:
    3 of ($o*)
}