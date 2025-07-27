rule auto_rule_20250727010608_3278 {
  strings:
    $o0 = "dwCreationDisposition" wide ascii nocase
    $o1 = "aGsyst12111cgcr" wide ascii nocase
  condition:
    all of them
}