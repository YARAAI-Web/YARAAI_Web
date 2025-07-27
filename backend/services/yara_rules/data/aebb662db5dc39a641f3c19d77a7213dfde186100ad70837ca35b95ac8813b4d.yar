rule auto_rule_20250726143528_6291 {
  strings:
    $o0 = "GetStringTypeW" wide ascii nocase
    $o1 = "dword_456CA4" wide ascii nocase
  condition:
    all of them
}