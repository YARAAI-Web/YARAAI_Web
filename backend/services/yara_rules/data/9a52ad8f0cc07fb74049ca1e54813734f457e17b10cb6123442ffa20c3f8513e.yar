rule auto_rule_20250726203433_7239 {
  strings:
    $o0 = "dword_4C12F8" wide ascii nocase
    $o1 = "WinSearchChildren" wide ascii nocase
  condition:
    all of them
}