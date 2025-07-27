rule auto_rule_20250726092719_5105 {
  strings:
    $o0 = "frndint" wide ascii nocase
    $o1 = "dword_47DC38" wide ascii nocase
  condition:
    all of them
}