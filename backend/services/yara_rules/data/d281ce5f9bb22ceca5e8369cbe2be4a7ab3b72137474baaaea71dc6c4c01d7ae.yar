rule auto_rule_20250726100018_2042 {
  strings:
    $o0 = "init" wide ascii nocase
    $o1 = "dword_78160" wide ascii nocase
  condition:
    all of them
}