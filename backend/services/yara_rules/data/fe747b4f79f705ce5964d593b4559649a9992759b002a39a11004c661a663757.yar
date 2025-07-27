rule auto_rule_20250726154826_2420 {
  strings:
    $o0 = "dword_78480" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}