rule auto_rule_20250727030053_6979 {
  strings:
    $o0 = "xFABF2DFF" wide ascii nocase
    $o1 = "xF89C853F" wide ascii nocase
    $o2 = "dword_4305C2" wide ascii nocase
  condition:
    3 of ($o*)
}