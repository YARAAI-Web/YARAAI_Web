rule auto_rule_20250727024401_5087 {
  strings:
    $o0 = "x10CE1C57" wide ascii nocase
  condition:
    all of them
}