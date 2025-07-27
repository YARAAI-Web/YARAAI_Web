rule auto_rule_20250726203034_1539 {
  strings:
    $o0 = "__initconin" wide ascii nocase
    $o1 = "dword_4674E0" wide ascii nocase
  condition:
    all of them
}