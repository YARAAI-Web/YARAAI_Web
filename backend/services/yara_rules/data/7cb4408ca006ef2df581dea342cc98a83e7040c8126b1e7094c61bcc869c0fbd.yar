rule auto_rule_20250726082210_2146 {
  strings:
    $o0 = "dword_45D274" wide ascii nocase
  condition:
    all of them
}