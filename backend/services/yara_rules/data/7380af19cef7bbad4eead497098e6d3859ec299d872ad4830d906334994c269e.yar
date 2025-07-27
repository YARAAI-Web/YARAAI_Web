rule auto_rule_20250727041330_1682 {
  strings:
    $o0 = "xC0000093" wide ascii nocase
    $o1 = "dword_468018" wide ascii nocase
  condition:
    all of them
}