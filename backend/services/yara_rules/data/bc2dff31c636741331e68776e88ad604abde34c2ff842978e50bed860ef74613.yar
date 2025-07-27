rule auto_rule_20250726161239_0950 {
  strings:
    $o0 = "dword_449700" wide ascii nocase
    $o1 = "x140u" wide ascii nocase
    $o2 = "dword_449544" wide ascii nocase
  condition:
    3 of ($o*)
}