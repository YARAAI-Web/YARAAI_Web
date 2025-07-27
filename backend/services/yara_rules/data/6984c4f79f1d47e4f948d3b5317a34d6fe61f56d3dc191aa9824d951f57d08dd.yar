rule auto_rule_20250726175325_9586 {
  strings:
    $o0 = "dword_45776C" wide ascii nocase
    $o1 = "dword_457A4C" wide ascii nocase
  condition:
    all of them
}