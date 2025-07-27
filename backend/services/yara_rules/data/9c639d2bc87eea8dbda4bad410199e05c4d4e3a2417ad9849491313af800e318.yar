rule auto_rule_20250726123156_4836 {
  strings:
    $o0 = "dword_460774" wide ascii nocase
  condition:
    all of them
}