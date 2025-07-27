rule auto_rule_20250726114441_4350 {
  strings:
    $o0 = "lpCommTimeouts" wide ascii nocase
  condition:
    all of them
}