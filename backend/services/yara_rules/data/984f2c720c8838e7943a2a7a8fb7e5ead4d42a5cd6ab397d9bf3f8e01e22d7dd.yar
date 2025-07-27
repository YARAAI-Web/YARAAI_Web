rule auto_rule_20250726235634_4543 {
  strings:
    $o0 = "atol" wide ascii nocase
    $o1 = "found_bx" wide ascii nocase
    $o2 = "dword_45D274" wide ascii nocase
    $o3 = "_except_handler3" wide ascii nocase
  condition:
    4 of ($o*)
}