rule auto_rule_20250726195329_1284 {
  strings:
    $o0 = "dword_45C314" wide ascii nocase
  condition:
    all of them
}