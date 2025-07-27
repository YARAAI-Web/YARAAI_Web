rule auto_rule_20250726100218_0341 {
  strings:
    $o0 = "aIopixklzawercd" wide ascii nocase
  condition:
    all of them
}