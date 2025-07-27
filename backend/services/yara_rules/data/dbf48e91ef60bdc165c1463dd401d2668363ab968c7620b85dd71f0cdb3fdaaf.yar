rule auto_rule_20250727031720_4248 {
  strings:
    $o0 = "dword_4C15DC" wide ascii nocase
    $o1 = "byte_4C10C2" wide ascii nocase
  condition:
    all of them
}