rule auto_rule_20250727000648_6294 {
  strings:
    $o0 = "dword_780D8" wide ascii nocase
  condition:
    all of them
}