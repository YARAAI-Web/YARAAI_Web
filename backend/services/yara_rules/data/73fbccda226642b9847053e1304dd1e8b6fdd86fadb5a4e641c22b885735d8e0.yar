rule auto_rule_20250727022326_6749 {
  strings:
    $o0 = "dword_6403034C" wide ascii nocase
  condition:
    all of them
}