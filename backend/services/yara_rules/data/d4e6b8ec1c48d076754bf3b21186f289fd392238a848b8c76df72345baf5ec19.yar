rule auto_rule_20250727011831_7604 {
  strings:
    $o0 = "dword_4698E8" wide ascii nocase
    $o1 = "dword_469D3C" wide ascii nocase
  condition:
    all of them
}