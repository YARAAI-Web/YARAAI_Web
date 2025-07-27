rule auto_rule_20250727010351_7092 {
  strings:
    $o0 = "dword_4453CC" wide ascii nocase
    $o1 = "xC9101061" wide ascii nocase
  condition:
    all of them
}