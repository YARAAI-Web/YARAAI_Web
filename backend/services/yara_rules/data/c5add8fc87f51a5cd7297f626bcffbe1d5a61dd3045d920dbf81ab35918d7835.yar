rule auto_rule_20250726140513_5211 {
  strings:
    $o0 = "x510E527F" wide ascii nocase
    $o1 = "E700h" wide ascii nocase
  condition:
    all of them
}