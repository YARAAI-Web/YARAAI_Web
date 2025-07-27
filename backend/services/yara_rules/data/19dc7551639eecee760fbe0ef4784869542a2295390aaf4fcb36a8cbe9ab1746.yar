rule auto_rule_20250726065307_2532 {
  strings:
    $o0 = "dwCreationDisposition" wide ascii nocase
    $o1 = "dword_43F9B8" wide ascii nocase
  condition:
    all of them
}