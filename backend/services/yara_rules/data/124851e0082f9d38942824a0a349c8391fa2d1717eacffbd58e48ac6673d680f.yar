rule auto_rule_20250726140017_7996 {
  strings:
    $o0 = "x1400310A8LL" wide ascii nocase
    $o1 = "Referenced" wide ascii nocase
  condition:
    all of them
}