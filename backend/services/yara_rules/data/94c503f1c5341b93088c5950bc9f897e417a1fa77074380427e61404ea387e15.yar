rule auto_rule_20250727030505_8311 {
  strings:
    $o0 = "x3DBEu" wide ascii nocase
    $o1 = "dword_42900C" wide ascii nocase
  condition:
    all of them
}