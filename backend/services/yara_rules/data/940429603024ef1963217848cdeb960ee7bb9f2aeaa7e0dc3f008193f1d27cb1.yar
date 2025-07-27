rule auto_rule_20250726191800_5864 {
  strings:
    $o0 = "dword_412234" wide ascii nocase
    $o1 = "xcptlookup" wide ascii nocase
  condition:
    all of them
}