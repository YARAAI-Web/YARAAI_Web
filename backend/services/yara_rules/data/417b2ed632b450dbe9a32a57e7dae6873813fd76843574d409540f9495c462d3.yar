rule auto_rule_20250726183606_7317 {
  strings:
    $o0 = "dwHighBytesToSeek" wide ascii nocase
    $o1 = "lpSearchFilter" wide ascii nocase
  condition:
    all of them
}