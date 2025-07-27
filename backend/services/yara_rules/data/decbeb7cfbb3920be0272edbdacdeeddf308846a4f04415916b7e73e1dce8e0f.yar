rule auto_rule_20250726174717_9550 {
  strings:
    $o0 = "x7EDB" wide ascii nocase
    $o1 = "dword_484B88" wide ascii nocase
    $o2 = "xE0EE" wide ascii nocase
  condition:
    3 of ($o*)
}