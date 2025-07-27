rule auto_rule_20250726060115_3611 {
  strings:
    $o0 = "xFFFFu" wide ascii nocase
    $o1 = "dword_4C12A4" wide ascii nocase
  condition:
    all of them
}