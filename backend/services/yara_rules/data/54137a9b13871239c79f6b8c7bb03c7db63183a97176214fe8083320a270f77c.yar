rule auto_rule_20250726210854_6014 {
  strings:
    $o0 = "dword_43540C" wide ascii nocase
  condition:
    all of them
}