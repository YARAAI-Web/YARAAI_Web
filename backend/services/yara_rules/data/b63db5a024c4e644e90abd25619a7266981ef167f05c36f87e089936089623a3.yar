rule auto_rule_20250726172951_6302 {
  strings:
    $o0 = "x2B4u" wide ascii nocase
    $o1 = "dword_40CDD8" wide ascii nocase
  condition:
    all of them
}