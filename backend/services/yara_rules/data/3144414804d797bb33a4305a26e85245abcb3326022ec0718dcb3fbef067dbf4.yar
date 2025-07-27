rule auto_rule_20250727042614_0034 {
  strings:
    $o0 = "dword_4C1288" wide ascii nocase
    $o1 = "byte_4C1634" wide ascii nocase
  condition:
    all of them
}