rule auto_rule_20250726085253_8955 {
  strings:
    $o0 = "aNegopenkeyw" wide ascii nocase
  condition:
    all of them
}