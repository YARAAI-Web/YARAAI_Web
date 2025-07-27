rule auto_rule_20250726155932_6168 {
  strings:
    $o0 = "dword_43381B" wide ascii nocase
    $o1 = "x2832u" wide ascii nocase
    $o2 = "x3FD8" wide ascii nocase
  condition:
    3 of ($o*)
}