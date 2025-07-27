rule auto_rule_20250726103723_1337 {
  strings:
    $o0 = "dword_640303EC" wide ascii nocase
    $o1 = "isprint" wide ascii nocase
  condition:
    all of them
}