rule auto_rule_20250727020638_6623 {
  strings:
    $o0 = "stdenvp" wide ascii nocase
    $o1 = "_forcdecpt" wide ascii nocase
  condition:
    all of them
}