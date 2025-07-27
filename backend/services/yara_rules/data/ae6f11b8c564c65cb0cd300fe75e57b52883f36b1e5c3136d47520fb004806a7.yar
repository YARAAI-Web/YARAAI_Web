rule auto_rule_20250726202027_6755 {
  strings:
    $o0 = "xF89C853F" wide ascii nocase
    $o1 = "dword_42FCDD" wide ascii nocase
    $o2 = "dword_42FD86" wide ascii nocase
  condition:
    3 of ($o*)
}