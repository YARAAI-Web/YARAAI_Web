rule auto_rule_20250726073146_5507 {
  strings:
    $o0 = "xF89C853D" wide ascii nocase
    $o1 = "x59D6" wide ascii nocase
    $o2 = "dword_42FCD5" wide ascii nocase
  condition:
    3 of ($o*)
}