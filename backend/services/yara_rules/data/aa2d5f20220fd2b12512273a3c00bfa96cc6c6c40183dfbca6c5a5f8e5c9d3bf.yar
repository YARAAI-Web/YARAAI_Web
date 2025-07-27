rule auto_rule_20250726235458_2523 {
  strings:
    $o0 = "dword_41D964" wide ascii nocase
    $o1 = "dword_41D96C" wide ascii nocase
  condition:
    all of them
}