rule auto_rule_20250726080748_8199 {
  strings:
    $o0 = "dword_455034" wide ascii nocase
    $o1 = "dword_455620" wide ascii nocase
    $o2 = "x61u" wide ascii nocase
    $o3 = "LStrDelete" wide ascii nocase
  condition:
    4 of ($o*)
}