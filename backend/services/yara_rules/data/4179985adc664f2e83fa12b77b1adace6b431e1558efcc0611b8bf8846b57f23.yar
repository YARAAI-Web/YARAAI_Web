rule auto_rule_20250726070819_1776 {
  strings:
    $o0 = "dword_78420" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}