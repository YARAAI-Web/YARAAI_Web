rule auto_rule_20250727010737_6304 {
  strings:
    $o0 = "byte_450181" wide ascii nocase
    $o1 = "CodePagea" wide ascii nocase
  condition:
    all of them
}